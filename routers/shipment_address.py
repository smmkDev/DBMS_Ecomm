from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import ShipmentAddress

router = APIRouter()

@router.get('/shipmentaddresses/')
def get_all_shipment_addresses():

    cursor.execute("SELECT * FROM shipment_address;")
    rows = cursor.fetchall()
    return rows

@router.post('/shipmentaddresses/')
def create_shipment_address(shipment_address:ShipmentAddress):

    try:
        cursor.execute(
            f"""INSERT INTO shipment_address (shipment_id, address_id)
                 VALUES ({shipment_address.shipment_id}, {shipment_address.address_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/shipmentaddresses/{shipment_id}')
def get_shipment_address(shipment_id:int):
    
    try:
        cursor.execute(
            f"SELECT * FROM shipment_address WHERE shipment_id={shipment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/shipmentaddresses/{shipment_id}')
def update_shipment_address(shipment_id:int, updated_shipment_address:ShipmentAddress):

    try:
        cursor.execute(
            f"""
                UPDATE shipment_address
                SET address_id={updated_shipment_address.address_id}
                WHERE shipment_id={shipment_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/shipmentaddresses/{shipment_id}')
def delete_shipment_address(shipment_id: int):

    try:
        cursor.execute(
            f"DELETE FROM shipment_address WHERE shipment_id={shipment_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
