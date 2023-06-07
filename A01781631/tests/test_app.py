from app import lambda_handler
import pytest
import sys
sys.path.append('../src')


def test_lambda_handler():
    result = lambda_handler(None , None)
    assert result == "Hola, A01781631"
