from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Rating 

router = APIRouter()

@router.get('/ratings/')
def get_all_ratings():

    cursor.execute("SELECT * FROM Rating;")
    rows = cursor.fetchall()
    return rows

@router.post('/ratings/')
def create_rating(rating:Rating):

    try:
        cursor.execute(
            f"""INSERT INTO Rating (rating_id, product_id, user_id, rate)
                 VALUES ({rating.rating_id}, {rating.product_id}, {rating.user_id}, {rating.rate});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/ratings/{rating_id}')
def get_rating(rating_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Rating WHERE rating_id={rating_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/ratings/{rating_id}')
def update_rating(rating_id:int, updated_rating:Rating):

    try:
        cursor.execute(
            f"""
                UPDATE Rating
                SET product_id={updated_rating.product_id},
                    user_id={updated_rating.user_id},
                    rate={updated_rating.rate}
                WHERE rating_id={rating_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/ratings/{rating_id}')
def delete_rating(rating_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Rating WHERE rating_id={rating_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
