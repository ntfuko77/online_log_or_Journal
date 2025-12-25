from pydantic import BaseModel,Field

class tag(BaseModel):
    tag_id: int
    tag_name: str
    category_name: str
class category(BaseModel):
    category_id: int
    category_name: str
class entity(BaseModel):
    entity_id: int
    entity_name: str
    description: str
    author_id: int
    category_id: int
    tags: list[tag]
class author(BaseModel):
    author_id: int
    author_name: str