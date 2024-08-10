from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import CartProduct 

router = APIRouter()

@router.get('/cartproducts/')
def get_all_cart_products():

    cursor.execute("SELECT * FROM cart_product;")
    rows = cursor.fetchall()
    return rows

@router.post('/cartproducts/')
def create_cart_product(cart_product:CartProduct):

    try:
        cursor.execute(
            f"""INSERT INTO cart_product (cart_id, product_id)
                 VALUES ({cart_product.cart_id}, {cart_product.product_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/cartproducts/{cart_id}')
def get_cart_product(cart_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM cart_product WHERE cart_id={cart_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/cartproducts/{cart_id}')
def update_cart_product(cart_id:int, updated_cart_product:CartProduct):

    try:
        cursor.execute(
            f"""
                UPDATE cart_product
                SET product_id={updated_cart_product.product_id}
                WHERE cart_id={cart_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/cartproducts/{cart_id}')
def delete_cart_product(cart_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM cart_product WHERE cart_id={cart_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
