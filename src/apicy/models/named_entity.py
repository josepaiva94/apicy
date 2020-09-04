from pydantic.main import BaseModel


class NamedEntity(BaseModel):
    start: int
    end: int
    text: str
    kind: str

