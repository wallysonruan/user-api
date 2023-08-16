from pydantic import BaseModel


class UserDtoRequest(BaseModel):
    first_name: str
    last_name: str
