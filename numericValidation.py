from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

"""
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The Id of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
    ):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
    


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
    

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results    
"""   

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000), 
    q: str,
    size: float = Query(gt=0, lt=10.5)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results    