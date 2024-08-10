from fastapi import APIRouter
from connection import cursor, conn, connector
from models import Payment

router = APIRouter()

@router.get('/payments/')
def get_all_payments():

    cursor.execute("SELECT * FROM Payment;")
    rows = cursor.fetchall()
    return rows

@router.post('/payments/')
def create_payment(payment:Payment):

    try:
        cursor.execute(
            f"""INSERT INTO Payment (payment_id, order_id, price, is_completed)
                 VALUES ({payment.payment_id}, {payment.order_id}, {payment.price}, {payment.is_completed});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/payments/{payment_id}')
def get_payment(payment_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Payment WHERE payment_id={payment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/payments/{payment_id}')
def update_payment(payment_id:int, updated_payment:Payment):

    try:
        cursor.execute(
            f"""
                UPDATE Payment
                SET order_id={updated_payment.order_id},
                    price={updated_payment.price},
                    is_completed={updated_payment.is_completed}
                WHERE payment_id={payment_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/payments/{payment_id}')
def delete_payment(payment_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Payment WHERE payment_id={payment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
