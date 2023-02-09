import pytest

from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word = "developer"
    with pytest.raises(UnicodeDecodeError):
        count_ocurrences(path, word)