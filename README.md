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
│   └── tests                 <= a root package for all automated tests
│       ├── api               <= API-related tests
│       ├── deployment        <= deployment-related tests
│       └── web               <= WEB-related tests
├── suite.py                  <= a job file to run all tests
└── requirements.txt          <= Python packages for automated tests execution
``` 

## Usage of automated tests
### Installation
Please use Python `3.6.5` for the test execution.

Before running any command, please install required Python's dependencies with 
```bash
pip install -r requirements.txt
```

### Execution
If you need to run whole tests suite, please run 

```bash
python suite.py -testbed_file testbed.yaml
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

### Creating a virtual machine for application using Vagrant 
To be able to use this type of run, you need to have Vagrant engine release 2.2.4+ and Virtualbox 
engine release  5.2.28+. 

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

Then you can run  `suite.py` to run all tests 


If you want to shutdown vm you must run:
```bash
vagrant halt
``` 

If you want to delete vm you must run:
```bash
vagrant destroy
```

### Deploy and destroy application
If you want to deploy the application to localhost, you need to run in the terminal
```bash
sudo docker-compose up
```
After that you can enter in the browser's search field 
```text
https://127.0.0.1 or https://localhost
```
and use the application.
If you need to destroy application, run in the terminal
```bash
sudo docker-compose down
```




