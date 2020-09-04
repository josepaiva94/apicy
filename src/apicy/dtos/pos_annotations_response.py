from typing import List

from pydantic.main import BaseModel

from ..models.pos_annotation import PosAnnotation


class PosAnnotationsResponse(BaseModel):
    pos_annotations: List[PosAnnotation]
