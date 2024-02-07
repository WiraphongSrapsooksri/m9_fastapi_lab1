from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

class user(BaseModel):
    cid: str
    username: str
    password: str
    status: str
    img1: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Service API M9"}    

# @app.get("/users")
# async def read_users():
#     with open("../assets/users.json", "r") as f:
#         user = json.load(f)
#         return user

@app.get("/users")
async def read_users():
    with open("/work/assets/users.json", "r") as f:
        users = json.load(f)
        return users

