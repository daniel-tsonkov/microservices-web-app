from fastapi import FastAPI
import requests

app = FastAPI()

AUTH_URL = "http://auth:8000"
USER_URL = "http://user:8000"
PRODUCT_URL = "http://product:8000"

@app.post("/login")
def login(data: dict):
    return requests.post(f"{AUTH_URL}/login", json=data).json()

@app.get("/users")
def users():
    return requests.get(f"{USER_URL}/users").json()

@app.get("/products")
def products():
    return requests.get(f"{PRODUCT_URL}/products").json()
