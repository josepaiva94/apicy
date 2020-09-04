from pydantic.main import BaseModel


class Word(BaseModel):
    start: int
    text: str
    lemma: str
