import pytest
from src.apicy.server import app
from starlette.testclient import TestClient


LANG = 'en'
LANG_ERR = 'unknown'
client = TestClient(app)


def test_pos_annotations():
    result = client.post(
        '/%s/pos-annotations' % LANG,
        json={'text': 'This is a test.'}
    )
    result_json = result.json()
    assert result_json == {
        'pos_annotations': [
            {'annotation': 'DT', 'word': {'start': 0, 'text': 'This', 'lemma': 'this'}},
            {'annotation': 'VBZ', 'word': {'start': 5, 'text': 'is', 'lemma': 'be'}},
            {'annotation': 'DT', 'word': {'start': 8, 'text': 'a', 'lemma': 'a'}},
            {'annotation': 'NN', 'word': {'start': 10, 'text': 'test', 'lemma': 'test'}},
            {'annotation': '.', 'word': {'start': 14, 'text': '.', 'lemma': '.'}}
        ]
    }


def test_named_entities():
    result = client.post(
        '/%s/named-entities' % LANG,
        json={'text': 'This is a test from Google.'}
    )
    result_json = result.json()
    assert result_json == {
        'entities': [{
            'end': 26,
            'kind': 'ORG',
            'start': 20,
            'text': 'Google'
        }]
    }


def test_sentences():
    result = client.post(
        '/%s/sentences' % LANG,
        json={'text': 'This is a test.'}
    )
    result_json = result.json()
    assert result_json == {
        'sentences': [
            'This is a test.'
        ]
    }


def test_dependency_parses():
    result = client.post(
        '/%s/dependency-parses' % LANG,
        json={'text': 'This is a test.'}
    )
    result_json = result.json()
    assert result_json == {
        'dep_parses': [
            {
                'start': 0,
                'end': 1,
                'label': 'nsubj',
                'word': {
                    'start': 0,
                    'text': 'This',
                    'lemma': 'this'
                },
                'right': False,
                'root': False
            },
            {
                'start': 1,
                'end': 1,
                'label': 'ROOT',
                'word': {
                    'start': 5,
                    'text': 'is',
                    'lemma': 'be'
                },
                'right': False,
                'root': True
            },
            {
                'start': 2,
                'end': 3,
                'label': 'det',
                'word': {
                    'start': 8,
                    'text': 'a',
                    'lemma': 'a'
                },
                'right': False,
                'root': False
            },
            {
                'start': 3,
                'end': 1,
                'label': 'attr',
                'word': {
                    'start': 10,
                    'text': 'test',
                    'lemma': 'test'
                },
                'right': True,
                'root': False
            },
            {
                'start': 4,
                'end': 1,
                'label': 'punct',
                'word': {
                    'start': 14,
                    'text': '.',
                    'lemma': '.'
                },
                'right': True,
                'root': False
            }
        ]
    }


def test_pipeline_nothing():
    result = client.post(
        '/%s/pipeline' % LANG,
        json={'text': 'This is a test.'}
    )
    result_json = result.json()
    assert result_json == {}


def test_pipeline_all():
    result = client.post(
        '/%s/pipeline?pos=1&ner=1&dep=1&sent=1' % LANG,
        json={'text': 'This is a test.'}
    )
    result_json = result.json()
    assert result_json == {
        'pos_annotations': [
            {'annotation': 'DT', 'word': {'start': 0, 'text': 'This', 'lemma': 'this'}},
            {'annotation': 'VBZ', 'word': {'start': 5, 'text': 'is', 'lemma': 'be'}},
            {'annotation': 'DT', 'word': {'start': 8, 'text': 'a', 'lemma': 'a'}},
            {'annotation': 'NN', 'word': {'start': 10, 'text': 'test', 'lemma': 'test'}},
            {'annotation': '.', 'word': {'start': 14, 'text': '.', 'lemma': '.'}}
        ],
        'entities': [],
        'sentences': [
            'This is a test.'
        ],
        'dep_parses': [
            {
                'start': 0,
                'end': 1,
                'label': 'nsubj',
                'word': {
                    'start': 0,
                    'text': 'This',
                    'lemma': 'this'
                },
                'right': False,
                'root': False
            },
            {
                'start': 1,
                'end': 1,
                'label': 'ROOT',
                'word': {
                    'start': 5,
                    'text': 'is',
                    'lemma': 'be'
                },
                'right': False,
                'root': True
            },
            {
                'start': 2,
                'end': 3,
                'label': 'det',
                'word': {
                    'start': 8,
                    'text': 'a',
                    'lemma': 'a'
                },
                'right': False,
                'root': False
            },
            {
                'start': 3,
                'end': 1,
                'label': 'attr',
                'word': {
                    'start': 10,
                    'text': 'test',
                    'lemma': 'test'
                },
                'right': True,
                'root': False
            },
            {
                'start': 4,
                'end': 1,
                'label': 'punct',
                'word': {
                    'start': 14,
                    'text': '.',
                    'lemma': '.'
                },
                'right': True,
                'root': False
            }
        ]
    }


@pytest.mark.parametrize('endpoint', [
    '/%s/pos-annotations',
    '/%s/named-entities',
    '/%s/dependency-parses',
    '/%s/sentences',
    '/%s/pipeline',
])
def test_model_not_found_exception_handling(endpoint):
    result = client.post(
        '/%s/dependency-parses' % LANG_ERR,
        json={'text': 'This is a test.'}
    )
    assert 'The pretrained statistical model "%s" is not available.' % LANG_ERR == result.json()['message']

