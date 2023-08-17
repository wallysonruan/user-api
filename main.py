from fastapi import FastAPI
from user.routers.userRoutes import router as user_router
from database.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user_router)
