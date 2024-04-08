from typing import List
from models import (
    Price,
    DishCategory,
    IngredientCategory,
    Ingredient,
    Dish,
    Restaurant,
    Combo,
    Menu,
    Badge,
)


class NewRestaurantMenu:
    restaurant: Restaurant
    menus: List[Menu] = []
    dishes: List[Dish] = []
    dish_categories: List[DishCategory] = []
    ingredients: List[Ingredient] = []
    ingredient_categories: List[IngredientCategory] = []
    combos: List[Combo] = []
    prices: List[Price] = []
    badges: List[Badge] = []

    def __init__(self):
        pass

    def get_data(self):
        return {
            "prices": self.prices,
            "ingredient_categories": self.ingredient_categories,
            "ingredients": self.ingredients,
            "dish_categories": self.dish_categories,
            "restaurants": [self.restaurant],
            "dishes": self.dishes,
            "combos": self.combos,
            "users": [],
            "orders": self.combos,
            "menus": self.menus,
        }

    def create_restaurant(
        self, name="", slug="", description="", banner=None, icon=None
    ) -> Restaurant:
        self.restaurant = Restaurant(
            name=name, slug=slug, description=description, banner=banner, icon=icon
        )
        return self.restaurant

    def create_price(
        self,
        size="",
        final_price=0,
        original_price=0,
        currency="COP",
        discount_percentage=0,
    ) -> Price:
        price = Price(
            size=size,
            final_price=final_price,
            original_price=original_price if original_price else final_price,
            currency=currency,
            discount_percentage=discount_percentage,
        )
        self.prices.append(price)
        return price

    def create_dish_category(
        self,
        name="",
        dishes=[],
        image=None,
        description="",
        icon=None,
        banner=None,
        color="",
    ) -> DishCategory:
        dish_category = DishCategory(
            name=name,
            dishes=dishes,
            image=image,
            description=description,
            icon=icon,
            banner=banner,
            color=color,
        )
        self.dish_categories.append(dish_category)
        return dish_category

    def create_ingredient_category(
        self, name="", ingredients=[], image="", description="", icon="", color=""
    ) -> IngredientCategory:
        ingredient_category = IngredientCategory(
            name=name,
            ingredients=ingredients,
            image=image,
            description=description,
            icon=icon,
            color=color,
        )
        self.ingredient_categories.append(ingredient_category)
        return ingredient_category

    def create_ingredient(
        self, name="", dishes=[], description="", categories=[], icon=""
    ) -> Ingredient:
        ingredient = Ingredient(
            name=name,
            dishes=dishes,
            description=description,
            categories=categories,
            icon=icon,
        )
        self.ingredients.append(ingredient)
        return ingredient

    def create_dish(
        self,
        name="",
        prices=[],
        description="",
        categories=[],
        ingredients=[],
        main_image=None,
        images=[],
        badges=[],
        recommended=False,
    ) -> Dish:
        dish = Dish(
            name=name,
            prices=prices,
            description=description,
            categories=[c.id for c in categories],
            ingredients=ingredients,
            main_image=main_image,
            images=images,
            badges=[badge.id for badge in badges],
            recommended=recommended,
        )
        self.dishes.append(dish)
        for category in categories:
            index = self.dish_categories.index(category)
            self.dish_categories[index].dishes.append(dish.id)
        return dish

    def create_badge(
        self,
        name="",
        icon=None,
        type="",
    ) -> Badge:
        badge = Badge(
            name=name,
            icon=icon,
            type=type,
        )
        self.badges.append(badge)
        return badge

    def create_menu(
        self,
        slug="",
        name="",
    ) -> Menu:
        menu = Menu(
            slug=slug,
            name=name,
            restaurant=self.restaurant.id,
            dishes=[dish.id for dish in self.dishes],
            dish_categories=[
                dish_category.id for dish_category in self.dish_categories
            ],
            ingredients=[ingredient.id for ingredient in self.ingredients],
            ingredient_categories=[
                ingredient_category.id
                for ingredient_category in self.ingredient_categories
            ],
            combos=[combo.id for combo in self.combos],
        )
        self.menus.append(menu)
        return menu
