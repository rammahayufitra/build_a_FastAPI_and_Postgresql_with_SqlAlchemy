from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional  

app = FastAPI() 

class Item(BaseModel):
    id:int 
    name:str 
    description:str 
    price:int 
    on_offer:bool


@app.get('/')
def index():
    return {"message":"hello world"}

@app.get('/greet/{name}')
def greet_name(name:str):
    return {"greeting":f"Hello {name}"}

@app.get('/greet')
def greet_optional_name(name:Optional[str]="user"):
    return {"message":f"Hello {name}"}

@app.put('/item')
def update_item(item:Item):
    return { 
            'id':item.id,
            'name': item.name,
            'description': item.description, 
            'price':item.price,
            'on_offer': item.on_offer
            }

https://www.youtube.com/watch?v=2g1ZjA6zHRo&list=PLEt8Tae2spYlDxuWQUqgpvXfVA4GiYsZb&index=5