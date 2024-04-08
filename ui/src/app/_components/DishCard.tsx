import Paper from '@mui/material/Paper'
import Image from 'next/image'
import Box from '@mui/material/Box'
import Divider from '@mui/material/Divider'
import Typography from '@mui/material/Typography'
import Grid from '@mui/material/Unstable_Grid2'
import ButtonBase from '@mui/material/ButtonBase'
import IngredientsPreferences from '../_lib/IngredientsPreferences'
import DishIngredients from './_subComponents/DishIngredients'
import DishPrices from './_subComponents/DishPrices'

const defaultDishImage = '', // TODO: Add default dish image
  DishCard = ({
    dish,
    setShowedDish,
    ingredientsPreferences,
  }: {
    dish: any
    setShowedDish: any
    ingredientsPreferences: IngredientsPreferences
  }) => {

    const DishImage = ({ dish }: any) => (
      <Box
        position='relative'
        height='150px'
        maxHeight='150px'
        minHeight='150px'
        overflow='hidden'
        borderRadius='3px 3px 0 0'
        sx={{ background: 'rgba(0,0,0,0.1)' }}>
        <Image
          src={dish.main_image || defaultDishImage}
          alt={dish.name}
          fill={true}
          style={{
            filter: 'blur(13px)  brightness(0.7)',
          }}
        />
        <Image
          src={dish.main_image || defaultDishImage}
          alt={dish.name}
          fill={true}
          style={{
            objectFit: 'contain',
          }}
        />
      </Box>
    )


    return (
      <Grid
        xs={12}
        sm={6}
        md={4}
        lg={3}
        display='flex'
        justifyContent='center'>
        <ButtonBase
          sx={{ width: '100%', textAlign: 'left' }}
          onClick={() => setShowedDish(dish)}>
          <Paper
            sx={{
              display: 'flex',
              flexDirection: 'column',
              minWidth: 200,
              maxWidth: 400,
              flexGrow: 1,
              height: '100%',
              pb: 1,
              gap: 1,
            }}>
            <DishImage dish={dish} />
            <Box
              px={2}
              flexGrow={1}>
              <Typography variant='h4'>{dish.name}</Typography>
              <Typography
                overflow='hidden'
                textOverflow='ellipsis'
                display='-webkit-box'
                textAlign='start'
                sx={{
                  WebkitLineClamp: 2,
                  WebkitBoxOrient: 'vertical',
                }}>
                {dish.description}
              </Typography>
            </Box>
            {dish.ingredients.length > 0 && (<>
              <Divider />
              <Box px={2} display="flex" justifyContent="flex-end">
                <DishIngredients
                  ingredients={dish.ingredients}
                  ingredientsPreferences={ingredientsPreferences} />
              </Box></>)}
            <Divider />
            <Box px={2}>
              <DishPrices dish={dish} />
            </Box>
          </Paper>
        </ButtonBase>
      </Grid>
    )
  }

export default DishCard
