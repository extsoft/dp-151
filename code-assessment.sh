#!/usr/bin/env bash
(
    black --check .
) || (
    cat <<RESULT

===================================================
= Code assessment is failed! Please fix errors!!! =
===================================================
RESULT
)