from fastapi import FastAPI
from routers import task
from routers import users

app = FastAPI()


@app.get("/")
async def main_get():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(users.router)
