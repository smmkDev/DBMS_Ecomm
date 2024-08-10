from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Orders  

router = APIRouter()

@router.get('/orders/')
def get_all_orders():

    cursor.execute("SELECT * FROM Orders;")
    rows = cursor.fetchall()
    return rows

@router.post('/orders/')
def create_order(order:Orders):

    try:
        cursor.execute(
            f"""INSERT INTO Orders (order_id, user_id, order_data, price)
                 VALUES ({order.order_id}, {order.user_id}, '{order.order_data}', {order.price});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/orders/{order_id}')
def get_order(order_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Orders WHERE order_id={order_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/orders/{order_id}')
def update_order(order_id:int, updated_order:Orders):

    try:
        cursor.execute(
            f"""
                UPDATE Orders
                SET user_id={updated_order.user_id},
                    order_data='{updated_order.order_data}',
                    price={updated_order.price}
                WHERE order_id={order_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/orders/{order_id}')
def delete_order(order_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Orders WHERE order_id={order_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
