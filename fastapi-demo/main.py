from typing import Annotated, Literal, Union
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


class ImageInfo(BaseModel):
    name: str
    description: str
    url: str
    tags: list[str]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# 获取图片列表
# /image/list?page=1&page_size=10
@app.get("/image/list")
def get_image_list(page: int = 1, page_size: int = 10):
    return {
        "page": page,
        "page_size": page_size,
        "list": ["image1", "image2", "image3"]
    }


@app.post("/image_info/create")
def create_image_info(image_info: ImageInfo):
    print(image_info.tags)
    return {"image_info": image_info}


@app.get("/items2/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        # results = {**results, "q2": q}
        # results = results | {"q2": q}

    return results


@app.get("/items3/")
async def read_items3(q: str = Query(max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        # results = {**results, "q2": q}
        # results = results | {"q2": q}

    return results


@app.get("/items4/{item_id}")
async def read_items33(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    # item_id: int = Path(title="类目ID"),
    # q: str | None = Query(alias="item-query", default=None),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items56/")
async def read_items56(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
