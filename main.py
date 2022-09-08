from http.client import HTTPException
from pydoc import describe
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI() 

class Item(BaseModel):
    id:int 
    name:str 
    description:str 
    price:int 
    on_offer:bool

    class Config:
        orm_mode = True 

db = SessionLocal() 


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass 

@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")

    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass 

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    pass 

# @app.get('/')
# def index():
#     return {"message":"hello world"}

# @app.get('/greet/{name}')
# def greet_name(name:str):
#     return {"greeting":f"Hello {name}"}

# @app.get('/greet')
# def greet_optional_name(name:Optional[str]="user"):
#     return {"message":f"Hello {name}"}

# @app.put('/item')
# def update_item(item:Item):
#     return { 
#             'id':item.id,
#             'name': item.name,
#             'description': item.description, 
#             'price':item.price,
#             'on_offer': item.on_offer
#             }


