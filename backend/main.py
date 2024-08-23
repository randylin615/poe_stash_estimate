
### ninja api 
### https://poe.ninja/api/data/currencyoverview?league=Settlers&type=Currency
### https://poe.ninja/api/data/itemoverview?league=Settlers&type=KalguuranRune

import base64
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from typing import List, Annotated
import models, update
# 引入engine及database設定好的SessionLocal
from database import engine, SessionLocal
# 引入Session
from sqlalchemy.orm import Session
from sqlalchemy import inspect

app = FastAPI()
inspector = inspect(engine)
# 在資料庫中建立剛剛models中設定好的資料結構
models.Base.metadata.create_all(bind=engine)

# 每次操作get_db時，db使用SessionLocal中提供的資料與資料庫連線，產生db存儲，完事後關閉
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 一個db的dependency，可以看做是要操作的db，這裡的Depends對應get_db，get_db對應SessionLocal    
db_dependency = Annotated[Session, Depends(get_db)]
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main(db:db_dependency):
    message = "testt"
    return {"message": message}


@app.post('/user_inform/{user_id}/{stash}')
async def add_user_data(user_id:str, stash:int, db:db_dependency):
    existing_user = db.query(models.User).filter(models.User.name == user_id).first()
    if not existing_user:
        db_user = models.User(name = user_id)
        db.add(db_user)

    db_userdata = models.UserData(username = user_id, stash1 = stash)
    db.add(db_userdata)

    db.commit()
    return db_userdata

@app.get('/item/img/{item_name}')
async def get_item_img(item_name:str, db:db_dependency):
    item = db.query(models.Item).filter(models.Item.item_name == item_name).first()
    return Response(content=item.img, media_type="image/png") 

@app.get('/item/price/{item_name}')
async def get_item_price(item_name:str, db:db_dependency):
    item = db.query(models.Item).filter(models.Item.item_name == item_name).first()
    return {"price":max(item.price_buy, item.price_sell)}



@app.get('/update/all')
async def update_all(db:db_dependency):
    rune = update.get_rune()
    curr = update.get_curr()
    
    for i in rune:
        temp = db.query(models.Item).filter(models.Item.item_name == i[0]).first()
        temp.price_sell = i[1]
        temp.price_buy = i[1]
        db.commit()
        
    for i in curr:
        temp = db.query(models.Item).filter(models.Item.item_name == i[0]).first()
        if temp:
            temp.price_sell = i[1]
            temp.price_buy = i[2]
            db.commit()
    return ("Done!", i[0])