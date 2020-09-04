from typing import List

from pydantic.main import BaseModel


class SchemaResponse(BaseModel):
    dep_types: List[str]
    ent_types: List[str]
    pos_types: List[str]
