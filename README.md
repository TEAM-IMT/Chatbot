# Chatbot

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/TatianaMoreno47/Chatbot">
    <img src="Presentation/logo.png" alt="Logo" width="720" >
  </a>

  <h3 align="center"> Clementine (Chatbot) </h3>

  <p align="center">
    Implementation of chatbot in rasa to consult universities around the world
    <br />
    <a href="https://github.com/TatianaMoreno47/Chatbot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TatianaMoreno47/Chatbot/blob/Main/demo.mp4">View Demo</a>
    ·
    <a href="https://github.com/TatianaMoreno47/Chatbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/TatianaMoreno47/Chatbot/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Proyecto to Chatbot with Rasa

### Built With
* [rasa](https://rasa.com/)
* [pyspellchecker](https://pyspellchecker.readthedocs.io/en/latest/quickstart.html)

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
Install virtual environment with venv or conda.

### Installation

1. Activate environment
	```sh
   source {venv_path}/bin/activate
   ```
1. Clone the repo
   ```sh
   git clone https://github.com/TEAM-IMT/Chatbot.git
   ```
2. Install requerements
   ```sh
   pip install -U requirements.
   ```

<!-- USAGE EXAMPLES -->
## Usage
If you want, you can train the model with the instruction
```sh
   rasa train
   ```
You can also download the pre-trained weights from the following [link](https://drive.google.com/file/d/100WauINufg7QWqOoz8AMUC_hrCPDgfXD/view?usp=sharing). Copy the file into the `models` folder. 

Then, just run the actions-server:
```sh
   rasa run actions
   ```
And finally, start a new conversation with Clementine!
```sh
   rasa shell
   ```

For more information, see the following links:

1. [Rasa framework](https://rasa.com/)
2. [Knowledge Base Actions](https://rasa.com/docs/action-server/knowledge-bases/)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/TatianaMoreno47/Chatbot/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact
* Johan Mejia (johan-steven.mejia-mogollon@imt-atlantique.net) - [![Linkend][linkedin-shield]][linkedin-url-1]
* Tatiana Moreno (jenny-tatiana.moreno-perea@imt-atlantique.net) - [![Linkend][linkedin-shield]][linkedin-url-2]
* Diego Carreño (diego-andres.carreno-avila@imt-atlantique.net) - [![Linkend][linkedin-shield]][linkedin-url-3]
* Project Link: [https://github.com/TatianaMoreno47/Chatbot](https://github.com/TatianaMoreno47/Chatbot)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) for providing the repository README template. 
<!-- * [UE TAL 2020 Chatbot](https://github.com/valeporti/imt_chatbot) for serving as the basis of the project, as well as providing examples of intentions. -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TatianaMoreno47/Chatbot.svg?style=for-the-badge
[contributors-url]: https://github.com/TatianaMoreno47/Chatbot/network/contributors
[forks-shield]: https://img.shields.io/github/forks/TatianaMoreno47/Chatbot.svg?style=for-the-badge
[forks-url]: https://github.com/TatianaMoreno47/Chatbot/network/members
[stars-shield]: https://img.shields.io/github/stars/TatianaMoreno47/Chatbot.svg?style=for-the-badge
[stars-url]: https://github.com/TatianaMoreno47/Chatbot/stargazers
[issues-shield]: https://img.shields.io/github/issues/TatianaMoreno47/Chatbot.svg?style=for-the-badge
[issues-url]: https://github.com/TatianaMoreno47/Chatbot/issues
[license-shield]: https://img.shields.io/github/license/TatianaMoreno47/Chatbot.svg?style=for-the-badge
[license-url]: https://github.com/TatianaMoreno47/Chatbot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url-1]: https://www.linkedin.com/in/johansmm/
[linkedin-url-2]: https://www.linkedin.com/in/tatiana-moreno-perea/
[linkedin-url-3]: https://www.linkedin.com/in/diego-andres-carre%C3%B1o-49b2ab157/
