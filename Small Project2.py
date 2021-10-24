from fastapi import FastAPI, HTTPException, status, Path, Query

from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
class Updateitem(BaseModel):
    name: Optional[str] = None
    price: Optional[float]=None
    brand: Optional[str] = None

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item that you would like to view", gt=0)):
    return inventory[item_id]
@app.get("/get-by-name")
def get_item(name: str = Query(None, title="name" , description="Name of item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        raise HTTPException(status_code=404, detail="item does not exist.")
@app.post("/create-item/{item_id}")
def create_item(item_id: int,item: item):
    if item_id in inventory:
        return{"Err": "Item Id already exists"}
    inventory[item_id] = item
    return inventory[item_id]
@app.put("/update-item/{item_id}")
def update_item (item_id:int, item:Updateitem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item does not exist.")
    if item.name != None:
        inventory[item_id].name= item.name
    if item.price != None:
        inventory[item_id].price= item.price
    if item.brand != None:
        inventory[item_id].brand= item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int = Query(..., description= "The item of the ID to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="item does not exist.")
    del inventory[item_id]
    return {"item deleted"}
