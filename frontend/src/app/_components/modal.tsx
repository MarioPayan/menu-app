import {forwardRef} from 'react'
import Dialog from '@mui/material/Dialog'
import Slide from '@mui/material/Slide'
import {TransitionProps} from '@mui/material/transitions'

const Transition = forwardRef(function Transition(
  props: TransitionProps & {
    // TODO: Fix this type
    children: React.ReactElement<any, any>
  },
  ref: React.Ref<unknown>
) {
  return <Slide direction='up' ref={ref} {...props} />
})

interface Modal {
  (props: {children: JSX.Element; isOpen: boolean; close: () => void}): JSX.Element
}

// TODO: Not closing
const Modal: Modal = ({children, isOpen, close}) => (
  <Dialog open={isOpen} TransitionComponent={Transition} onClose={close}>
    {children}
  </Dialog>
)

export default Modal
