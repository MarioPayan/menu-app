from faker import Faker
import json
import random

fake = Faker()


def fake_image(type):
    image_sizes = {
        "icon": {"width": 100, "height": 100},
        "banner": {"width": 1000, "height": 500},
        "image": {"width": 500, "height": 500},
    }
    return fake.image_url(**image_sizes[type])


def rand_bool(probability=0.5):
    return random.random() < probability


def rand_int(min, max):
    return random.randint(min, max)


def sample(type, num):
    return random.sample(type, num)


def generate_api_object():
    return {
        "id": fake.uuid4(),
        "created_at": fake.iso8601(),
        "modified_at": fake.iso8601(),
    }


def generate_restaurant():
    return {
        "name": fake.company(),
        "slug": fake.slug(),
        "description": fake.text(),
        "banner": fake_image("banner"),
        "icon": fake_image("icon") if rand_bool(0.75) else None,
        **generate_api_object(),
    }


def generate_price():
    is_disccount = rand_bool(0.3)
    price = rand_int(1, 130) * 1000
    disccount = fake.random_int(0, 100) if is_disccount else 0
    return {
        "size": fake.word(),
        "finalPrice": price - (price * disccount / 100),
        "originalPrice": price,
        "currency": "COP",  # fake.currency_code(),
        "discountPercentage": disccount,
        **generate_api_object(),
    }


def generate_dish_category():
    return {
        "name": fake.word(),
        "image": fake_image("image") if rand_bool(0.75) else None,
        "description": fake.text(),
        "icon": fake_image("icon") if rand_bool(0.75) else None,
        "banner": fake_image("banner") if rand_bool(0.75) else None,
        "color": fake.color() if rand_bool(0.75) else None,
        **generate_api_object(),
    }


def generate_ingredient_category():
    return {
        "name": fake.word(),
        "image": fake_image("image") if rand_bool(0.75) else None,
        "description": fake.text(),
        "icon": fake_image("icon") if rand_bool(0.75) else None,
        "color": fake.color() if rand_bool(0.75) else None,
        **generate_api_object(),
    }


def generate_ingredient(categories):
    return {
        "name": fake.word(),
        "description": fake.text(),
        "categories": sample(categories, rand_int(1, 3)),
        "image": fake_image("image") if rand_bool(0.75) else None,
        **generate_api_object(),
    }


def generate_dish(categories, ingredients):
    return {
        "name": fake.word(),
        "prices": [generate_price() for _ in range(rand_int(1, 3))],
        "description": fake.text(),
        "categories": sample(categories, rand_int(1, 3)),
        "ingredients": sample(ingredients, rand_int(3, 5)),
        "mainImage": fake_image("image") if rand_bool(0.75) else None,
        "images": [fake_image("image") for _ in range(rand_int(0, 5))],
        "recommended": rand_bool(0.2),
        **generate_api_object(),
    }


def generate_combo(dishes):
    return {
        "name": fake.word(),
        "description": fake.text(),
        "image": fake_image("image") if rand_bool(0.75) else None,
        "dishes": sample(dishes, rand_int(2, 3)),
        "price": generate_price(),
        **generate_api_object(),
    }


def generate_order(dishes, restaurant):
    return {
        "dishes": sample(dishes, rand_int(1, 5)),
        "restaurant": restaurant,
        "price": fake.random_number(2),
        "status": random.choice(["pending", "completed", "canceled"]),
        "date": fake.iso8601(),
        **generate_api_object(),
    }


def generate_user():
    return {"name": fake.name(), "email": fake.email(), **generate_api_object()}


def generate_menu(restaurant, dishes, dish_categories, ingredients, ingredient_categories, combos):
    return {
        "slug": fake.slug(),
        "name": fake.word(),
        "restaurant": restaurant,
        "dishes": dishes,
        "dishCategories": dish_categories,
        "ingredients": ingredients,
        "ingredientCategories": ingredient_categories,
        "combos": combos,
        **generate_api_object(),
    }


ingredient_categories = [generate_ingredient_category() for _ in range(15)]
dish_categories = [generate_dish_category() for _ in range(7)]
ingredients = [generate_ingredient(ingredient_categories) for _ in range(30)]
dishes = [generate_dish(dish_categories, ingredients) for _ in range(18)]
combos = [generate_combo(dishes) for _ in range(4)]
restaurant = generate_restaurant()

menu = generate_menu(restaurant, dishes, dish_categories, ingredients, ingredient_categories, combos)

output_file_path = "../frontend/src/app/api/data.json"
with open(output_file_path, "w") as output_file:
    json.dump(menu, output_file, indent=2)

print(f"Generated data saved to {output_file_path}")