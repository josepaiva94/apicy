from pydantic.main import BaseModel

from .word import Word


class DependencyParse(BaseModel):
    start: int
    end: int
    label: str
    word: Word
    right: bool
    root: bool

