import uvicorn
from fastapi import FastAPI
from gingerit.gingerit import GingerIt
from pydantic import BaseModel
from typing import Union
from fastapi.middleware.cors import CORSMiddleware


class Item(BaseModel):
    description: Union[str, None] = None


app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/text")
def correct_text(item: Item):
    text = item.description
    parser = GingerIt()
    text = parser.parse(text)
    result_text = text['result']

    return result_text


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5004, reload=True)
