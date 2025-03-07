from fastapi import FastAPI, HTTPException
from google.cloud import firestore
from typing import List
from google.oauth2 import service_account
from pydantic import BaseModel
import uuid

class User(BaseModel):
    name: str
    email: str
    age: int

# Helper function
COLLECTION_NAME = "users"

# Load credentials
cred = service_account.Credentials.from_service_account_file("./fast-api-coding-challenge-16eac14f3407.json")

# Init firestore
client = firestore.Client(credentials=cred)

# Init Fast API
app = FastAPI(
    title="CRUD User Management API",
    description="API CRUD untuk mengelola data pengguna menggunakan FastAPI dan Firebase Firestore",
    version="1.0.0"
)

def get_user_ref(user_id: str):
    return client.collection(COLLECTION_NAME).document(user_id)

# Create user
@app.post("/users", response_model=dict, summary="Create User", description="Create new user data to firestore")
def create_user(user: User):
    user_id = str(uuid.uuid4())
    user_data = user.model_dump()
    get_user_ref(user_id).set(user_data)
    return {"id": user_id, **user_data}

# Get by id User
@app.get("/users/{user_id}", response_model=dict, summary="Get user by id", description="Get user data by id")
def get_user(user_id: str):
    doc = get_user_ref(user_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **doc.to_dict()}

# Get users
@app.get("/users", response_model=List[dict], summary="Get all users", description="Get all users")
def get_all_users():
    users = []
    docs = client.collection(COLLECTION_NAME).stream()
    for doc in docs:
        users.append({"id": doc.id, **doc.to_dict()})
    return users

# Update user
@app.put("/users/{user_id}", response_model=dict, summary="Update user", description="Update user data to firestore")
def update_user(user_id: str, user: User):
    doc = get_user_ref(user_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump()
    get_user_ref(user_id).update(user_data)
    return {"id": user_id, **user_data}

# Delete user
@app.delete("/users/{user_id}", response_model=dict, summary="Delete user", description="Detele user data by id to firestore")
def delete_user(user_id: str):
    doc = get_user_ref(user_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    get_user_ref(user_id).delete()
    return {"message": "user deleted successfully"}