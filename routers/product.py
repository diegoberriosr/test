from fastapi import APIRouter, Depends
from database import get_db
from schemas import Product
import models
from crud_helpers import get_all, get_by_id, delete_by_id

router = APIRouter()


@router.post('/products', tags=['products'])
def create_product(request: Product , db = Depends(get_db)):
    newproduct = models.Product(title=request.title, description=request.description, price=request.price)
    db.add(newproduct)
    db.commit()
    
    return {
        'id' : newproduct.id,
        'title' : newproduct.title,
        'description' : newproduct.description,
        'price' : newproduct.price
    } 

@router.get('/products', tags=['products'])
def get_all_products(db = Depends(get_db)):
    products = get_all(models.Product, db, 'products')

    return products

@router.get('/products/{product_id}/users', tags=['products'])
def get_product_users(product_id : int , db = Depends(get_db)):
    product = get_by_id(models.Product, db, product_id, 'product')

    return product.users

@router.delete('/products/{product_id}', tags=['products'])
def delete_product(product_id : int, db = Depends(get_db)):
    delete_by_id(models.Product, db, product_id)

@router.put('/products/{product_id}', tags=['products'])
def edit_product(product_id : int, request: Product, db = Depends(get_db)):
    product = get_by_id(models.Product, db, product_id, 'product')

    product.title = request.title
    product.description = request.description
    product.price = request.price

    db.commit()

    return {
        'id' : product.id,
        'title' : product.title,
        'description' : product.description,
        'price' : product.price
    }

