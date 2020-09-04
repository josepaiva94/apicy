from typing import List, Optional

from pydantic.main import BaseModel

from ..models.dependency_parse import DependencyParse
from ..models.named_entity import NamedEntity
from ..models.pos_annotation import PosAnnotation


class PipelineResponse(BaseModel):
    pos_annotations: Optional[List[PosAnnotation]]
    dep_parses: Optional[List[DependencyParse]]
    sentences: Optional[List[str]]
    entities: Optional[List[NamedEntity]]
