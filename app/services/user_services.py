# app/services/user_service.py

from app.models.user import UserModel
from app.schemas.user import UserUpdate
from google.cloud import firestore

db = firestore.AsyncClient()

async def get_user_by_email(email: str):
    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email)
    docs = [doc async for doc in query.stream()]
    if docs:
        return UserModel(**docs[0].to_dict())
    return None

async def create_user_in_db(user: UserModel):
    users_ref = db.collection('users')
    await users_ref.document(user.user_id).set(user.dict())

async def get_user_by_id(user_id: str):
    user_ref = db.collection('users').document(user_id)
    doc = await user_ref.get()
    if doc.exists:
        return UserModel(**doc.to_dict())
    return None

async def update_user(user_id: str, user_update: UserUpdate):
    user_ref = db.collection('users').document(user_id)
    updates = user_update.dict(exclude_unset=True)
    await user_ref.update(updates)
    updated_doc = await user_ref.get()
    return UserModel(**updated_doc.to_dict())
