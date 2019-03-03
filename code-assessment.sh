#!/usr/bin/env bash
(
    black --check .
    pylint oct suite.py
) || (
    cat <<RESULT

===================================================
= Code assessment is failed! Please fix errors!!! =
===================================================
RESULT
)