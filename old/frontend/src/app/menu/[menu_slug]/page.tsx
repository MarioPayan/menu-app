import AppBar from '@/components/appBar'
import {fetchMenuSlugs, fetchMenuBySlug} from '@/api/api'
import MenuNotFound from './not-found'
import DishCard from '@/components/dishCard'
import DishCategoryCard from '@/components/dishCategoryContainer'
import Box from '@mui/material/Box'

const Menu = async ({params}: {params: {menu_slug: string}}) => {
  const menu = await fetchMenuBySlug(params.menu_slug)

  if (!menu) {
    return <MenuNotFound />
  }

  const dishesFromCategory = (category: DishCategory): Dish[] =>
    menu.dishes.filter(dish => dish.categories.map(category => category.id).includes(category.id))

  const dishesByCategories = menu.dishCategories
    .map(category => ({
      ...category,
      dishes: dishesFromCategory(category),
    }))
    .filter(category => category.dishes.length >= 1)

  const ingredientsFromCategory = (category: IngredientCategory) =>
    menu.ingredients.filter(ingredient => ingredient.categories.map(category => category.id).includes(category.id))

  const ingredientsByCategories = menu.ingredientCategories
    .map(category => ({
      ...category,
      ingredients: ingredientsFromCategory(category),
    }))
    .filter(category => category.ingredients.length >= 1)

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        maxWidth: '100%',
      }}>
      <AppBar menu={menu} />

      {dishesByCategories.map(category => (
        <DishCategoryCard category={category} key={category.id}>
          <Box
            sx={{
              display: 'flex',
              flexDirection: 'row',
              flexWrap: 'wrap',
              justifyContent: 'center',
              gap: '1rem',
            }}>
            {menu.dishes.map(dish => (
              <DishCard dish={dish} key={dish.id} />
            ))}
          </Box>
        </DishCategoryCard>
      ))}
    </Box>
  )
}

export const generateStaticParams = async () => await fetchMenuSlugs()

export default Menu
