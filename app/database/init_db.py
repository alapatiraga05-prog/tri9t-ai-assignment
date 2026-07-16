from app.database.database import engine
from app.database.base import Base

# Import models so SQLAlchemy knows about them
from app.models.document import Document
from app.models.node import Node


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database created successfully!")