from bson import ObjectId
from fastapi import FastAPI, APIRouter, HTTPException
from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from configration.conf import collection, rec_collection
from main_app.schema import (all_task, individual_data, all_records,
                             individual_record)
from main_app.models import Item, ClockInRecord

app = FastAPI()
router = APIRouter()


@router.get("/items")
async def get_all_items():
    items = list(collection.find())
    if items:
        return all_task(items)
    raise HTTPException(status_code=404, detail="No items found")


@router.get("/")
async def get_item(id: str):
    item = collection.find_one({"_id": ObjectId(id)})
    if item:
        return individual_data(item)
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/")
async def post_item(new_task: Item):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"some error founded{e}")


@router.delete("/")
async def delete_item(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/{item_id}")
async def update_item(id: str, item: Item):
    try:
        collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(item)}
        )
        return {"status": "ok", "message": "Data have been updated"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"item not fount {e}")


@router.get("/item/filter")
async def filter_items(
    email: Optional[str] = None,
    expiry_date: Optional[datetime] = None,
    insert_date: Optional[datetime] = None,
    quantity: Optional[int] = None
):
    filters = {}
    if email:
        filters["email"] = email
    if expiry_date:
        filters["expiry_date"] = {"$gt": expiry_date.timestamp()}
    if insert_date:
        filters["insert_date"] = {"$gt": insert_date.timestamp()}
    if quantity is not None:
        filters["quantity"] = {"$gte": quantity}
    items = list(collection.find(filters))
    if not items:
        raise HTTPException(status_code=404,
                            detail="No items found with the given filters")

    return all_task(items)


@router.get("/item/aggregate")
async def aggregate_items():
    results = collection.aggregate([
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ])
    return [{"email": res["_id"], "count": res["count"]} for res in results]


@router.get("/rec")
async def get_all_records():
    records = list(rec_collection.find())
    if records:
        return all_records(records)
    raise HTTPException(status_code=404, detail="No items found")


@router.post("/rec")
async def post_records(new_rec: ClockInRecord):
    try:
        new_rec.insert_date = datetime.utcnow()
        resp = rec_collection.insert_one(dict(new_rec))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"some error founded{e}")


@router.get("/rec/{id}")
async def get_records(id: str):
    item = rec_collection.find_one({"_id": ObjectId(id)})
    if item:
        return individual_data(item)
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/rec/filter")
async def filter_records(
    email: Optional[str] = None,
    location: Optional[str] = None,
    insert_datetime: Optional[datetime] = None
):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": insert_datetime}
    records = list(rec_collection.find(query))
    if records:
        raise HTTPException(status_code=404,
                            detail="No items found with the given filters")

    return all_records(records)


@router.delete("/rec")
async def delete_records(id: str):
    result = rec_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/{rec_id}")
async def update_records(id: str, records: ClockInRecord):
    try:
        rec_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": dict(records)}
        )
        return {"status": "ok", "message": "Data have been updated"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"item not fount {e}")


app.include_router(router)
