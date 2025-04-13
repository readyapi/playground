from typing import Union
from readyapi import ReadyAPI
from readyapi_play import get_play_api_reference

app = ReadyAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/play", include_in_schema=False)
async def play_html():
    return get_play_api_reference(
        openapi_url=app.openapi_url,
        title=app.title + " - ReadyAPI",
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
