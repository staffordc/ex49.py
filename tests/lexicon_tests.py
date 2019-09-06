from nose.tools import *
from lexicon import lexicon


def test_empty_returns_nothing():
    assert_equal(lexicon.scan(""), [])


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])


def test_directions_2():
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'), ('direction', 'east')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
