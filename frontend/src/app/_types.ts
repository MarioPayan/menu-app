type ApiObject = {
  id: string
  created_at: string
  modified_at: string
}

type Restaurant = {
  name: string
  slug: string
  description: string
  banner: string
  icon?: string
} & ApiObject

type Dish = {
  name: string
  prices: Price[]
  description: string
  categories: DishCategory[]
  ingredients: Ingredient[]
  mainImage?: string
  images: string[]
  recommended: boolean
} & ApiObject

type DishCategory = {
  name: string
  image?: string
  description: string // TODO: Should this be optional?
  icon?: string
  banner?: string
  color?: string
} & ApiObject

type Price = {
  size: string
  finalPrice: number
  originalPrice: number
  currency: string
  discountPercentage: number
} & ApiObject

type Ingredient = {
  name: string
  description: string
  categories: IngredientCategory[]
  image?: string
} & ApiObject

type IngredientCategory = {
  name: string
  image?: string
  description: string
  icon?: string
  color?: string
} & ApiObject

type Combos = {
  name: string
  description: string
  image?: string
  dishes: Dish[]
  price: Price
} & ApiObject

type Order = {
  dishes: Dish[]
  restaurant: Restaurant
  price: number
  status: string
  date: string
} & ApiObject

type User = {
  name: string
  email: string
} & ApiObject

type Menu = {
  slug: string
  name: string
  restaurant: Restaurant
  dishes: Dish[]
  categories: DishCategory[]
  ingredients: Ingredient[]
  combos: Combos[]
} & ApiObject
