from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

"""
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(default="fixedquery", max_length=3)):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    

@app.get("/items/")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
   
@app.get("/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items" : [{"item_id" : "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q" : q}
    return query_items
   

@app.get("/items/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q" : q}
    return query_items

@app.get("/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q" : q}
    return query_items

@app.get("/items/")
async def read_items(
        q: str | None = Query(default=None, title="Query String", 
        description="Query string for the items to search in the database that have a good match",
        alias="item-query",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    
"""

@app.get("/items/")
async def read_items(
    hidden_qeury: str | None = Query(default=None, include_in_schema=False)):
    if hidden_qeury:
        return{"hidden_qeury": hidden_qeury}
    else:
        return{"hidden_qeury": "Not found"}