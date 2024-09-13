# -*- coding: utf-8 -*-
# /app/main.py
from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)
