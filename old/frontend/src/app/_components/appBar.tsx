import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import IconButton from '@mui/material/IconButton'
import MenuIcon from '@mui/icons-material/Menu'
import Image from 'next/image'

interface Banner {
  (props: {restaurant: Restaurant}): JSX.Element
}

const Banner: Banner = ({restaurant}) => {
  const ImageBanner: Banner = ({restaurant}) => <Image src={restaurant.banner} alt='Banner' fill />

  const TextBanner: Banner = ({restaurant}) => (
    <Typography variant='h6' component='div' sx={{flexGrow: 1}}>
      {restaurant.name}
    </Typography>
  )

  if (restaurant.banner) {
    return <ImageBanner restaurant={restaurant} />
  }
  return <TextBanner restaurant={restaurant} />
}

function ButtonAppBar({menu}: {menu: Menu}) {
  return (
    <Box sx={{flexGrow: 1}}>
      <AppBar position='static'>
        <Toolbar>
          <IconButton size='large' edge='start' color='inherit' aria-label='menu'>
            <MenuIcon />
          </IconButton>
          <Box display='flex' width={1} justifyContent='center'>
            <Banner restaurant={menu.restaurant} />
          </Box>
        </Toolbar>
      </AppBar>
    </Box>
  )
}

export default ButtonAppBar
