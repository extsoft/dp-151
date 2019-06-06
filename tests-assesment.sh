#!/usr/bin/env bash
declare -a FAILURES

add_fail() {
    FAILURES+=("$1")
}

python suite.py -testbed_file testbed.yaml  || add_fail easypy
if [[ ${#FAILURES[@]} -ne 0 ]]; then
    cat <<RESULT

===================================================
= TEST assessment is failed! Please fix errors!!! =
===================================================
Failed tool(s):
RESULT
    for var in "${FAILURES[@]}"; do
        echo "- ${var}"
    done
    exit 11
fi