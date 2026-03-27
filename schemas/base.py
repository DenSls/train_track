import datetime

from pydantic import BaseModel


class DBIdentification(BaseModel):
    id: int
    created_at: datetime