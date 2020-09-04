from typing import List

from pydantic.main import BaseModel


class ModelsResponse(BaseModel):
    models: List[str]
