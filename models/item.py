from sqlalchemy import Column, Integer, String, Text
from config.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    field_1 = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(Text)
    my_numeric_field = Column(Integer)
