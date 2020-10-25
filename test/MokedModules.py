import time
from unittest import mock
from unittest.mock import *


def compute(x):
    response = expensive_api_call(x)
    return response


def expensive_api_call(x):
    time.sleep(10)  # takes 1,000 seconds
    return x*x


def test_compute():
    expected = 144
    actual = compute(12)
    assert expected == actual
