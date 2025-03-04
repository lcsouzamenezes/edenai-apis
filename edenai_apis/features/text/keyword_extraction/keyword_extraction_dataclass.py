from typing import Optional, Sequence

from pydantic import BaseModel, Field, StrictStr, validator


class InfosKeywordExtractionDataClass(BaseModel):
    keyword: str
    importance: Optional[float]

    @validator('importance')
    def valid_importance(cls, value):
        if value:
            value = round(value, 2)
        return value


class KeywordExtractionDataClass(BaseModel):
    items: Sequence[InfosKeywordExtractionDataClass] = Field(default_factory=list)
