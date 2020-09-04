import os
from typing import Dict

import spacy
from spacy.symbols import ORTH

from ..exceptions.model_not_found_exception import ModelNotFoundException


class Model(object):

    def __init__(self, spacy_model):
        self.spacy_model = spacy_model

    def get_dep_types(self):
        """List the available dep labels in the model."""
        return self.spacy_model.parser.labels

    def get_ent_types(self):
        """List the available entity types in the model."""
        return self.spacy_model.entity.labels

    def get_pos_types(self):
        """List the available part-of-speech tags in the model."""
        return self.spacy_model.tagger.labels


class ModelManager(object):
    models: Dict[str, Model] = {}

    def get_or_load_model(self, spacy_identifier: str, language: str = None):
        """Get spacy model."""
        if language is None:
            language = spacy_identifier.split('_', 1)[0]
        if language.lower() not in self.models:
            self.models[language.lower()] = Model(spacy_model=spacy.load(spacy_identifier))
            self.load_special_cases_if_available(language)
        if language.lower() not in self.models:
            raise ModelNotFoundException(language.lower())
        return self.models[language.lower()]

    def get_language_model(self, language: str):
        if language.lower() not in self.models:
            raise ModelNotFoundException(language.lower())
        return self.models[language.lower()]

    def load_special_cases_if_available(self, language):
        special_cases_str = os.getenv(f"{language.upper()}_SPECIAL_CASES", "")
        if special_cases_str:
            model = self.models[language.lower()]
            for special_case in special_cases_str.split(','):
                model.spacy_model.tokenizer.add_special_case(
                    special_case,
                    [{ORTH: special_case}]
                )
