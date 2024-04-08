'use client'
import { useState, useEffect } from 'react'
import AppBar from '@/app/_components/AppBar'
import DishCard from '@/app/_components/DishCard'
import DishCategorySection from '@/app/_components/DishCategorySection'
import DishDrawer from '@/app/_components/DishDrawer'
import DishCategoriesDrawer from '../_components/DishCategoriesDrawer'
import IngredientsDrawer from '../_components/IngredientsDrawer'
import IngredientsPreferences from '../_lib/IngredientsPreferences'
import Box from '@mui/material/Box'
import { scrollToId } from '../_utils/utils'

const Menu = ({ menu }: { menu: any }) => {
  const [showedDish, setShowedDish] = useState(null)
  const [showedDishCategoriesDrawer, setShowedDishCategoriesDrawer] = useState(false)
  const [showedIngredientsDrawer, setShowedIngredientsDrawer] = useState(false)
  const [ingredientsPreferences, setIngredientsPreferences] = useState(new IngredientsPreferences())
  const scrollToCategory = (category: any) => scrollToId(`category-${category.id}`)
  const [isDrawerOpen, setIsDrawerOpen] = useState(false)

  useEffect(() => {
    setIsDrawerOpen(showedDishCategoriesDrawer || showedIngredientsDrawer || !!showedDish)
  }, [showedDishCategoriesDrawer, showedIngredientsDrawer, showedDish])

  return (
    <>
      <AppBar
        restaurant={menu.restaurant}
        toggleLeftDrawer={menu.dish_categories.length > 0 ? () => setShowedDishCategoriesDrawer(!showedDishCategoriesDrawer) : undefined}
        toggleRightDrawer={menu.ingredient_categories.length > 0 ? () => setShowedIngredientsDrawer(!showedIngredientsDrawer) : undefined}
        isDrawerOpen={isDrawerOpen}
      />
      <Box p={2}>
        {menu.dish_categories.map((dishCategory: any) => (
          <DishCategorySection
            category={dishCategory}
            key={dishCategory.id}>
            {dishCategory.dishes.map((dish: any) => (
              <DishCard
                dish={dish}
                key={dish.id}
                setShowedDish={setShowedDish}
                ingredientsPreferences={ingredientsPreferences}></DishCard>
            ))}
          </DishCategorySection>
        ))}
      </Box>
      <DishDrawer dish={showedDish} ingredientsPreferences={ingredientsPreferences} onClosed={() => setShowedDish(null)} />
      <DishCategoriesDrawer
        dishCategories={menu.dish_categories}
        isOpen={showedDishCategoriesDrawer}
        setOpen={setShowedDishCategoriesDrawer}
        scrollToCategory={scrollToCategory}
      />
      <IngredientsDrawer
        ingredientCategories={menu.ingredient_categories}
        isOpen={showedIngredientsDrawer}
        setOpen={setShowedIngredientsDrawer}
        scrollToCategory={scrollToCategory}
        ingredientsPreferences={ingredientsPreferences}
        setIngredientsPreferences={setIngredientsPreferences}
      />
    </>
  )
}

// Export const generateStaticParams = async () => await fetchMenuSlugs()

export default Menu
