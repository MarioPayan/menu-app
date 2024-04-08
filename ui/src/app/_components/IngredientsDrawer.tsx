import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Drawer from './Drawer'
import Icon from './_subComponents/Icon'
import Button from '@mui/material/Button'
import IngredientsPreferences from '../_lib/IngredientsPreferences'

const IngredientsDrawer = ({
  ingredientCategories,
  setOpen,
  isOpen,
  ingredientsPreferences,
  setIngredientsPreferences,
}: {
  ingredientCategories?: any[]
  setOpen: any
  isOpen: boolean
  scrollToCategory: any
  ingredientsPreferences: IngredientsPreferences
  setIngredientsPreferences: any
}) => {
  if (!ingredientCategories?.length) {
    return null
  }

  const changeIngredientPreference = (ingredientId: any) =>
    setIngredientsPreferences(ingredientsPreferences.cyclePreference(ingredientId)),
    IngredientPreferenceState = ({ ingredientId }: { ingredientId: string }) => {
      if (ingredientsPreferences.isFavorite(ingredientId)) {
        return '✅'
      } else if (ingredientsPreferences.isExcluded(ingredientId)) {
        return '❌'
      }
      return ''
    }

  return (
    <Drawer
      side='right'
      isOpen={isOpen}
      setOpen={setOpen}>
      <Box
        display='flex'
        flexDirection='column'
        gap={2}>
        <Typography variant='h5'>Ingredients</Typography>
        <Box
          display='flex'
          flexDirection='column'
          gap={1}>
          {ingredientCategories.map((category: any) => (
            <Box
              display='flex'
              flexDirection='column'
              key={category.id}>
              <Button
                fullWidth
                variant='text'
                startIcon={category && <Icon obj={category} />}
                sx={{ justifyContent: 'flex-start' }}>
                {category.name}
              </Button>
              <Box
                display='flex'
                flexDirection='column'
                paddingLeft={3}>
                {category.ingredients.map((ingredient: any) => (
                  <Button
                    key={ingredient.id}
                    fullWidth
                    variant='text'
                    startIcon={ingredient && <Icon obj={ingredient} />}
                    endIcon={<IngredientPreferenceState ingredientId={ingredient.id} />}
                    onClick={() => {
                      changeIngredientPreference(ingredient.id)
                    }}
                    sx={{ justifyContent: 'flex-start' }}>
                    {ingredient.name}
                  </Button>
                ))}
              </Box>
            </Box>
          ))}
        </Box>
      </Box>
    </Drawer>
  )
}

export default IngredientsDrawer
