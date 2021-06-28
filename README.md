<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[**Enlish**](https://github.com/hungtangwei/django_restapi_ml_model/) | [**中文**](https://github.com/ymcui/Chinese-BERT-wwm/blob/master/README_EN.md)
<br />
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->

<br />
<p align="center">
  <a href="https://github.com/hungtangwei/django_restapi_ml_model">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Deploy Machine Learning Models with Django</h3>

  <p align="center">
    A tutorial to deploy machine learning models with Django 3.2.4
    <br />
    <a href="https://github.com/hungtangwei/django_restapi_ml_model"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hungtangwei/django_restapi_ml_model">View Demo</a>
    ·
    <a href="https://github.com/hungtangwei/django_restapi_ml_model/issues">Report Bug</a>
    ·
    <a href="https://github.com/hungtangwei/django_restapi_ml_model/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
  <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#start">Start</a>
      <ul>
        <li><a href="#setup-git-repository">Setup git repository</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#start-django-project">Start Django project</a></li>
      </ul>
    </li>
    <li>
      <a href="#build-ml-model">Build ML algorithms</a>
      <ul>
        <li><a href="#set-jupyter-notebook">Setup Jupyter notebook</a></li>
        <li><a href="#train-ml-model">Train ML algorithms</a></li>
      </ul>
    </li>
    <li>
      <a href="#django-models">Django models</a>
      <ul>
        <li><a href="#create-django-models">Create Django models</a></li>
        <li><a href="#create-restful-api-for-models">Create RESTFUL API for models</a></li>
      </ul>
    </li>
    <li>
      <a href="#add-ml-models-to-the-server">Add ML algorithms to the server</a>
      <ul>
        <li><a href="#ml-code-in-the-server">ML code in the server</a></li>
        <li><a href="#algorithms-registry">Algorithms registry</a></li>
        <li><a href="#add-ml-models-to-the-registry">Add ML algorithms to the registry</a></li>
      </ul>
    </li>
    <li>
      <a href="#making-predictions">Making predictions</a>
      <ul>
        <li><a href="#predictions-view">Predictions view</a></li>
        <li><a href="#add-tests-for-predict-view">Add tests for PredictView</a></li>
      </ul>
    </li>
    <li>
      <a href="#ab-testing">A/B testing</a>
      <ul>
        <li><a href="#add-second-ml-model">Add second ML algorithm</a></li>
        <li><a href="#create-ab-model-in-the-database">Create A/B model in the database</a></li>
      </ul>
    </li>
    <!-- <li>
      <a href="#containers">Containers</a>
      <ul>
        <li><a href="#prep-code">Prepare the code</a></li>
        <li><a href="#docker">Dockerfiles</a></li>
      </ul>
    </li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- Introduction -->
## Introduction
This tutorial will introduce how to build Machine Learning system available with RESTFUL API by Django framework.

In this repository, The versions for building the Machine Learning service are Python 3.8.10 and Django 3.2.4.

This tutorial is suitable for readers who are familiar with Machine Learning and would like to learn how to build Machine Learning web services. Therefore, basic Python knowledge is required.
<!-- Start -->
## Start 
In this chapter, here are four main tasks you will learn:
* How to set up a git repository.
* Setup environment for development.
* Install required packages.
* Start the Django project.

#### Setup Git Repository
The first step is to create a new repository in GitHub.
![Create new repository][create-repo-screenshot]
<br />
Then please go to your terminal and set the repository:
```sh
  git clone [your repository url]
  cd django_restapi_ml
  ls -l
  ```
To check files in the repository.

#### Installation
Let's set up and activate the environment for development.
I will use pyenv + pipenv to set up the environment.

1. To install the python version in pyenv and set python version in pyenv:
```sh
  pyenv install 3.8.10
  pyenv local 3.8.10
  ```

<br />

2. Install pipenv and set up python version and install libraries:
```sh
  pip install pipenv
  pipenv install --python 3.8.10 django==3.2.4 djangorestframework sklearn numpy pandas 
  ```
<br />

3. Run the virtual machine:
```sh
  pipenv shell
  ```

#### Start Django Project


<!-- Build ML Model -->
## Build ML Model

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)

#### Set Jupyter Notebook

#### Train ML Model


<!-- Django modles -->
## Django Models

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

#### Create Django Models


#### Create RESTful API For Models


<!-- Add ML models to the server-->
## Add ML Models To The Server

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

#### ML Code In The Server


#### Algorithms Registry


#### Add ML Models To The Registry


<!-- Making Predictions -->
## Making Predictions

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```


#### Predictions View

#### Add Tests For Predict View

<!-- A/B Testing -->
## AB Testing

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

#### Add Second ML Model


#### Create AB Model In The Database

<!-- ROADMAP
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues). -->



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

Tang-Wei, Hung  - hung.tangwei@gmail.com

Project Link: [https://github.com/hungtangwei/django_restapi_ml_model](https://github.com/hungtangwei/django_restapi_ml_model)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hungtangwei/django_restapi_ml_model.svg?style=for-the-badge
[contributors-url]: https://github.com/hungtangwei/django_restapi_ml_model/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hungtangwei/django_restapi_ml_model.svg?style=for-the-badge
[forks-url]: https://github.com/hungtangwei/django_restapi_ml_model/network/members
[stars-shield]: https://img.shields.io/github/stars/hungtangwei/django_restapi_ml_model.svg?style=for-the-badge
[stars-url]: https://github.com/hungtangwei/django_restapi_ml_model/stargazers
[issues-shield]: https://img.shields.io/github/issues/hungtangwei/django_restapi_ml_model.svg?style=for-the-badge
[issues-url]: https://github.com/hungtangwei/django_restapi_ml_model/issues
[license-shield]: https://img.shields.io/github/license/hungtangwei/django_restapi_ml_model.svg?style=for-the-badge
[license-url]: https://github.com/hungtangwei/django_restapi_ml_model/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tang-wei-hung-4a3042165/
[create-repo-screenshot]: images/create_repo.png
