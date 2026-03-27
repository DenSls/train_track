from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ExerciseBaseSchema(BaseModel):
    name: str
    description: str
    category: str
    muscle_group: str


class ExercisesSchema(BaseModel):  # maybe BaseShema
    ...
    limit: Optional[int] = Field(default=20)
    offset: Optional[int] = Field(default=0)

    model_config = ConfigDict(
        extra='forbid',
        str_strip_whitespace=False
    )
