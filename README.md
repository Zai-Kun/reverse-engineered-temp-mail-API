
<div align="center">
  <a href="https://github.com/Zai-Kun/reverse-engineered-temp-mail-API">  </a>

<h1 align="center">Reverse Engineered <a href="https://temp-mail.org">Temp Mail</a> API</h1>

  <p align="center">
    Use Temp Mail in your Python code without an API key

[![Stargazers][stars-badge]][stars-url]
[![Forks][forks-badge]][forks-url]
[![Discussions][discussions-badge]][discussions-url]
[![Issues][issues-badge]][issues-url]
[![MIT License][license-badge]][license-url]

  </p>
    <p align="center">
    <a href="https://github.com/Zai-Kun/reverse-engineered-temp-mail-API"></a>
    <a href="https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/issues">Report Bug</a>
    |
    <a href="https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/discussions">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
        <li><a href="#how-it-works">How it works</a></li>
        <li><a href="#built-using">Built using</a></li>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This project can be used to integrate temporary email services into your python code. You can use this project to receive emails from temporary disposable mail boxes directly into your Python code. You can create as many email ids as you want, and view mailboxes from previously created email ids.

This can be useful if you want to test your project which uses email with various different email ids, or to integrate your code with other API's which require email verification.

### Inspiration

Temp mail has an official API which can be used to interface your Python code to it, but it needs to be used with an API key. This project aims to fulfil the same purpose without using an API key.

### How it works

[Temp Mail](https://temp-mail.org) website requests have been reverse engineered, and directly integrated into Python requests. Hence, any requests made using this script is a simulated request made by a user directly on the website.

### Built Using

* [![Python][python-badge]][python-url]
* [![aiohttp][aiohttp-badge]][aiohttp-url]
* [![Beautiful Soup][beautiful-soup-badge]][beautiful-soup-url]

## Getting Started

### Prerequisites

* Python >= 3.9

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Zai-Kun/reverse-engineered-temp-mail-API.git
   ```

2. Install the necessary pip packages:

    ```sh
    pip install -r reverse-engineered-temp-mail-API/requirements.txt
    ```

3. Copy the `temp_mail` directory into your project directory. To do this, copy the `temp_mail` folder from the `reverse-engineered-temp-mail-API` directory and paste it into your project folder.

## Usage

Refer [example_usage.py](/example_usage.py) for the guide on using the library.

## Roadmap

* [x] Use multiple email ids
* [x] View mailbox of previously created email id

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Apache License 2.0. See [`LICENSE`](https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/blob/main/LICENSE
) for more information.

## Contact

Zai-Kun - [Discord Server](https://discord.gg/ymcqxudVJG)

Repo Link: [https://github.com/Zai-Kun/reverse-engineered-temp-mail-API](https://github.com/Zai-Kun/reverse-engineered-temp-mail-API)

## Acknowledgments

* [sudoAlphaX](https://github.com/sudoAlphaX)

* [Leonard Richardson (Beautiful Soup)](https://www.crummy.com/self/)

* [aio-libs (aiohttp)](https://github.com/aio-libs/aiohttp)

* [othneildrew (README Template)](https://github.com/othneildrew)

<!-- MARKDOWN LINKS & IMAGES -->
[forks-badge]: https://img.shields.io/github/forks/Zai-Kun/reverse-engineered-temp-mail-API
[forks-url]: https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/network/members
[stars-badge]: https://img.shields.io/github/stars/Zai-Kun/reverse-engineered-temp-mail-API
[stars-url]: https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/stargazers
[issues-badge]: https://img.shields.io/github/issues/Zai-Kun/reverse-engineered-temp-mail-API
[issues-url]: https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/issues
[discussions-badge]: https://img.shields.io/github/discussions/Zai-Kun/reverse-engineered-temp-mail-API
[discussions-url]: https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/discussions
[python-badge]: https://img.shields.io/badge/Python-blue?logo=python&logoColor=yellow
[python-url]: https://www.python.org/
[beautiful-soup-badge]: https://img.shields.io/badge/Beautiful%20Soup-4.12.2-green
[beautiful-soup-url]: https://www.crummy.com/software/BeautifulSoup/
[aiohttp-url]: https://github.com/aio-libs/aiohttp
[aiohttp-badge]: https://img.shields.io/static/v1?message=AIOHTTP&color=2C5BB4&logo=AIOHTTP&logoColor=FFFFFF&label=
[license-badge]: https://img.shields.io/github/license/Zai-Kun/reverse-engineered-temp-mail-API
[license-url]: https://github.com/Zai-Kun/reverse-engineered-temp-mail-API/blob/main/LICENSE
