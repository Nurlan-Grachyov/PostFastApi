from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, Base, session_local
from models import User, Post
from schemas import User as DBUser, UserCreate, PostResponse, PostCreate

app = FastAPI()

# Create tables based on defined models
Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency function that yields a database session. Ensures proper cleanup by closing the session after use."""
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/user", response_model=DBUser)
async def user_create(user: UserCreate, db: Session = Depends(get_db)) -> DBUser:
    """Creates a new user entry in the database.
    Parameters: user (UserCreate): Data for creating a new user.
    db (Session): Database session dependency injected automatically.
    Returns: DBUser: Representation of the newly created user."""
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/posts", response_model=PostResponse)
async def post_create(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    """Creates a new blog post in the database.
    Parameters: post (PostCreate): Data for creating a new blog post.
    db (Session): Database session dependency injected automatically.
    Raises: HTTPException: If no user exists with the given author_id.
    Returns: PostResponse: Representation of the newly created blog post."""
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    db_post = Post(title=post.title, body=post.body, author=db_user)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.get("/posts/", response_model=List[PostResponse])
async def list_posts(db: Session = Depends(get_db)) -> List[PostResponse]:
    """Retrieves all existing blog posts from the database.
    Parameters: db (Session): Database session dependency injected automatically.
    Returns: List[PostResponse]: A list containing representations of all blog posts."""
    return db.query(Post).all()
