from fastapi import APIRouter, Depends
from database import get_db
from schemas import User
import models
from crud_helpers import get_all, get_by_id, delete_by_id

router = APIRouter()

@router.post('/users', tags=['users'])
def create_user(request: User ,db = Depends(get_db)):
    newuser = models.User(username = request.username, email=request.email)

    db.add(newuser)
    db.commit()

    return {
        'id' : newuser.id,
        'username' : newuser.username,
        'email' : newuser.email
    }

@router.get('/users', tags=['users'])
def get_all_users(db = Depends(get_db)):
    users = get_all(models.User, db, 'users')

    return users

@router.post('/users{user_id}/purchases/{product_id}', tags=['users'])
def create_purchase(user_id : int, product_id: int, db = Depends(get_db)):
    user = get_by_id(models.User, db, user_id, 'user')
    product = get_by_id(models.Product, db, product_id, 'product')

    user.purchases.append(product)
    db.commit()

    return user


@router.get('/users/{user_id}/purchases', tags=['users'])
def get_user_products(user_id : int, db = Depends(get_db)):
    user = get_by_id(models.User, db, user_id, 'user')

    return user.purchases


