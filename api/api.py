import uvicorn
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"当前登录:" : "system_jiagou.UserName"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

uvicorn.run(app)