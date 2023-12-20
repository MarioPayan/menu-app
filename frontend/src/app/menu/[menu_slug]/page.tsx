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
  const dishesByCategories = menu.dishCategories
    .map(category => ({
      ...category,
      dishes: menu.dishes.filter(dish => dish.categories.map(category => category.id).includes(category.id)),
    }))
    .filter(category => category.dishes.length > 0)
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
