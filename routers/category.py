from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Category 

router = APIRouter()

@router.get('/categories/')
def get_all_categories():

    cursor.execute("SELECT * FROM Category;")
    rows = cursor.fetchall()
    return rows

@router.post('/categories/')
def create_category(category:Category):

    try:
        cursor.execute(
            f"""INSERT INTO Category (category_id, name)
                 VALUES ({category.category_id}, '{category.name}');
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/categories/{category_id}')
def get_category(category_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Category WHERE category_id={category_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/categories/{category_id}')
def update_category(category_id:int, updated_category:Category):

    try:
        cursor.execute(
            f"""
                UPDATE Category
                SET name='{updated_category.name}'
                WHERE category_id={category_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/categories/{category_id}')
def delete_category(category_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Category WHERE category_id={category_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
