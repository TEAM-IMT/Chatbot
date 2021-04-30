
# Take from https://nicks-cheke44.medium.com/building-rasa-nlu-custom-component-for-spell-checking-in-incoming-message-742527b35d27
import typing, re
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
if typing.TYPE_CHECKING: from rasa.nlu.model import Metadata
from rasa.shared.nlu.constants import INTENT

from spellchecker import SpellChecker
spell = SpellChecker()

class SpellingAnalyzer(Component):

    name = "spell_analyzer"
    provides = ["entities", "intent", "intent_ranking"]
    requires = ["message", "intent", "intent_ranking"]
    language_list = ["en"]

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None):
        super(SpellingAnalyzer, self).__init__(component_config)

    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def process(self, message: Message, **kwargs):
        """Retrieve the text message, do spelling correction word by word,
        then append all the words and form the sentence,
        pass it to next component of pipeline"""
        try: textdata = re.sub("[^\s\w']", '', message.data['text']).split() # Fix bug with punctuation
        except: textdata = ['pass']
        wrong_words = list(spell.unknown(textdata)) # Get misspelling words
        if len(wrong_words) > 0:
            intent_name = message.get('intent')['name']
            entities = message.get('entities') + [ # New entities + previous
                {"value": wrong_words, "confidence": 1.0, "entity": "wrong_words", "extractor": "spell_analyzer"},
                {"value": [spell.correction(w) for w in wrong_words], "confidence": 1.0, "entity": "correct_words", "extractor": "spell_analyzer"},
                {"value": intent_name, "confidence": 1.0, "entity": "last_intent", "extractor": "spell_analyzer"}
            ]
            intent = {"id": hash("fix_mispelling"), "name": "fix_mispelling", "confidence": 1.0}
            intent_ranking = message.get('intent_ranking') + [intent] # Add new intention
            message.set(INTENT, intent, add_to_output = True)
            message.set("intent_ranking", intent_ranking, add_to_output = True)
            message.set("entities", entities, add_to_output = True)
    
    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Pass because a pre-trained model is already persisted"""
        pass
