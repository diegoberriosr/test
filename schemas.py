from pydantic import BaseModel
from typing import List
class User(BaseModel):
    username : str
    email : str


class Product(BaseModel):
    title : str
    description : str
    price : float

class Order(BaseModel):
    user_id : int
    product_id : List[int]