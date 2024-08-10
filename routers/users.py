from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Users

router = APIRouter()

@router.get('/users/')
def get_all_users():

    cursor.execute("SELECT * FROM Users;")
    rows = cursor.fetchall()
    return rows

@router.post('/users/')
def create_user(user:Users):

    try:
        cursor.execute(
            f"""INSERT INTO Users (user_id, user_name, password, is_admin, is_verified, email)
                 VALUES ({user.user_id}, '{user.user_name}', '{user.password}', {user.is_admin}, {user.is_verified}, '{user.email}');
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/users/{user_id}')
def get_user(user_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Users WHERE user_id={user_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/users/{user_id}')
def update_user(user_id:int, updated_user:Users):

    try:
        cursor.execute(
            f"""
                UPDATE Users
                SET user_name='{updated_user.user_name}',
                    password='{updated_user.password}',
                    is_admin={updated_user.is_admin},
                    is_verified={updated_user.is_verified},
                    email='{updated_user.email}'
                WHERE user_id={user_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/users/{user_id}')
def delete_user(user_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Users WHERE user_id={user_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
