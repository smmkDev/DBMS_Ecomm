from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import OrderProduct

router = APIRouter()

@router.get('/orderproducts/')
def get_all_order_products():

    cursor.execute("SELECT * FROM order_product;")
    rows = cursor.fetchall()
    return rows

@router.post('/orderproducts/')
def create_order_product(order_product:OrderProduct):

    try:
        cursor.execute(
            f"""INSERT INTO order_product (order_id, product_id)
                 VALUES ({order_product.order_id}, {order_product.product_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/orderproducts/{order_id}')
def get_order_product(order_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM order_product WHERE order_id={order_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/orderproducts/{order_id}')
def update_order_product(order_id:int, updated_order_product:OrderProduct):

    try:
        cursor.execute(
            f"""
                UPDATE order_product
                SET product_id={updated_order_product.product_id}
                WHERE order_id={order_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/orderproducts/{order_id}')
def delete_order_product(order_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM order_product WHERE order_id={order_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
