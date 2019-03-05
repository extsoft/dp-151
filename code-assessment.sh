#!/usr/bin/env bash
(
    black --check .
    pylint oct suite.py
    flake8 oct suite.py
    mypy oct suite.py
) || (
    cat <<RESULT

===================================================
= Code assessment is failed! Please fix errors!!! =
===================================================
RESULT
    exit 11
)
