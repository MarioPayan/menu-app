import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import { numberToMoney } from '@/app/_utils/utils'

const DishPrices = ({ dish }: any) => {
  if (!dish.prices) {
    return null
  }

  return (
    <>
      {dish.prices.map((price: any) => (
        <Box
          key={price.id}
          display='flex'
          flexDirection='row'
          justifyContent='space-between'>
          <Typography
            noWrap
            variant='subtitle1'>
            {price.size}
          </Typography>
          <Typography
            noWrap
            variant='subtitle1'>
            {numberToMoney(price.final_price)}
          </Typography>
        </Box>
      ))}
    </>
  )
  
}

export default DishPrices
