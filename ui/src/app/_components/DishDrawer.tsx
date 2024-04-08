'use client'
import { useEffect, useState } from 'react'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Image from 'next/image'
import Typography from '@mui/material/Typography'
import Divider from '@mui/material/Divider'
import Drawer from './Drawer'
import DishIngredients from './_subComponents/DishIngredients'
import DishPrices from './_subComponents/DishPrices'

const defaultDishImage = '', // TODO: Add default dish image
  DishDrawer = ({ dish, ingredientsPreferences, onClosed }: { dish: any, ingredientsPreferences: any, onClosed: any }) => {
    const [isOpen, setOpen] = useState(false)

    useEffect(() => {
      setOpen(Boolean(dish))
    }, [dish])

    if (!dish) {
      return null
    }

    const DishImage = ({ dish }: any) => (
      <Box
        position='relative'
        minHeight='30vh'
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
      <Drawer
        side='bottom'
        isOpen={isOpen}
        setOpen={setOpen}
        onClosed={onClosed}
      >
        <Paper
          sx={{
            display: 'flex',
            flexDirection: 'column',
            minHeight: '60vh',
            maxHeight: '70vh',
            pb: 10,
            gap: 1,
            borderBottomLeftRadius: 0,
            borderBottomRightRadius: 0,
          }}>
          <DishImage dish={dish} />
          <Box
            pt={2}
            px={3}
            flexGrow={1}>
            <Typography variant='h3'>{dish.name}</Typography>
            <Typography variant='h6'>{dish.description}</Typography>
          </Box>
          {dish.ingredients.length > 0 && (<>
            <Divider />
            <Box padding={2}>
              <DishIngredients ingredients={dish.ingredients} ingredientsPreferences={ingredientsPreferences} />
            </Box></>)}
          <Divider />
          <Box px={2}>
            <DishPrices dish={dish} />
          </Box>
        </Paper>
      </Drawer>
    )
  }

export default DishDrawer
