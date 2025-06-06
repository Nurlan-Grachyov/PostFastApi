from typing import Annotated

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Base model for users with required fields 'name' and 'age'.
    Attributes: name (str): The user's full name (min length: 2 characters, max length: 25 characters).
    age (int): The user's age (must be between 5 and 111 years old)."""

    name: Annotated[
        str,
        Field(
            ...,
            title="Name of the user",
            description="The user's full name.",
            min_length=2,
            max_length=25,
        ),
    ]
    age: Annotated[
        int,
        Field(
            ...,
            title="Age of the user",
            description="The user's age in years.",
            ge=5,
            le=111,
        ),
    ]


class User(UserBase):
    """Full representation of a user including an auto-generated ID field.
    Attributes: id (int): Unique identifier for each user (auto-incremented integer)."""

    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    """Model used to create new users via API endpoints. Inherits all attributes from UserBase."""

    pass


class PostBase(BaseModel):
    """Base model for blog posts with required fields 'title', 'body', and 'author_id'.
    Attributes: title (str): Title of the blog post.
    body (str): Content or text of the blog post. author_id (int): Identifier of the user who created this post."""

    title: str
    body: str
    author_id: int


class PostResponse(PostBase):
    """Complete representation of a blog post including its unique ID and associated author details.
    Attributes: id (int): Unique identifier for each post (auto-incremented integer).
    author (User): Information about the user who authored this post."""

    id: int
    author: User

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    """Model used to create new blog posts via API endpoints. Inherits all attributes from PostBase."""

    pass
