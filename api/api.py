import uvicorn
from typing import Optional
from fastapi import FastAPI

from disk import *
from ram import *
from gpu import *
from system import *

app = FastAPI()


@app.get("/")
def read_root():
    return {"当前登录:" : "system_jiagou.UserName"}


@app.get("/sys/{key}")
def read_item(key: str):
    sys_txt1 = {}
    sys_txt1 ["id"] = "1"
    sys_txt1 ["type"] = "system"
    sys_txt1 ["name"] = System(1).sys_CSName()
    sys_txt1 ["system"] = System(1).sys_Caption()
    sys_txt1 ["install_time"] = System(1).sys_InstallDate()
    sys_txt1 ["sys_ram"] = System(1).sys_ram()
    sys_txt1 ["Manufacturer"] = System(1).board_Manufacturer()
    textarr = []
    textarr.append(sys_txt1)
    return {"item_id": textarr}


uvicorn.run(app)


