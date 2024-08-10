from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Shipment

router = APIRouter()

@router.get('/shipments/')
def get_all_shipments():
    
    cursor.execute("SELECT * FROM Shipment;")
    rows = cursor.fetchall()
    return rows

@router.post('/shipments/')
def create_shipment(shipment:Shipment):

    try:
        cursor.execute(
            f"""INSERT INTO Shipment (shipment_id, order_id, date, is_completed)
                 VALUES ({shipment.shipment_id}, {shipment.order_id}, '{shipment.date}', {shipment.is_completed});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/shipments/{shipment_id}')
def get_shipment(shipment_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Shipment WHERE shipment_id={shipment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/shipments/{shipment_id}')
def update_shipment(shipment_id:int, updated_shipment:Shipment):

    try:
        cursor.execute(
            f"""
                UPDATE Shipment
                SET order_id={updated_shipment.order_id},
                    date='{updated_shipment.date}',
                    is_completed={updated_shipment.is_completed}
                WHERE shipment_id={shipment_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/shipments/{shipment_id}')
def delete_shipment(shipment_id: int):
    
    try:
        cursor.execute(
            f"DELETE FROM Shipment WHERE shipment_id={shipment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
