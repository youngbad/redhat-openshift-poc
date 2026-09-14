from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    title: str
    completed: bool = False


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
