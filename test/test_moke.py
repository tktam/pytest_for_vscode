import sys
sys.path.insert(0,'T:\\Programming\\VSCODE\\testing')

import MokedModules
from MokedModules import *
from datetime import *
from pytest import *

def test_mock_double(monkeypatch):
    monkeypatch.setattr(MokedModules, 'KTCONST', 2)
    expected = 4
    actual = double_const()  # now it returns 4, not 2

    assert expected == actual


def test_mock_function(monkeypatch):
    monkeypatch.setattr(MokedModules, 'expensive_api_call', mock_return)
    expected = 144
    actual = compute(12)
    assert expected == actual


def mock_return(x=None):
    return 144


def test_datetime():
    test_date = datetime.now()
    test_file = "Current time is {0}".format(test_date)
    return test_file
