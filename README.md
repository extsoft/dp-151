# DP-151 group project

The purpose of this repository is to provide automated test suite for 
[OpenCart](https://github.com/bitnami/bitnami-docker-opencart) e-commerce platform.

[![Build Status](https://travis-ci.org/extsoft/dp-151.svg?branch=master)](https://travis-ci.org/extsoft/dp-151)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Project structure
The following directories tree outlines the most important information about project structure:
```text
.
├── README.md                 <= This file which documents the project.
├── archive                   <= pyATS reports directory (excluded from git)
├── oct                       <= a root package
│   ├── __main__.py           <= a job file to run all tests          
│   └── tests                 <= a root package for all automated tests
│       ├── api               <= API-related tests
│       ├── deployment        <= deployment-related tests
│       └── web               <= WEB-related tests
├── tests                     <= Pytest-related tests
├── docker-compose.yaml       <= This file running app in docker
├── Vagrantfile               <= This file create Vagrant VM
├── testbed.yaml              <= This file which topolgy 
├── requirements.txt          <= Python packages for automated tests execution
├── requirements-dev.txt      <= Python packages for quality of the code
└── code-assessment.sh        <= This file running tools for code quality evaluation
``` 

## Usage of automated tests
### Installation
Please use Python `3.6.5` for the test execution.

Before running any command, please install required Python's dependencies with 
```bash
pip install -r requirements.txt
```

### System under test (SUT) installation
#### Vagrant 
This type of launch allows to create a vagrant virtual machine with docker
installed for deploying the application.
 
If you already have virtual machine you can skip this step.

To be able to use this type of run, you need to have 
[Vagrant](https://www.vagrantup.com/) engine release 2.2.4+ 
and [Virtualbox](https://www.virtualbox.org/wiki/Downloads) engine release  5.2.28+. 

A simple way to check Vagrant: 
```bash
vagrant --version
```

A simple way to check Virtualbox:
```bash
vboxmanage --version
``` 

First of all, you need to run:
```bash
vagrant up
```

Now you have a virtual machine and you can deploy the application 
on it using the oct/deployment/deploy_app.py or run all the tests 
with the command described in the next step

If you want to shutdown vm you must run:
```bash
vagrant halt
``` 

If you want to delete vm you must run:
```bash
vagrant destroy
```

#### Docker
This type of launch allows to create a docker container with
application on your PC.

To be able to use this type of run, you need to have
[Docker](https://www.docker.com/) engine release 18.06.1-ce

A simple way to check Docker:
```bash
docker --version
```
First of all, you need to run:
```bash
docker-compose up -d
```
In this case, the application will be launched on the localhost
(127.0.0.1)

If you want to run the application on another IP you need to pass the
parameter with IP:
```bash
APP_HOST="IP" docker-compose up -d
```
If you want to shutdown docker you must run:
```bash
docker-compose down
```

### Execution
If you need to run whole tests suite, please run 

```bash
python -m oct -testbed_file testbed.yaml
```  

If you need to run a particular test, please run
```bash
export PYTHONPATH=$(pwd):${PYTHONPATH}
python oct/tests/web/sample.py
```
where `oct/tests/web/sample.py` has to be replaced with desired test module.

**_Please note!_** If you run WEB tests, please make sure you run the `chromedriver` binary first.

## Development of automated tests
All contributors have to follow 
[Google Python's style guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
until it conflicts with the configured tools for code quality evaluation.

Also, docstrings are optional for the project.

[Type Hints](https://www.python.org/dev/peps/pep-0484/) are mandatory.

### Installation
Please install required Python's dependencies with 
```bash
pip install -r requirements-dev.txt
```

### Code formatting
We use [Black](https://black.readthedocs.io/en/stable/) for the auto-formatting of the code.
This allows supporting of common code style across all contributors and will reduce amount of
lines for either merge conflicts or review.

Please run `black .` to reformat the code according to the projects convention.

### Code assessment
We use some tools to guarantee the quality of the code.

1. [Black](https://black.readthedocs.io/en/stable/) checks the quality of the code formatting.
2. [Pylint](https://pylint.org) analyzes the code and assesses it accordingly.
3. [flake8](http://flake8.pycqa.org/en/latest/) applies some style checks on the code.
4. [pydocstyle](http://www.pydocstyle.org/en/stable/) analyses the quality of docstrings
(executed via `flake8`).
5. [Mypy](https://mypy.readthedocs.io/en/latest/) checks static types.
6. [py.test](https://docs.pytest.org) runs unittests. 

In order to run code assessment, you need to run `./code-assessment.sh` command and make sure
that there is no message like **_Code assessment is failed! Please fix errors!!!_**. If you face
the massage, please fix all violations.
