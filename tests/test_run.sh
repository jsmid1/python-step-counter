#!/bin/bash

test_dir="./tests"
e2e_tests_defaults="$test_dir/e2e/test_defaults"
e2e_ib111_tests="$test_dir/e2e/test_ib111"
e2e_complexity_tests="$test_dir/e2e/test_complexity"


run_setup() {
    local python_version=$1

    if command -v "python$python_version" >/dev/null 2>&1; then
        echo "Setting up python$python_version"
        "python$python_version" setup.py build_ext --inplace

    else
        echo "Python $python_version is not installed. Skipping setup for $python_version."
    fi
    echo ""
}

run_setup 3.10
run_setup 3.11
run_setup 3.12

run_test() {
    local python_version=$1
    local test_path=$2

    if command -v "python$python_version" >/dev/null 2>&1; then
        echo "$python_version:$test_path"
        "python$python_version" -m unittest "$test_path"
    else
        echo "Python $python_version is not installed. Skipping tests for $python_version."
    fi
    echo ""
}

for test in "$e2e_tests_defaults"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    run_test 3.10 "$test"
    run_test 3.11 "$test"

    if [[ "$test" != "int_test.py" ]]; then
        run_test 3.12 "$test"
    fi

    echo ""
done

for test in "$e2e_ib111_tests"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    run_test 3.10 "$test"
    run_test 3.11 "$test"
    run_test 3.12 "$test"
    echo ""
done

for test in "$e2e_complexity_tests"/*
do
    base_test=$(basename "$test")

    if [[ "$base_test" == "__pycache__" ]]; then
        continue
    fi

    run_test 3.10 unittest "$test"
    run_test 3.11 unittest "$test"
    run_test 3.12 unittest "$test"
    echo ""
done
