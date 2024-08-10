from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import AnalyticsSales

router = APIRouter()

@router.get('/analyticssales/')
def get_analytics_sales():

    cursor.execute(
        f"SELECT * FROM Analytics_sales;"
    )
    rows = cursor.fetchall()
    return rows

@router.post('/analyticssales/')
def post_analytics_sales(analytics_sales:AnalyticsSales):
    
    try:
        cursor.execute(
            f"""INSERT INTO Analytics_sales VALUES({analytics_sales.analytics_id}, 
                                         {analytics_sales.sales_id});"""
        )
    except connector.Error as error :
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/analyticssales/{analytics_id}')
def get_analytics_sale(analytics_id:int):
    
    try:
        cursor.execute(
            f"SELECT * FROM Analytics_sales WHERE analytics_id={analytics_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}


@router.put('/analyticssales')
def put_analytics_sale(analytics_id:int, analytics_sales:AnalyticsSales):

    try:
        cursor.execute(
            f"""
                UPDATE Analytics_sales
                SET 
                analytics_id={analytics_sales.analytics_id},
                sales_id={analytics_sales.sales_id}
                WHERE analytics_id={analytics_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/analyticssales')
def delete_analytics_sale(analytics_id:int):

    try:
        cursor.execute(
            f"DELETE FROM Analytics_sales WHERE analytics_id={analytics_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
