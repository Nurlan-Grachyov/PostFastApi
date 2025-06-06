from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL
SQL_DB_URL = "sqlite:///./itproger.db"

# Initialize database engine
""" Initialize SQLAlchemy engine for SQLite database. 
Args: SQL_DB_URL (str): Connection string for SQLite database. Returns: Engine: SQLAlchemy engine instance. """
engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

# Configure session factory
""" Configure session factory for working with the database. 
Args: autoflush (bool): Whether to flush changes before queries. autocommit (bool): Whether to commit transactions immediately. 
bind (Engine): Bind session factory to the engine. Returns: sessionmaker: Factory for creating database sessions. """
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Declare base class for data models
""" Declare base class for defining SQLAlchemy models. Subclasses represent database tables. """
Base = declarative_base()
