from pydantic import BaseModel

class Product(BaseModel):

    product_id:int
    sub_category:int
    brand_id:int
    rating:int
    quantity:int
    name:str
    price:float

class Address(BaseModel):

    address_id:int
    city:str
    country:str
    postal_code:str
    street:str

class Analytics(BaseModel):

    analytics_id:int
    store_id:int
    time_period:str

class AnalyticsSales(BaseModel):

    analytics_id:int
    sales_id:int

class Brand(BaseModel):

    brand_id:int
    name:str

class Cart(BaseModel):

    cart_id:int
    user_id:int
    total_price:float
    is_checked_out:bool

class CartProduct(BaseModel):

    cart_id:int
    product_id:int

class Category(BaseModel):

    category_id:int
    name:str

class Coupon(BaseModel):

    coupon_code:str
    discount:float
    valid_till:str
    copies:int
    product_id:int

class Feedback(BaseModel):

    feedback_id:int
    product_id:int
    user_id:int
    description:int

class OrderProduct(BaseModel):

    order_id:int
    product_id:int

class Orders(BaseModel):

    order_id:int
    user_id:int
    order_data:str
    price:float

class Payment(BaseModel):

    payment_id:int
    order_id:int
    price:float
    is_completed:bool

class Rating(BaseModel):

    rating_id:int
    product_id:int
    user_id:int
    rate:int

class Sales(BaseModel):

    sales_id:int
    sale_amount:float
    time_period:str

class SalesProduct(BaseModel):

    sales_id:int
    product_id:int

class Shipment(BaseModel):

    shipment_id:int
    order_id:int
    date:str
    is_completed:bool

class ShipmentAddress(BaseModel):

    shipment_id:int
    address_id:int

class Store(BaseModel):

    store_id:int
    vendor_id:int
    capacity:int

class SubCategory(BaseModel):

    sub_category_id:int
    name:str
    category_id:int

class Users(BaseModel):

    user_id:int
    user_name:str
    password:str
    is_admin:bool
    is_verified:bool
    email:str

class Vendor(BaseModel):

    vendor_id:int
    name:str

class WishList(BaseModel):

    wishlist_id:int
    user_id:int

