#!/bin/bash

test_dir="./tests"
e2e_tests_defaults="$test_dir/e2e/test_defaults"
e2e_ib111_tests="$test_dir/e2e/test_ib111"
e2e_complexity_tests="$test_dir/e2e/test_complexity"

for test in "$e2e_tests_defaults"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    echo "3.10:$test"
    python3.10 -m unittest "$test"
    echo "3.11:$test"
    python3.11 -m unittest "$test"

    if [[ "$test" != "int_test.py" ]]; then
        echo "3.12:$test"
        python3.12 -m unittest "$test"
    fi

    echo ""
done

for test in "$e2e_ib111_tests"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    echo "3.10:$test"
    python3.10 -m unittest "$test"
    echo "3.11:$test"
    python3.11 -m unittest "$test"
    echo "3.12:$test"
    python3.12 -m unittest "$test"
    echo ""
done

for test in "$e2e_complexity_tests"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    echo "3.10:$test"
    python3.10 -m unittest "$test"
    echo "3.11:$test"
    python3.11 -m unittest "$test"
    echo "3.12:$test"
    python3.12 -m unittest "$test"
    echo ""
done
