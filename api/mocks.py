from typing import List
from faker import Faker
from datetime import datetime, timedelta
from decimal import Decimal
from models import (
    Price,
    DishCategory,
    IngredientCategory,
    Ingredient,
    Dish,
    Restaurant,
    Combo,
    User,
    Order,
    Menu,
)
from random import randint, sample

fake = Faker()


def rangint(min: int, max: int) -> range:
    return range(randint(min, max))


def fake_words(min: int, max: int) -> str:
    return " ".join(fake.words(nb=randint(min, max)))


def generate_price() -> Price:
    return Price(
        size=fake_words(1, 3),
        final_price=Decimal(fake.random_number(digits=5)),
        original_price=Decimal(fake.random_number(digits=5)),
        currency=fake.random_element(elements=("USD", "EUR", "GBP")),  # TODO: check
        discount_percentage=fake.pydecimal(
            left_digits=2, right_digits=2, positive=True, min_value=0.01, max_value=100
        ),
    )


def generate_ingredient_category() -> IngredientCategory:
    return IngredientCategory(
        name=fake_words(1, 3),
        ingredients=[],
        image=fake.image_url(),
        description=fake.text(),
        icon=fake.image_url(width=32, height=32),
        color=fake.hex_color(),
    )


def generate_ingredient(categories: List[IngredientCategory]) -> Ingredient:
    selected_category_ids = sample([c.id for c in categories], randint(1, 3))

    ingredient = Ingredient(
        name=fake_words(1, 3),
        dishes=[],
        description=fake.text(),
        categories=selected_category_ids,
        icon=fake.image_url(width=32, height=32),
    )

    for category_id in selected_category_ids:
        category = next(c for c in categories if c.id == category_id)
        category.ingredients.append(ingredient.id)

    return ingredient


def generate_dish_category() -> DishCategory:
    return DishCategory(
        name=fake_words(1, 3),
        dishes=[],
        image=fake.image_url(),
        description=fake.text(),
        icon=fake.image_url(),
        banner=fake.image_url(),
        color=fake.hex_color(),
    )


def generate_dish(
    categories: List[IngredientCategory],
    ingredients: List[Ingredient],
    prices: List[Price],
) -> Dish:
    selected_category_ids = sample([c.id for c in categories], randint(1, 3))
    selected_ingredient_ids = sample([i.id for i in ingredients], randint(2, 5))
    selected_price_ids = sample([p.id for p in prices], randint(1, 3))

    dish = Dish(
        name=fake_words(1, 5),
        prices=selected_price_ids,
        description=fake.text(),
        categories=selected_category_ids,
        ingredients=selected_ingredient_ids,
        main_image=fake.image_url(),
        images=[fake.image_url() for _ in rangint(3, 7)],
        recommended=fake.boolean(),
    )

    for category_id in selected_category_ids:
        category = next(c for c in categories if c.id == category_id)
        category.dishes.append(dish.id)

    for ingredient_id in selected_ingredient_ids:
        category = next(i for i in ingredients if i.id == ingredient_id)
        category.dishes.append(dish.id)

    return dish


def generate_restaurant() -> Restaurant:
    return Restaurant(
        name=fake.company(),
        slug=fake.slug(),
        description=fake.text(),
        banner=fake.image_url(),
        icon=fake.image_url(),
    )


def generate_user() -> User:
    return User(
        name=fake.name(),
        email=fake.email(),
    )


def generate_order(dishes: List[Dish], restaurant: Restaurant, price: Price) -> Order:
    selected_dish_ids = sample([d.id for d in dishes], randint(1, 8))

    return Order(
        dishes=selected_dish_ids,
        restaurant=restaurant.id,
        price=price.id,
        status=fake.random_element(elements=("pending", "completed", "cancelled")),
        date=datetime.now() + timedelta(days=fake.random_int(min=-30, max=30)),
    )


def generate_combo(dishes: List[Dish], price: Price) -> Combo:
    selected_dish_ids = sample([d.id for d in dishes], randint(2, 3))

    return Combo(
        name=fake_words(2, 6),
        description=fake.text(),
        image=fake.image_url(),
        dishes=selected_dish_ids,
        price=price.id,
    )


def generate_menu(
    restaurant: Restaurant,
    dishes: List[Dish],
    dish_categories: List[DishCategory],
    ingredients: List[Ingredient],
    ingredient_categories: List[IngredientCategory],
    combos: List[Combo],
) -> Menu:
    selected_dish_ids = sample([d.id for d in dishes], randint(10, 30))
    selected_dish_category_ids = sample(
        [dc.id for dc in dish_categories], randint(5, 12)
    )
    selected_ingredient_ids = sample([i.id for i in ingredients], randint(10, 30))
    selected_ingredient_category_ids = sample(
        [ic.id for ic in ingredient_categories], randint(5, 15)
    )
    selected_combo_ids = sample([c.id for c in combos], randint(0, 3))

    return Menu(
        slug=fake.slug(),
        name=fake_words(1, 5),
        restaurant=restaurant.id,
        dishes=selected_dish_ids,
        dish_categories=selected_dish_category_ids,
        ingredients=selected_ingredient_ids,
        ingredient_categories=selected_ingredient_category_ids,
        combos=selected_combo_ids,
    )


def generate_mock_data() -> dict:
    prices = [generate_price() for _ in rangint(20, 30)]
    ingredient_categories = [generate_ingredient_category() for _ in rangint(15, 25)]
    ingredients = [generate_ingredient(ingredient_categories) for _ in rangint(30, 50)]
    dish_categories = [generate_dish_category() for _ in rangint(12, 22)]
    restaurants = [generate_restaurant() for _ in rangint(5, 10)]
    dishes = [
        generate_dish(dish_categories, ingredients, prices) for _ in rangint(30, 70)
    ]
    combos = [
        generate_combo(dishes, fake.random_element(prices)) for _ in rangint(5, 10)
    ]
    users = [generate_user() for _ in rangint(50, 100)]
    orders = [
        generate_order(
            dishes, fake.random_element(restaurants), fake.random_element(prices)
        )
        for _ in rangint(20, 40)
    ]
    menus = [
        generate_menu(
            fake.random_element(restaurants),
            dishes,
            dish_categories,
            ingredients,
            ingredient_categories,
            combos,
        )
        for _ in rangint(5, 10)
    ]

    return {
        "prices": prices,
        "ingredient_categories": ingredient_categories,
        "ingredients": ingredients,
        "dish_categories": dish_categories,
        "restaurants": restaurants,
        "dishes": dishes,
        "combos": combos,
        "users": users,
        "orders": orders,
        "menus": menus,
    }
