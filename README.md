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
├── oct.py                    <= a job file to run all tests
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
python oct.py
```  

If you need to run a particular test, please run
```bash
export PYTHONPATH=$(pwd):${PYTHONPATH}
python oct/tests/web/sample.py
```
where `oct/tests/web/sample.py` has to be replaced with desired test module.

## Development of automated tests
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

1. [Black](https://black.readthedocs.io/en/stable/) will check the quality of the code formatting.

In order to run code assessment, you need to run `./code-assessment.sh` command and make sure
that there is no message like **_Code assessment is failed! Please fix errors!!!_**. If you face
the massage, please fix all violations.
