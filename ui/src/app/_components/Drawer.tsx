import Box from '@mui/material/Box'
import SwipeableDrawer from '@mui/material/SwipeableDrawer'

const Drawer = ({
  side,
  children,
  setOpen,
  isOpen,
  onClosed,
}: {
  side: 'left' | 'right' | 'bottom' | 'top'
  children: JSX.Element
  setOpen: any
  isOpen: boolean
  onClosed?: any
}) => {
  const border = 12
  const borderProps = {
    left: { borderTopRightRadius: border, borderBottomRightRadius: border },
    right: { borderTopLeftRadius: border, borderBottomLeftRadius: border },
    top: { borderBottomLeftRadius: border, borderBottomRightRadius: border },
    bottom: { borderTopLeftRadius: border, borderTopRightRadius: border },
  }

  const onClosedHandler = () => {
    if(onClosed) {
      const timeToClose = 200
    setTimeout(() => onClosed(), timeToClose)}
    }

  return (
    <SwipeableDrawer
      anchor={side}
      open={isOpen}
      onClose={() => {setOpen(false); onClosedHandler()}}
      onOpen={() => setOpen(true)}
      sx={{
        '& .MuiDrawer-paper': { ...borderProps[side] },
      }}>
      <Box
        py={1}
        px={1}>
        {children}
      </Box>
    </SwipeableDrawer>
  )
}

export default Drawer
