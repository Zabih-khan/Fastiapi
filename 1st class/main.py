from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello world! I am practicing FastAPI"}


@app.post("/createpost")
def create_post(post: Post):
    print(post.dict())
    return {"data": post}
