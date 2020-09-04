from pydantic.main import BaseModel


class ModelResponse(BaseModel):
    language: str
    spacy_identifier: str

    def __init__(self, language, spacy_identifier=None):
        super().__init__()
        self.language = language
        if spacy_identifier is None:
            self.spacy_identifier = language
        else:
            self.spacy_identifier = spacy_identifier
