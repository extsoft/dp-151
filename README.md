# DP-151 group project

The purpose of this repository is to provide automated test suite for 
[OpenCart](https://github.com/bitnami/bitnami-docker-opencart) e-commerce platform.

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
