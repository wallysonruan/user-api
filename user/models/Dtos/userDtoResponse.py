from uuid import UUID

from pydantic import BaseModel


class UserDtoResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
