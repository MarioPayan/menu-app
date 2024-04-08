import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import IconButton from '@mui/material/IconButton'
import MenuIcon from '@mui/icons-material/Menu'
import Slide from '@mui/material/Slide'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import useScrollTrigger from '@mui/material/useScrollTrigger'

const ButtonAppBar = ({
  restaurant,
  toggleLeftDrawer,
  toggleRightDrawer,
  isDrawerOpen = false
}: {
  restaurant: any
  toggleLeftDrawer?: any
  toggleRightDrawer?: any
  isDrawerOpen?: boolean
}) => {
  const isAtTop = useScrollTrigger({
    disableHysteresis: true,
    threshold: 0,
  })
  // const isScrollingUp = !useScrollTrigger()
  const isScrollingUp = true

  return (
    <Slide
      direction='down'
      in={isDrawerOpen || isScrollingUp}>
      <Box height={64}>
        <AppBar style={
          {
            backgroundColor: `rgba(25, 118, 210, ${isDrawerOpen || isAtTop ? 1 : 0})`,
            color: isDrawerOpen || isAtTop ? 'white' : 'black',
            transition: 'all 0.3s linear'
          }
        }>
          <Toolbar
            sx={{
              display: 'flex',
              justifyContent: 'space-between',
            }}>
            {toggleLeftDrawer && (
              <IconButton
                size='large'
                edge='start'
                color='inherit'
                aria-label='menu'
                onClick={() => toggleLeftDrawer()}>
                <MenuIcon />
              </IconButton>
            )}
            <Typography>{restaurant.name}</Typography>
            {toggleRightDrawer && (
              <IconButton
                size='large'
                edge='start'
                color='inherit'
                aria-label='menu'
                onClick={() => toggleRightDrawer()}>
                <MenuIcon />
              </IconButton>
            )}
          </Toolbar>
        </AppBar>
      </Box>
    </Slide>
  )
}

export default ButtonAppBar
