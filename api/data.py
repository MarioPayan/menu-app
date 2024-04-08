from typing import List, T
import uuid
from mocks import generate_mock_data
from models import (
    ExpandedDish,
    ExpandedDishCategory,
    ExpandedIngredient,
    ExpandedIngredientCategory,
    ExpandedMenu,
    Restaurant,
    Menu,
    Dish,
    DishCategory,
    Ingredient,
    IngredientCategory,
    Combo,
    Price,
)
from platillos_voladores import platillos_voladores


class Data:
    restaurants: List[Restaurant] = []
    menus: List[Menu] = []
    dishes: List[Dish] = []
    dish_categories: List[DishCategory] = []
    ingredients: List[Ingredient] = []
    ingredient_categories: List[IngredientCategory] = []
    combos: List[Combo] = []
    prices: List[Price] = []

    def __init__(self):
        mock_data = generate_mock_data()
        pv_data = platillos_voladores.get_data()
        self.restaurants = mock_data["restaurants"] + pv_data["restaurants"]
        self.menus = mock_data["menus"] + pv_data["menus"]
        self.dishes = mock_data["dishes"] + pv_data["dishes"]
        self.dish_categories = mock_data["dish_categories"] + pv_data["dish_categories"]
        self.ingredients = mock_data["ingredients"] + pv_data["ingredients"]
        self.ingredient_categories = mock_data["ingredient_categories"] + pv_data["ingredient_categories"]
        self.combos = mock_data["combos"] + pv_data["combos"]
        self.prices = mock_data["prices"] + pv_data["prices"]

    def expand_dish(self, dish: Dish) -> ExpandedDish:
        dish_dict = dish.model_dump(exclude={"categories", "ingredients", "prices"})
        return ExpandedDish(
            **dish_dict,
            categories=self.get_dish_categories_by_ids(dish.categories),
            ingredients=[
                self.expand_ingredient(i)
                for i in self.get_ingredients_by_ids(dish.ingredients)
            ],
            prices=self.get_prices_by_ids(dish.prices),
        )

    def expand_dish_category(self, dish_category: DishCategory) -> ExpandedDishCategory:
        dish_category_dict = dish_category.model_dump(exclude={"dishes"})
        return ExpandedDishCategory(
            **dish_category_dict,
            dishes=[
                self.expand_dish(d)
                for d in self.get_dishes_by_ids(dish_category.dishes)
            ],
        )

    def expand_ingredient(self, ingredient: Ingredient) -> ExpandedIngredient:
        ingredient_dict = ingredient.model_dump(exclude={"categories"})
        return ExpandedIngredient(
            **ingredient_dict,
            categories=self.get_ingredient_categories_by_ids(ingredient.categories),
        )

    def expand_ingredient_category(
        self, ingredient_category: IngredientCategory
    ) -> ExpandedIngredientCategory:
        ingredient_category_dict = ingredient_category.model_dump(exclude={"ingredients"})
        return ExpandedIngredientCategory(
            **ingredient_category_dict,
            ingredients=[
                self.expand_ingredient(i)
                for i in self.get_ingredients_by_ids(ingredient_category.ingredients)
            ],
        )

    def expand_menu(self, menu: Menu) -> ExpandedMenu:
        menu_dict = menu.model_dump(
            exclude={
                "restaurant",
                "dishes",
                "dish_categories",
                "ingredients",
                "ingredient_categories",
                "combos",
            }
        )
        return ExpandedMenu(
            **menu_dict,
            restaurant=self.get_restaurant_by_id(menu.restaurant),
            dishes=[self.expand_dish(d) for d in self.get_dishes_by_ids(menu.dishes)],
            dish_categories=[
                self.expand_dish_category(d)
                for d in self.get_dish_categories_by_ids(menu.dish_categories)
            ],
            ingredients=[
                self.expand_ingredient(i)
                for i in self.get_ingredients_by_ids(menu.ingredients)
            ],
            ingredient_categories=[
                self.expand_ingredient_category(d)
                for d in self.get_ingredient_categories_by_ids(
                    menu.ingredient_categories
                )
            ],
            combos=self.get_combos_by_ids(menu.combos),
        )

    def set(self, data):
        pass

    def get(self, id: uuid.UUID, entities: List[T], key="id") -> T:
        return next((e for e in entities if getattr(e, key, None) == id), None)

    def get_list(self, ids: List[uuid.UUID], entities: List[T], key="id") -> List[T]:
        return [self.get(id, entities, key) for id in ids]  # TODO: Exclude None values

    def get_restaurants(self) -> List[Restaurant]:
        return self.restaurants

    # Restaurants

    def get_restaurant_by_id(self, id: uuid.UUID) -> Restaurant:
        return self.get(id, self.restaurants)

    def get_restaurant_by_slug(self, slug: str) -> Restaurant:
        return self.get(slug, self.restaurants, "slug")

    # Menus

    def get_menus(self) -> List[Menu]:
        return self.menus

    def get_menu_by_slug(self, slug: str) -> Menu:
        return self.get(slug, self.menus, "slug")

    def get_expanded_menu(self, menu: Menu) -> ExpandedMenu:
        return self.expand_menu(menu)

    # Dishes

    def get_dishes_by_ids(self, ids: List[uuid.UUID]) -> List[Dish]:
        return self.get_list(ids, self.dishes)

    def get_expanded_dish(self, dish: Dish) -> Dish:
        return dish

    def get_dishes(self) -> List[Dish]:
        return self.dishes

    # Dish Categories

    def get_dish_categories_by_ids(self, ids: List[uuid.UUID]) -> List[DishCategory]:
        return self.get_list(ids, self.dish_categories)

    # Ingredients

    def get_ingredients_by_ids(self, ids: List[uuid.UUID]) -> List[Ingredient]:
        return self.get_list(ids, self.ingredients)

    # Ingredient Categories

    def get_ingredient_categories_by_ids(
        self, ids: List[uuid.UUID]
    ) -> List[IngredientCategory]:
        return self.get_list(ids, self.ingredient_categories)

    # Combos

    def get_combos_by_ids(self, ids: List[uuid.UUID]) -> List[Combo]:
        return self.get_list(ids, self.combos)

    def get_prices_by_ids(self, ids: List[uuid.UUID]) -> List[Price]:
        return self.get_list(ids, self.prices)
