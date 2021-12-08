from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):     
    title: str
    description: str = None


class ItemCreate(ItemBase):     
    pass


class Item(ItemBase):     
    id: int     
    owner_id: int      
 
    class Config:         
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Item] = []
    class Config:         
        orm_mode = True