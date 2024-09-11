from fastapi import APIRouter, Depends, status, HTTPException
# # # Сессия БД
from sqlalchemy.orm import Session
# # # Функция подключения к БД
from backend.db_depends import get_db
from backend.db import SessionLocal
# # # # Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models.task import Task
from schemas import CreateTask, UpdateTask
# # # Функции работы с записями.
from sqlalchemy import select, insert, update, delete, func
# # # Функция создания slug-строки
from slugify import slugify
from random import randint

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).all()
    return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task1: CreateTask):
    db.execute(insert(Task).values(title=create_task1.title,
                                   content=create_task1.content,
                                   priority=create_task1.priority))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
@router.post('/create_5_tasks_for_test')
async def create_tasks_5(db: Annotated[Session, Depends(get_db)]):
    for i in range(5):
        number = db.scalars(select(func.max(Task.id))).one()
        if number == None:
            number = 0
        db.execute(insert(Task).values(title=f'Read book №{number+1}',
                                       content=f'Homework №{number+1}',
                                       priority=i))
        db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful. Five new tasks have been added for tests'
    }
@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, ud_task: UpdateTask):
    change_task = db.scalars(select(Task).where(Task.id == task_id))
    if change_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )

    db.execute(update(Task).where(Task.id == task_id).values(title=ud_task.title,
                                                             content=ud_task.content,
                                                             priority=ud_task.priority))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': f'Task {task_id} update'
    }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    change_task = db.scalars(select(Task).where(Task.id == task_id))
    if change_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found'
        )

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': f'Yask {task_id} delete'
    }

@router.delete('/delete_all_tasks')
async def delete_task_all(db: Annotated[Session, Depends(get_db)]):
    db.execute(delete(Task).where(Task.id != 0))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': f'All tasks have been deleted'
    }
