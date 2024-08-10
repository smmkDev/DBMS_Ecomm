from fastapi import APIRouter
from connection import cursor, conn, connector
from models import Sales

router = APIRouter()

@router.get('/sales/')
def get_all_sales():

    cursor.execute("SELECT * FROM Sales;")
    rows = cursor.fetchall()
    return rows

@router.post('/sales/')
def create_sales(sales: Sales):

    try:
        cursor.execute(
            f"""INSERT INTO Sales (sales_id, sale_amount, time_period)
                 VALUES ({sales.sales_id}, {sales.sale_amount}, '{sales.time_period}');
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/sales/{sales_id}')
def get_sales(sales_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Sales WHERE sales_id={sales_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/sales/{sales_id}')
def update_sales(sales_id:int, updated_sales:Sales):

    try:
        cursor.execute(
            f"""
                UPDATE Sales
                SET sale_amount={updated_sales.sale_amount},
                    time_period='{updated_sales.time_period}'
                WHERE sales_id={sales_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/sales/{sales_id}')
def delete_sales(sales_id:int):

    try:
        cursor.execute(
            f"DELETE FROM Sales WHERE sales_id={sales_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
