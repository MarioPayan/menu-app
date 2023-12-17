'use client' // TODO: Should be server

import Typography from '@mui/material/Typography'
import Box from '@mui/material/Box'
import Paper from '@mui/material/Paper'
import Image from 'next/image'
import {defaultDishImage} from '@/utils/assets'
import Modal from './modal'
import {useState} from 'react'
import {numberToMoney, numberToPercentage} from '../_utils/utils'
import styles from './dishCard.module.css'
import {ButtonBase} from '@mui/material'

const DishNotFound = async () => <div>Dish not found</div>

const Prices = ({prices}: {prices: Price[]}) => {
  const Price = ({price, showSize = false}: {price: Price; showSize?: boolean}) => {
    const priceSize = `${price.size}: `
    const originalPrice = numberToMoney(price.originalPrice, price.currency)
    const finalPrice = numberToMoney(price.finalPrice, price.currency)
    const discountPercentage = numberToPercentage(price.discountPercentage)
    return (
      <Box className={styles.prices}>
        {showSize && <Typography>{priceSize}</Typography>}
        <Typography fontWeight='bold'>{finalPrice}</Typography>
        {price.discountPercentage !== 0 && (
          <>
            <Typography className={styles.strikeText}>{originalPrice}</Typography>
            <Typography>{discountPercentage}</Typography>
          </>
        )}
      </Box>
    )
  }
  return (
    <>
      {prices.map(price => (
        <Price key={price.id} price={price} showSize={prices.length > 1} />
      ))}
    </>
  )
}

const MediumDishCard = ({dish}: {dish: Dish}) => (
  <Paper className={styles.mediumPaper}>
    <Box className={styles.mediumInfo}>
      <Typography variant='h6' fontWeight='bold'>
        {dish.name}
      </Typography>
      <Typography variant='body1' className={styles.ellipsisText}>
        {dish.description}
      </Typography>
      <Prices prices={dish.prices} />
    </Box>
    <Box className={styles.mediumImage}>
      <Image src={dish.mainImage || defaultDishImage} alt={dish.name} fill />
    </Box>
  </Paper>
)

const FullDishCard = ({dish}: {dish: Dish}) => 
// const ingredientsByCategory = dish.ingredients
//   .map(category => ({
//     ...category,
//     dishes: menu.dishes.filter(dish => dish.categories.map(category => category.id).includes(category.id)),
//   }))
//   .filter(category => category.dishes.length > 0)

  (
    <Paper className={styles.fullPaper}>
      <Box className={styles.fullImage}>
        <Image src={dish.mainImage || defaultDishImage} alt={dish.name} fill />
      </Box>
      <Box className={styles.fullText}>
        <Typography variant='h5' fontWeight='bold'>
          {dish.name}
        </Typography>
        <Typography variant='body1'>{dish.description}</Typography>
        <Prices prices={dish.prices} />
        {dish.ingredients.map(ingredient => (
          <Typography key={ingredient.id}>{ingredient.name}</Typography>
        ))}
      </Box>
    </Paper>
  )


const DishCard = ({dish}: {dish: Dish}) => {
  const [dishModal, setDishModal] = useState<Dish | undefined>(undefined)

  if (!dish) {
    return <DishNotFound />
  }

  return (
    <ButtonBase onClick={() => setDishModal(dish)}>
      <MediumDishCard dish={dish} />
      <Modal isOpen={!!dishModal} close={() => setDishModal(undefined)}>
        {dishModal ? <FullDishCard dish={dishModal} /> : <></>}
      </Modal>
    </ButtonBase>
  )
}

export default DishCard
