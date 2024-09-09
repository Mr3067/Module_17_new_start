from fastapi import FastAPI
from routers import task
from routers import users

app1 = FastAPI()


@app1.get("/")
async def main_get():
    return {"message": "Welcome to Taskmanager"}


app1.include_router(task.router)
app1.include_router(users.router)
