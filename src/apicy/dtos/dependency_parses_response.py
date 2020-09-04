from typing import List

from pydantic.main import BaseModel

from ..models.dependency_parse import DependencyParse


class DependencyParsesResponse(BaseModel):
    dep_parses: List[DependencyParse]
