from ninja import Schema, Field
from typing import Optional, List, Any
from apps.customer import models


class Filters(Schema):
    email: str = None
    first_name: str = None
    last_name: str = None
    is_active: bool = None


class PhoneSchema(Schema):
    number: int


class AddressSchema(Schema):
    address: str


class UserSchema(Schema):
    id: int
    email: str
    first_name: str
    last_name: str
    birth: Optional[Any] = None
    is_active: bool
    is_staff: bool
    is_superuser: bool
    is_deleted: bool
    user_phone: List[PhoneSchema] = Field(..., alias="user_phone")
    user_address: List[AddressSchema] = Field(..., alias="user_address")


class Message(Schema):
    message: str
