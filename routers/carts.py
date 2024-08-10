from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Cart  

router = APIRouter()

@router.get('/carts/')
def get_all_carts():

    cursor.execute("SELECT * FROM Cart;")
    rows = cursor.fetchall()
    return rows

@router.post('/carts/')
def create_cart(cart:Cart):

    try:
        cursor.execute(
            f"""INSERT INTO Cart (cart_id, user_id, total_price, is_checked_out)
                 VALUES ({cart.cart_id}, {cart.user_id}, {cart.total_price}, {cart.is_checked_out});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/carts/{cart_id}')
def get_cart(cart_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Cart WHERE cart_id={cart_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/carts/{cart_id}')
def update_cart(cart_id:int, updated_cart:Cart):

    try:
        cursor.execute(
            f"""
                UPDATE Cart
                SET user_id={updated_cart.user_id},
                    total_price={updated_cart.total_price},
                    is_checked_out={updated_cart.is_checked_out}
                WHERE cart_id={cart_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/carts/{cart_id}')
def delete_cart(cart_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Cart WHERE cart_id={cart_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
