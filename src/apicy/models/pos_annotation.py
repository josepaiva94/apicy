from pydantic.main import BaseModel

from .word import Word


class PosAnnotation(BaseModel):
    word: Word
    annotation: str
