from typing import List
from uuid import UUID

import sqlalchemy
from fastapi import APIRouter

from database.database import database, DATABASE_URL
from user.models.User import table
from user.models.userDtos import UserDtoResponse, UserDtoRequest, UserRoleUpdateDtoRequest, UserRoleUpdateDtoResponse

router = APIRouter()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()
metadata.create_all(engine)

DEFAULT_URL = "/users/"


@router.post(DEFAULT_URL)
async def create_user(user: UserDtoRequest) -> UUID:
    query = table.insert(user.__dict__)
    last_id = await database.execute(query)
    return last_id


@router.get(DEFAULT_URL)
async def get_all_users() -> List[UserDtoResponse]:
    query = table.select()
    return await database.fetch_all(query)


@router.get("{}{}".format(DEFAULT_URL, "{user_id}"))
async def get_user_by_id(user_id: UUID) -> List[UserDtoResponse]:
    query = table.select().where(table.columns.id == user_id)
    return await database.fetch_all(query)


@router.delete("{}{}".format(DEFAULT_URL, "{user_id}"))
async def delete_user_by_id(user_id: UUID):
    query = table.delete().where(table.columns.id == user_id)
    await database.execute(query)


@router.patch(DEFAULT_URL)
async def update_user_role(user_role_update: UserRoleUpdateDtoRequest) -> List[UserRoleUpdateDtoResponse]:
    query = table.update().where(table.columns.id == user_role_update.id).values(role=user_role_update.role)
    await database.execute(query)
    query = table.select().where(table.columns.id == user_role_update.id)
    return await database.fetch_all(query)
