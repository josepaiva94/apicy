from typing import List

from pydantic.main import BaseModel


class SentencesResponse(BaseModel):
    sentences: List[str]
