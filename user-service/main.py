from fastapi import FastAPI

app = FastAPI()

fake_users = [
    {"id": 1, "name": "Ivan"},
    {"id": 2, "name": "Maria"}
]

@app.get("/users")
def get_users():
    return fake_users
