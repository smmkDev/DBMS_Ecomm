from fastapi import APIRouter
from connection import (cursor, conn, connector)
from models import WishList

router = APIRouter()

@router.get('/wishlists/')
def get_all_wishlists():

    cursor.execute("SELECT * FROM WishList;")
    rows = cursor.fetchall()
    return rows

@router.post('/wishlists/')
def create_wishlist(wishlist:WishList):

    try:
        cursor.execute(
            f"""INSERT INTO WishList (wishlist_id, user_id)
                 VALUES ({wishlist.wishlist_id}, {wishlist.user_id});
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/wishlists/{wishlist_id}')
def get_wishlist(wishlist_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM WishList WHERE wishlist_id={wishlist_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

# Update an existing wishlist
@router.put('/wishlists/{wishlist_id}')
def update_wishlist(wishlist_id:int, updated_wishlist:WishList):

    try:
        cursor.execute(
            f"""
                UPDATE WishList
                SET user_id={updated_wishlist.user_id}
                WHERE wishlist_id={wishlist_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/wishlists/{wishlist_id}')
def delete_wishlist(wishlist_id:int):

    try:
        cursor.execute(
            f"DELETE FROM WishList WHERE wishlist_id={wishlist_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
