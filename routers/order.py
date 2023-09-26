from fastapi import APIRouter, Depends
from database import get_db
from schemas import Order
import models
from crud_helpers import get_all, get_by_id, delete_by_id

router = APIRouter()


@router.post('/order', tags=['order'])
def create_order(request: Order, db = Depends(get_db)):
    user = get_by_id(models.User, db, request.user_id, 'user')
    
    neworder = models.Order(user_id=user.id)
    db.add(neworder)

    for id in request.product_id:
        product = get_by_id(models.Product, db, id, 'product')
        neworder.products.append(product) # add product to order
        user.purchases.append(product) # add every ordered product to the 'purchases' table

    db.commit()

    return{
        'id' : neworder.id,
        'user_id' : neworder.user_id,
        'products': neworder.products
    }

@router.get('/order/{order_id}/products', tags=['order'])
def get_order_products(order_id : int, db = Depends(get_db)):
    order = get_by_id(models.Order, db, order_id, 'order')

    return order.products