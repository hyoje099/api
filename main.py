from re import template
from typing import Union
from urllib import response

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "World1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/name/{name}/age/{age}", response_class=HTMLResponse)
def read_name(request: Request,name:str, age: int):
    ref= db.reference(f"/{name}")
    ref.set(f"{age}")
    return templates.TemplateResponse("index.html",{"request":request,"name":name,"age":age})

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("./testtest-79fe1-firebase-adminsdk-yqn8g-69708e0e80.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://testtest-79fe1-default-rtdb.firebaseio.com/'
})

@app.get("/view/{name}",response_class=HTMLResponse)
async def read_value(request:Request,name:str):
    ref=db.reference(f"/{name}")
    value=ref.get()
    print(value)
    return templates.TemplateResponse("index.html",{"request":request,"name":name,"age":value})