from typing import List

from pydantic.main import BaseModel

from ..models.named_entity import NamedEntity


class NamedEntitiesResponse(BaseModel):
    entities: List[NamedEntity]
