from calculator import arithmetic
from calculator import trigonometric
import pytest

def test_arithmetic():
    assert(arithmetic("1 + 3 * 7 + 55 -123")) == 77

def test_trigonometric_sin_30(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: '30' if prompt == "What angle? " else 'sin')
    result = trigonometric()
    assert result == 0.5
