from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Vendor

router = APIRouter()

@router.get('/vendors/')
def get_all_vendors():

    cursor.execute("SELECT * FROM Vendor;")
    rows = cursor.fetchall()
    return rows

@router.post('/vendors/')
def create_vendor(vendor: Vendor):

    try:
        cursor.execute(
            f"""INSERT INTO Vendor (vendor_id, name)
                 VALUES ({vendor.vendor_id}, '{vendor.name}');
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/vendors/{vendor_id}')
def get_vendor(vendor_id: int):

    try:
        cursor.execute(
            f"SELECT * FROM Vendor WHERE vendor_id={vendor_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/vendors/{vendor_id}')
def update_vendor(vendor_id: int, updated_vendor: Vendor):

    try:
        cursor.execute(
            f"""
                UPDATE Vendor
                SET name='{updated_vendor.name}'
                WHERE vendor_id={vendor_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/vendors/{vendor_id}')
def delete_vendor(vendor_id: int):

    try:
        cursor.execute(
            f"DELETE FROM Vendor WHERE vendor_id={vendor_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
