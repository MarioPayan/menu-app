'use client'
import {Nunito} from 'next/font/google'
import {StyledEngineProvider} from '@mui/material/styles'
import createTheme from '@mui/material/styles/createTheme'
import CssBaseline from '@mui/material/CssBaseline'
import ThemeProvider from '@mui/material/styles/ThemeProvider'

const nunito = Nunito({
  weight: ['200', '300', '400', '500', '600', '700'],
  subsets: ['latin'],
  fallback: ['Roboto', 'Helvetica', 'Arial', 'sans-serif'],
})

const theme = createTheme({
  typography: {
    fontFamily: nunito.style.fontFamily,
    // fontWeightRegular: 400,
  },
  palette: {
    mode: 'light',
    primary: {
      main: '#00bcd4',
    },
    secondary: {
      main: '#9f69e7',
    },
    // background: {default: 'rgb(22, 28, 36)', paper: 'rgb(33, 43, 54)'},
  },
  components: {
    MuiTypography: {
      styleOverrides: {
        root: {
          lineHeight: '1.1',
        },
      },
    },
    MuiPaper: {
      defaultProps: {
        elevation: 3,
      },
      styleOverrides: {
        root: {
          borderRadius: 8,
        },
      },
    },
  },
})

const LayoutWrapper: React.FC<{children: React.ReactNode}> = ({children}) => (
  <StyledEngineProvider injectFirst>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {children}
    </ThemeProvider>
  </StyledEngineProvider>
)

export default LayoutWrapper
