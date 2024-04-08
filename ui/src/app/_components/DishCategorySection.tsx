import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Grid from '@mui/material/Unstable_Grid2'
import Image from 'next/image'


const DishCategorySection = ({ category, children }: { category: any; children: JSX.Element }) => {
  const Banner = ({ category }: any) => {
    if (category.banner) {
      return (
        <Box
          position='relative'
          height='150px'
          maxHeight='150px'
          >
          <Image
            src={category.banner}
            alt={category.name}
            fill={true}
            style={{
              objectFit: 'contain',
            }}
          />
        </Box>
      )
    } else {
      return (
        <Typography variant='h3'>{category.name}</Typography>
      )
    }
  }

  return (
    <Box
      id={`category-${category.id}`}
      width={1}>
      <Banner category={category} />
      <Grid
        container
        spacing={3}
        justifyContent='center'
        p={1}
        m={1}
        width={1}>
        {children}
      </Grid>
    </Box>
  )
}

export default DishCategorySection
