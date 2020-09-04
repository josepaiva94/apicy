from pydantic.main import BaseModel


class AnalyzeTextRequest(BaseModel):
    text: str
