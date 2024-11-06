from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


new_post = [
    {
        "title": "Faviorte Books",
        "content": "I love reading books",
        "id": 1,
    },
    {
        "title": "Faviorte Movies",
        "content": "I love watching movies",
        "id": 2,
    },
]


def find_post(id):
    for post in new_post:
        if post["id"] == id:
            return post


@app.get("/posts")
async def root():
    return {"data": new_post}


@app.post("/posts")
def create_post(post: Post):
    id = randrange(1, 100000)
    post_dict = post.dict()
    post_dict["id"] = id
    new_post.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post = new_post[len(new_post) - 1]
    print(post)
    return {"data": post}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(int(id))
    return {"data": post}
