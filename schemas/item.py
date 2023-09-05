from pydantic import BaseModel

class ItemSchema(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int    