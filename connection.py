from fastapi import FastAPI
from pydantic import BaseModel
from mysql import connector


conn = connector.connect(
    host="localhost",
    port="3306",
    username="root",
    password="root123",
    database="DbProject"
)
cursor = conn.cursor(dictionary=True)


