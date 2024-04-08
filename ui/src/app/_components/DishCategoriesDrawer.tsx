import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Button from '@mui/material/Button'
import Drawer from './Drawer'

const DishCategoriesDrawer = ({
  dishCategories,
  setOpen,
  isOpen,
  scrollToCategory,
}: {
  dishCategories?: any[]
  setOpen: any
  isOpen: boolean
  scrollToCategory: any
}) => {
  if (!dishCategories?.length) {
    return null
  }

  return (
    <Drawer
      side='left'
      isOpen={isOpen}
      setOpen={setOpen}>
      <Box
        display='flex'
        flexDirection='column'
        gap={2}>
        <Typography
          variant='h5'
          display='flex'
          justifyContent='center'
          width={1}>
          Categories
        </Typography>
        <Box
          display='flex'
          flexDirection='column'
          gap={1}>
          {dishCategories.map((category: any) => (
            <Button
              key={category.id}
              variant='text'
              fullWidth
              sx={{justifyContent: 'flex-start'}}
              onClick={() => {
                setOpen(false)
                scrollToCategory(category)
              }}>
              {category.name}
            </Button>
          ))}
        </Box>
      </Box>
    </Drawer>
  )
}

export default DishCategoriesDrawer
