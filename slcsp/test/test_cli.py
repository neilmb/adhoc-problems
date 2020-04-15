"""Test the SLCSP CLI functions."""

import os

from pathlib import Path
from subprocess import run


def _execute_slcsp(args=[]):
    """Helper to execute our script with the given arguments."""
    # pytest wasn't finding the executable, so compute the path relative to
    # this file
    this_path = Path(os.path.dirname(os.path.realpath(__file__)))
    return run(
        ["python3", this_path.parent / "slcsp.py"] + args,
        text=True,
        capture_output=True,
    )


def test_no_argument():
    result = _execute_slcsp()
    assert result.returncode > 0
    assert "ERROR" in result.stderr


def test_output_header():
    result = _execute_slcsp(["slcsp.csv"])
    assert "zipcode,rate" == result.stdout.splitlines()[0]


def test_complete():
    """Output has a line for every line in the input file."""
    with open("slcsp.csv") as f:
        # count lines in a file from
        # https://www.codespeedy.com/count-the-number-of-lines-in-a-text-file-in-python/
        num_lines = sum(1 for _ in f)
    result = _execute_slcsp(["slcsp.csv"])
    assert len(result.stdout.splitlines()) == num_lines


def test_formatting():
    """Output should have either a rate with two decimal digit or nothing."""
    result = _execute_slcsp(["slcsp.csv"])

    # skip header line
    for line in result.stdout.splitlines()[1:]:
        zipcode, rate = line.split(",")
        if rate:
            assert len(rate.split(".")[1]) == 2
