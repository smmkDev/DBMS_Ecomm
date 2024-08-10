from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Address

router = APIRouter()

@router.get('/address/')
def get_addresses():

    cursor.execute(
        f"SELECT * FROM Address;"
    )
    rows = cursor.fetchall()
    return rows

@router.post('/address/')
def post_address(address:Address):
    
    try:
        cursor.execute(
            f"""INSERT INTO Address VALUES({address.address_id}, 
                                         {address.city},
                                         {address.country}, 
                                         {address.postal_code}, 
                                         {address.street});"""
        )
    except connector.Error as error :
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/address/{address_id}')
def get_address(address_id:int):
    
    try:
        cursor.execute(
            f"SELECT * FROM Address WHERE address_id={address_id};"
        )
    except connector.Error as error:
        return {"Error":error}
    return {"Result": cursor.fetchall()}


@router.put('/address')
def put_address(address_id:int, address:Address):

    try:
        cursor.execute(
            f"""
                UPDATE Address
                SET 
                address_id={address.address_id},
                city={address.city},
                country={address.country},
                postal_code={address.postal_code},
                street={address.street}
                WHERE address_id={address_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/address/')
def delete_address(address_id:int):

    try:
        cursor.execute(
            f"DELETE FROM Address WHERE address_id={address_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
