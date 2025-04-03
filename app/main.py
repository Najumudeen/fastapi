from fastapi import FastAPI, Response, status, HTTPException # type: ignore
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange # Create random number for ID
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Optinal Schema if user not provided then will take the value True

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', 
            password='vlbjcas', cursor_factory=RealDictCursor
            )
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Coonecting to database failed")
        print("Error", error)
        time.sleep(2)

#    rating: Optional[int] = None
# request Get Method url: "/" Order does matter.



# POST is store in to memory

my_posts = [ 
            {"title": "title of post 1", "content": "content of post1", "id": 1},
            {"title": "favorite foods", "content": "I like Pizza", "id": 2}
           ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts) 
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
# Never use this method    cursor.execute(f"INSERT INTO posts (title, content, published) VALUES (post.title, post.content, post.published)")
    cursor.execute(
                    """ INSERT INTO posts (title, content, published) VALUES  (%s, %s, %s) RETURNING * """, 
                   (post.title, post.content, post.published)
                  )
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}

# input value format title str, content str

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
    
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s returning * """, (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    return {"data": updated_post}