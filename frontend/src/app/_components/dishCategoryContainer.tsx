import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Image from 'next/image'

const DishCategoryNotFound = async () => <div>Category not found</div>

interface Banner {
  (props: {category: DishCategory}): JSX.Element
}
const Banner: Banner = ({category}) => {
  const ImageBanner: Banner = ({category}) => (
    <Image src={category.banner as string} alt={category.name} width={200} height={50} />
  )

  const TextBanner: Banner = ({category}) => <Typography variant='h3'>{category.name}</Typography>

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center',
      }}>
      {category.banner ? <ImageBanner category={category} /> : <TextBanner category={category} />}
    </Box>
  )
}

const DishCategoryCard = ({category, children}: {category: DishCategory; children: React.ReactNode}) => {
  if (!category) {
    return <DishCategoryNotFound />
  }
  return (
    <Box sx={{padding: '0.5rem'}}>
      <Banner category={category} />
      {children}
    </Box>
  )
}

export default DishCategoryCard
