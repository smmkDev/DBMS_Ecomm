from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Store  

router = APIRouter()

@router.get('/stores/')
def get_all_stores():

    cursor.execute("SELECT * FROM Store;")
    rows = cursor.fetchall()
    return rows

@router.post('/stores/', status_code=201)
def create_store(store:Store):

    try:
        cursor.execute(
            f"""INSERT INTO Store (store_id, vendor_id, capacity)
                 VALUES ({store.store_id}, {store.vendor_id}, {store.capacity});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/stores/{store_id}')
def get_store(store_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Store WHERE store_id={store_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/stores/{store_id}')
def update_store(store_id:int, updated_store:Store):

    try:
        cursor.execute(
            f"""
                UPDATE Store
                SET vendor_id={updated_store.vendor_id},
                capacity={updated_store.capacity}
                WHERE store_id={store_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/stores/{store_id}')
def delete_store(store_id:int):
    try:
        cursor.execute(
            f"DELETE FROM Store WHERE store_id={store_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
