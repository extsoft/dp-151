#!/usr/bin/env bash

declare -a FAILURES

add_fail() {
    FAILURES+=("$1")
}

black --check . || add_fail black
pylint oct suite.py || add_fail pylint
flake8 oct suite.py || add_fail flake8
mypy oct suite.py || add_fail mypy
if [[ ${#FAILURES[@]} -ne 0 ]]; then
    cat <<RESULT

===================================================
= Code assessment is failed! Please fix errors!!! =
===================================================
Failed tool(s):
RESULT
    for var in "${FAILURES[@]}"; do
        echo "- ${var}"
    done
    exit 11
fi
