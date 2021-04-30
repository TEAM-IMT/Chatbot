# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from typing import Text, Dict, List, Any
from rasa_sdk import utils, Action, Tracker

from spellchecker import SpellChecker
spell = SpellChecker()

chatbot_name = 'Clementine'

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("./data/data_chat.json")
        super().__init__(knowledge_base)

    def utter_attribute_value(self, dispatcher: CollectingDispatcher, object_name: Text,
        attribute_name: Text, attribute_value: Text,):
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.
        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        #dispatcher.utter_message(attachment = "")
        if attribute_value:
            if attribute_name in ['city']:
                dispatcher.utter_message(text = f"{chatbot_name} -> Sure. The {attribute_name} of '{object_name}' is '{attribute_value}'.")
            elif attribute_name in ['careers', 'link', 'scholarship']:
                dispatcher.utter_message(text = f"{chatbot_name} -> Let me check (...). ")
                dispatcher.utter_message(text = f"You can get all the info in : ", attachment = attribute_value)
            elif attribute_name in ['ranking']:
                dispatcher.utter_message(text = f"{chatbot_name} -> Ok. '{object_name}' is the '{attribute_value}' best in the world. Awesome!")
            elif attribute_name in ['cost']:
                if 'http' in attribute_value and '//' in attribute_value:
                    dispatcher.utter_message(text = f"{chatbot_name} -> All the information about costs of {object_name} is in the following link : ", attachment = attribute_value)
                else:
                    dispatcher.utter_message(text = f"{chatbot_name} -> The costs of '{object_name}' are: '{attribute_value}'.")
            else:    
                dispatcher.utter_message(text = f"{chatbot_name} -> '{object_name}' has the value '{attribute_value}' for attribute '{attribute_name}'.")
        else:
            dispatcher.utter_message(
                text = f"{chatbot_name} ->  Did not find a valid value for attribute '{attribute_name}' for object '{object_name}'."
            )

    async def utter_objects(self, dispatcher: CollectingDispatcher, object_type: Text,
        objects: List[Dict[Text, Any]],):
        """
        Utters a response to the user that lists all found objects.
        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if objects:
            dispatcher.utter_message(
                text=f"{chatbot_name} -> Found the following list of universities in '{object_type}':"
            )

            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"{chatbot_name} ->  I could not find any objects of type '{object_type}'."
            )

class ActionSpellingCheck(Action):
    def name(self) -> Text:
        return "action_spelling_check"
        #dispatcher.utter_button_message 
    
    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [] 
        # Erase parameters at the end
        change_slots = [SlotSet("wrong_words", []), SlotSet("correct_words", []), SlotSet("last_intent", []),]

        # Get info words wrong
        wrong_words = tracker.get_slot('wrong_words')[0]
        correct_words = tracker.get_slot('correct_words')[0]
        intent = "/" + tracker.get_slot("last_intent")
        if intent == "/query_knowledge_base": # Fix attributes spellmissing
            for key, value in tracker.slots.items(): # Try to fix some words
                try: 
                    fix_word = spell.correction(value)
                    if fix_word != value: 
                        print("[INFO]: {}:{}".format(value, fix_word))
                        change_slots.append(SlotSet(key, fix_word))
                except: pass
        if len(wrong_words) > 0 and intent != '/nlu_fallback': # List of words to fix or message identified
            print(wrong_words, correct_words, "\n")
            buttons.append({"title": "yes", "payload": intent})
            buttons.append({"title": "no", "payload": "/deny"})
            buttons.append({"title": "really no. But run the action xD", "payload": intent})
            message = " and ".join(["'{}' (you wrote '{}')".format(w[0], w[1]) for w in zip(correct_words, wrong_words)])
            dispatcher.utter_message(text = f"{chatbot_name} -> I don't get it. Did you mean {message} ?", buttons = buttons)
        elif intent == '/nlu_fallback':
            dispatcher.utter_message(response = "utter_ask_rephrase")
        return change_slots

# class ActionSpellingCorrection(Action):
#     def name(self) -> Text:
#         return "action_spelling_correction"
    
#     async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         message_exec = tracker.get_slot("last_intent")
#         if message_exec == 'query_knowledge_base':
#             message_exec = 'action_query_knowledge_base'
#         return [FollowupAction(message_exec), SlotSet("last_intent", "")] # Excecute previous intention
