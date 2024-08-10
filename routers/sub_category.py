from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import SubCategory

router = APIRouter()

@router.get('/subcategories/')
def get_all_subcategories():

    cursor.execute("SELECT * FROM SubCategory;")
    rows = cursor.fetchall()
    return rows

@router.post('/subcategories/')
def create_subcategory(subcategory:SubCategory):

    try:
        cursor.execute(
            f"""INSERT INTO sub_category (sub_category_id, name, category_id)
                 VALUES ({subcategory.sub_category_id}, '{subcategory.name}', {subcategory.category_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/subcategories/{sub_category_id}')
def get_subcategory(sub_category_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM sub_category WHERE sub_category_id={sub_category_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/subcategories/{sub_category_id}')
def update_subcategory(sub_category_id:int, updated_subcategory:SubCategory):

    try:
        cursor.execute(
            f"""
                UPDATE sub_category
                SET name='{updated_subcategory.name}',
                    category_id={updated_subcategory.category_id}
                WHERE sub_category_id={sub_category_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/subcategories/{sub_category_id}')
def delete_subcategory(sub_category_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM sub_category WHERE sub_category_id={sub_category_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
