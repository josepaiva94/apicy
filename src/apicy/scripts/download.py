import os

from spacy.cli import download


def download_models():
    models = os.getenv('MODELS', 'en').split()
    for model in models:
        download(model=model, direct=False)
    print('Done!')
