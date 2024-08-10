from fastapi import APIRouter
from connection import (cursor, conn, connector)  
from models import Brand  

router = APIRouter()

@router.get('/brands/')
def get_brands():

    cursor.execute("SELECT * FROM Brand;")
    rows = cursor.fetchall()
    return rows

@router.post('/brands/')
def post_brand(brand:Brand):

    try:
        cursor.execute(
            f"INSERT INTO Brand (brand_id, name) VALUES ({brand.brand_id}, '{brand.name}');"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.put('/brands/{brand_id}')
def update_brand(brand_id:int, brand:Brand):

    try:
        cursor.execute(
            f"""
            UPDATE Brand
            SET name = '{brand.name}'
            WHERE brand_id = {brand_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/brands/{brand_id}')
def delete_brand(brand_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Brand WHERE brand_id = {brand_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

