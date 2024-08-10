from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import Product

router = APIRouter()

@router.get('/products/')
def get_products(db_name:str):

    cursor.execute(
        f"SELECT * FROM {db_name}"
    )
    rows = cursor.fetchall()
    return rows

@router.post('/products/')
def post_product(product:Product):

    try:
        cursor.execute(
            f"""INSERT INTO Product VALUES({product.product_id}, 
                                         {product.sub_category},
                                         {product.brand_id}, 
                                         {product.rating}, 
                                         {product.quantity}, 
                                         {product.name}, 
                                         {product.price});"""
        )
    except connector.Error as error :
        return {"Error": error}
    conn.commit()
    return {"Response" : "Success"}

@router.get('/products/{product_id}')
def get_product(product_id:int):
    
    try:
        cursor.execute(
            f"SELECT * FROM Product WHERE product_id={product_id};"
        )
    except connector.Error as error:
        return {"Error":error}
    return {"Result" : cursor.fetchall()}


@router.put('/products/')
def put_product(product_id:int, product:Product):

    try:
        cursor.execute(
            f"""
                UPDATE Product
                SET 
                sub_category_id={product.sub_category},
                brand_id={product.brand_id},
                rating={product.rating},
                quantity={product.quantity},
                name='{product.name}',
                price={product.price}
                WHERE product_id={product_id};
            """
        )
    except connector.Error as error:
        return {"Error" : error}
    conn.commit()
    return {"Response" : "Success"}

@router.delete('/products/')
def delete_product(product_id:int):

    try:
        cursor.execute(
            f"DELETE FROM Product WHERE product_id={product_id};"
        )
    except connector.Error as error:
        return {"Error" : error}
    conn.commit()
    return {"Response" : "Success"}
