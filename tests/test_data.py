import pytest

import spacy
from src.stackoverservices.data.text.converters import lemmatization


@pytest.mark.skip(reason='problem with characters')
def test_lemmatization():
    nlp = spacy.load("en_core_web_sm")
    assert lemmatization(nlp, "don't do") == "do not do"
