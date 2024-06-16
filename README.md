<br />
<div align="center">
  <a href="/url">
    <img src="./static/assets/url-shortener-logo.png" alt="Url Shortener Logo" height="150">
  </a>

<h3 align="center">
    Url-Shortener - A Simple Url Shortener Service 
</h3>

  <p align="center">
    A simple url shortener service built with Flask, providing a RESTful API for shortening urls.
    <br />
    <br />
    <a href="https://github.com/openceJav/docs-required/issues">Report Bug</a>
    ✱
    <a href="https://github.com/openceJav/docs-required/issues">Request Feature</a>
    ✱
    <a href="/">Documentation</a>
  </p>
</div>
<div align="center">
    <!-- Build Status & Other Information -->
    <a href="/url">
        <img src="https://img.shields.io/github/issues/Hi-kue/url-shortener-flpy" alt="Issues">
    </a>
    <a href="/url">
        <img src="https://img.shields.io/github/forks/Hi-kue/url-shortener-flpy" alt="Forks">
    </a>
    <a href="/url">
        <img src="https://img.shields.io/github/stars/Hi-kue/url-shortener-flpy" alt="Stars">
    </a>
    <a href="/url">
        <img src="https://img.shields.io/github/license/Hi-kue/url-shortener-flpy" alt="License">
    </a>
</div>
<div align="center">
    <!-- Badges & Built-With -->
    <img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/-Flask-%23000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
    <img src="https://img.shields.io/badge/-Tailwind%20CSS-%23068BFB?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
    <img src="https://img.shields.io/badge/-SQLite-%23003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</div>

## Table of Contents

- [About The Project](#about-the-project)
- [Installation](#installation)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## About The Project

This project is a simple url shortener service built with Flask, 
providing a RESTful API for shortening urls. It was built as a learning guide
for Flask and is referenced from a LinkedIn Learning course on Flask.

If you would like to know the course, please check the [Acknowledgements](#acknowledgements) section.

## Installation

Installing the repository is as simple as cloning the repository and installing the
dependencies; The following steps will guide you through the process.

1. Clone the repository
```shell
git clone https://github.com/Hi-kue/url-shortener-flpy.git
```

2. Change into the project directory
```shell
cd url-shortener-flpy
```

3. Create a virtual environment using pipenv (make sure to have it installed)
```shell
pipenv shell
```

4. Install the dependencies (pipenv)
```shell
pipenv install -r requirements.txt
```

5. Install the dependencies (npm)
```shell
npm install 
```

6. Start both the backend and frontend services (2 terminals)
```shell
# Terminal 1
npm run build

# Terminal 2
flask start
```

You should now have the application running on `http://localhost:5000`, or any other port you specified.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, 
and create. Please read the [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct,
and the process for submitting pull requests. Any contributions you make are **greatly appreciated**.

![URL-Shortener Analytics](https://repobeats.axiom.co/api/embed/6a30f9045c4ddbd8c4603473f8763014b42740d2.svg "Url Shortener Analytics")

## Acknowledgements

This project was referenced from a LinkedIn Learning course covering the Flask framework.
The course is titled [Flask Essential Training](https://www.linkedin.com/learning/flask-essential-training/) 
by [LinkedIn Learning](https://www.linkedin.com/learning/).

Huge thanks to the author Nick Walter for the amazing course!
