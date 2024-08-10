from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Analytics

router = APIRouter()

@router.get('/analytics/')
def get_analytics():

    cursor.execute(
        f"SELECT * FROM Analytics;"
    )
    rows = cursor.fetchall()
    return rows

@router.post('/analytics/')
def post_analytics(analytics:Analytics):
    
    try:
        cursor.execute(
            f"""INSERT INTO Analytics VALUES({analytics.analytics_id}, 
                                         {analytics.store_id},
                                         {analytics.time_period});"""
        )
    except connector.Error as error :
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/analytics/{analytics_id}')
def get_analytic(analytics_id:int):
    
    try:
        cursor.execute(
            f"SELECT * FROM Analytics WHERE analytics_id={analytics_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}


@router.put('/analytics')
def put_analytics(analytics_id:int, analytics:Analytics):

    try:
        cursor.execute(
            f"""
                UPDATE Analytics
                SET 
                store_id={analytics.store_id},
                time_period={analytics.time_period}
                WHERE analytics_id={analytics_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/analytics/')
def delete_analytics(analytics_id:int):

    try:
        cursor.execute(
            f"DELETE FROM Analytics WHERE analytics_id={analytics_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
