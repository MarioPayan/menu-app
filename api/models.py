from pydantic import BaseModel, Field, EmailStr, condecimal, HttpUrl
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from enum import Enum
import uuid


class CurrencyEnum(str, Enum):
    USD = "USD"
    COP = "COP"
    EUR = "EUR"
    GBP = "GBP"


class StatusEnum(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CustomBaseModel(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)


class Price(CustomBaseModel):
    size: str
    final_price: Decimal
    original_price: Decimal
    currency: CurrencyEnum
    discount_percentage: condecimal(max_digits=5, decimal_places=2) = Field(
        ge=0, le=100
    )


class Badge(CustomBaseModel):
    name: str
    icon: Optional[HttpUrl] = None
    type: Optional[str] = None


class IngredientCategory(CustomBaseModel):
    name: str
    ingredients: List[uuid.UUID] = []
    image: Optional[HttpUrl] = None
    description: str
    icon: Optional[HttpUrl] = None
    color: Optional[str] = None


class Ingredient(CustomBaseModel):
    name: str
    dishes: List[uuid.UUID] = []
    description: str
    categories: List[uuid.UUID] = []
    icon: Optional[HttpUrl] = None


class DishCategory(CustomBaseModel):
    name: str
    dishes: List[uuid.UUID] = []
    image: Optional[HttpUrl] = None
    description: str
    icon: Optional[HttpUrl] = None
    banner: Optional[HttpUrl] = None
    color: Optional[str] = None


class Dish(CustomBaseModel):
    name: str
    prices: List[uuid.UUID] = []
    description: str
    categories: List[uuid.UUID] = []
    ingredients: List[uuid.UUID] = []
    badges: List[uuid.UUID] = []
    main_image: Optional[HttpUrl] = None
    images: List[HttpUrl] = []
    recommended: bool


class Restaurant(CustomBaseModel):
    name: str
    slug: str
    description: str
    banner: Optional[HttpUrl] = None
    icon: Optional[HttpUrl] = None


class Combo(CustomBaseModel):
    name: str
    description: str
    image: Optional[HttpUrl] = None
    dishes: List[uuid.UUID] = []
    price: uuid.UUID


class Order(CustomBaseModel):
    dishes: List[uuid.UUID] = []
    restaurant: uuid.UUID
    price: uuid.UUID
    status: StatusEnum
    date: datetime = Field(default_factory=datetime.now)


class User(CustomBaseModel):
    name: str
    email: EmailStr


class Menu(CustomBaseModel):
    slug: str
    name: str
    restaurant: uuid.UUID
    dishes: List[uuid.UUID] = []
    dish_categories: List[uuid.UUID] = []
    ingredients: List[uuid.UUID] = []
    ingredient_categories: List[uuid.UUID] = []
    combos: List[uuid.UUID] = []


class ExpandedIngredient(Ingredient):
    categories: List[IngredientCategory] = []


class ExpandedDish(Dish):
    prices: List[Price] = []
    categories: List[DishCategory] = []
    ingredients: List[Ingredient] = []


class ExpandedDishCategory(DishCategory):
    dishes: List[ExpandedDish] = []


class ExpandedIngredientCategory(IngredientCategory):
    ingredients: List[ExpandedIngredient] = []


class ExpandedMenu(Menu):
    restaurant: Restaurant
    dishes: List[ExpandedDish] = []
    dish_categories: List[ExpandedDishCategory] = []
    ingredients: List[ExpandedIngredient] = []
    ingredient_categories: List[ExpandedIngredientCategory] = []
    combos: List[Combo] = []
