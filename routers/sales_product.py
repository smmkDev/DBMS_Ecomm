from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import SalesProduct  

router = APIRouter()

@router.get('/salesproducts/')
def get_all_sales_products():
    
    cursor.execute("SELECT * FROM sales_product;")
    rows = cursor.fetchall()
    return rows

@router.post('/salesproducts/')
def create_sales_product(sales_product:SalesProduct):

    try:
        cursor.execute(
            f"""INSERT INTO sales_product (sales_id, product_id)
                 VALUES ({sales_product.sales_id}, {sales_product.product_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/salesproducts/{sales_id}')
def get_sales_product(sales_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Ssales_product WHERE sales_id={sales_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/salesproducts/{sales_id}')
def update_sales_product(sales_id:int, updated_sales_product:SalesProduct):

    try:
        cursor.execute(
            f"""
                UPDATE sales_product
                SET product_id={updated_sales_product.product_id}
                WHERE sales_id={sales_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/salesproducts/{sales_id}')
def delete_sales_product(sales_id:int):

    try:
        cursor.execute(
            f"DELETE FROM sales_product WHERE sales_id={sales_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
