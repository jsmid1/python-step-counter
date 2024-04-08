#!/bin/bash

test_dir="./tests"
e2e_tests_defaults="$test_dir/e2e/test_defaults"
e2e_ib111_tests="$test_dir/e2e/test_ib111"

for test in "$e2e_tests_defaults"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    echo "$test"
    python -m unittest "$test"
    echo ""
done

for test in "$e2e_ib111_tests"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    echo "$test"
    python -m unittest "$test"
    echo ""
done
