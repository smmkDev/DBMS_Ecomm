from fastapi import FastAPI
import uvicorn
from routers import (address, analytics_sales, analytics, brand, cart_products, carts, 
                     category, coupons, feedback, order_product, orders, payment, product,
                     rating, sales_product, sales, shipment_address, shipment, store, 
                     sub_category, users, vendor, wishlist
                    )

app = FastAPI(title="Ecommerce Store", description="DBMS Project")
app.include_router(address.router)
app.include_router(analytics_sales.router)
app.include_router(analytics.router)
app.include_router(brand.router)
app.include_router(cart_products.router)
app.include_router(carts.router)
app.include_router(category.router)
app.include_router(coupons.router)
app.include_router(feedback.router)
app.include_router(order_product.router)
app.include_router(orders.router)
app.include_router(payment.router)
app.include_router(product.router)
app.include_router(rating.router)
app.include_router(sales_product.router)
app.include_router(sales.router)
app.include_router(shipment_address.router)
app.include_router(shipment.router)
app.include_router(store.router)
app.include_router(sub_category.router)
app.include_router(users.router)
app.include_router(vendor.router)
app.include_router(wishlist.router)

uvicorn.run(app, host="localhost", port=8000)