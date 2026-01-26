from fastapi import FastAPI
import requests

app = FastAPI()

AUTH_URL = "http://auth"
USER_URL = "http://user"
PRODUCT_URL = "http://product"

@app.post("/login")
def login(data: dict):
    r = requests.post(f"{AUTH_URL}/login", json=data)
    return r.json()

@app.get("/users")
def users():
    r = requests.get(f"{USER_URL}/users")
    return r.json()

@app.get("/products")
def products():
    r = requests.get(f"{PRODUCT_URL}/products")
    return r.json()
