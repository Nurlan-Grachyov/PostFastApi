from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    """Database model representing a single user."""

    __tablename__ = "users"

    #: Primary key column, auto-incremented integer.
    id = Column(Integer, index=True, primary_key=True)

    #: Username or full name of the user.
    name = Column(String, index=True)

    #: Age of the user.
    age = Column(Integer)


class Post(Base):
    """Database model representing a blog post."""

    __tablename__ = "posts"

    #: Primary key column, auto-incremented integer.
    id = Column(Integer, index=True, primary_key=True)

    #: Title of the blog post.
    title = Column(String, index=True)

    #: Main content or body of the blog post.
    body = Column(String)

    #: Foreign key linking to the author's user record.
    author_id = Column(Integer, ForeignKey("users.id"))

    #: Relationship back-reference to the corresponding User object.
    author = relationship("User")
