from typing import Optional
from fastapi import FastAPI
from mongo.handler import MongoHandler
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class MsgItem(BaseModel):
    msg: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/log")
def log_post(msg: MsgItem):
    mongo = MongoHandler()
    
    mongo.insert_item_one({"log": msg.msg, "when": datetime.now()})
    mongo.close()
        
    return {"result": True}

# @app.get("/log")
# def log_get():
#     mongo = MongoHandler()
    
#     mongo.close()
        
#     return {"result": True}