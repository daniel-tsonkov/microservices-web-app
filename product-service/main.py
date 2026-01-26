from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

@app.get("/products")
def get_products():
    return products
