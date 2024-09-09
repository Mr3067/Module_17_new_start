# from fastapi import APIRouter
#
# router = APIRouter(prefix='/user', tags=['user'])
#
# @router.get('/')
# async def all_users():
#     pass
#
# @router.get('/user_id')
# async def user_by_id():
#     pass
#
# @router.post('/create')
# async def create_user():
#     pass
#
# @router.put('/update')
# async def update_user():
#     pass
#
# @router.delete('/delete')
# async def delete_user():
#     pass


# ____________________________________________________________________________________________

from fastapi import APIRouter , Depends, status, HTTPException
# # # Сессия БД
from sqlalchemy.orm import Session
# # # Функция подключения к БД
from app.backend.db_depends import get_db
# # # Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
# # # Функции работы с записями.
from sqlalchemy import select, insert
# # # Функция создания slug-строки
from slugify import slugify



router = APIRouter(prefix='/user', tags=['user'])


# @router.get('/')
# async def all_users(db: Annotated[Session, Depends(get_db)]):
#     users = db.scalars(select(User)).all()
#     return users
#
# @router.get('/')
#
# async def all_users():
#     pass


# @router.get('/user_id')
# async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
#     # user = db.scalars(select(User).where(User.id == user_id))
#     # return user
#     pass
#
#
@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user1: CreateUser):
    db.execute(insert(User).values(username=create_user1.username,
                                   firstname=create_user1.firstname,
                                   lastname=create_user1.lastname,
                                   age=create_user1.age,
                                   slug=slugify(create_user1.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
    pass

#
# @router.put('/update')
# async def update_user(db: Annotated[Session, Depends(get_db)],user_id:int, ud_user: UpdateUser):
#     # change_user = db.scalars(select(User).where(User.id == user_id))
#     # if change_user is None:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_404_NOT_FOUND,
#     #         detail='User not found'
#     #     )
#     #
#     # db.execute(insert(User).values(firstname=ud_user.firstname,
#     #                                lastname=ud_user.lastname,
#     #                                age=ud_user.age))
#     # db.commit()
#     #
#     # return {
#     #     'status_code': status.HTTP_200_OK,
#     #     'transaction': f'User {user_id} update'
#     # }
#     pass
#
# @router.delete('/delete')
# async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
#     # change_user = db.scalars(select(User).where(User.id == user_id))
#     # if change_user is None:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_404_NOT_FOUND,
#     #         detail='User not found'
#     #     )
#     #
#     # db.execute(update(User).where(User.id == user_id))
#     # db.commit()
#     # return {
#     #     'status_code': status.HTTP_200_OK,
#     #     'transaction': f'User {user_id} delete'
#     # }
#     pass
