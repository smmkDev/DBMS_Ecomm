from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Coupon 

router = APIRouter()

@router.get('/coupons/')
def get_all_coupons():

    cursor.execute("SELECT * FROM Coupon;")
    rows = cursor.fetchall()
    return rows

@router.post('/coupons/')
def create_coupon(coupon:Coupon):

    try:
        cursor.execute(
            f"""INSERT INTO Coupon (coupon_code, discount, valid_till, copies, product_id)
                 VALUES ('{coupon.coupon_code}', {coupon.discount}, '{coupon.valid_till}', {coupon.copies}, {coupon.product_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/coupons/{coupon_id}')
def get_coupon(coupon_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Coupon WHERE coupon_id={coupon_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/coupons/{coupon_id}')
def update_coupon(coupon_id:int, updated_coupon:Coupon):

    try:
        cursor.execute(
            f"""
                UPDATE Coupon
                SET coupon_code='{updated_coupon.coupon_code}',
                    discount={updated_coupon.discount},
                    valid_till='{updated_coupon.valid_till}',
                    copies={updated_coupon.copies},
                    product_id={updated_coupon.product_id}
                WHERE coupon_id={coupon_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/coupons/{coupon_id}')
def delete_coupon(coupon_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Coupon WHERE coupon_id={coupon_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
