'use client'
import {createContext} from 'react'
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
      // FontWeightRegular: 400,
    },
    palette: {
      mode: 'light',
      /*
       * Primary: {
       * 	main: '#00bcd4',
       * },
       * secondary: {
       * 	main: '#9f69e7',
       * },
       * background: { default: 'rgb(22, 28, 36)', paper: 'rgb(33, 43, 54)' },
       */
    },
    components: {},
  })

export const DataContext = createContext<{}>({})

const LayoutWrapper: React.FC<{children: React.ReactNode}> = ({children}) => (
  <StyledEngineProvider injectFirst>
    <ThemeProvider theme={theme}>
      <DataContext.Provider value={{}}>
        <CssBaseline />
        {children}
      </DataContext.Provider>
    </ThemeProvider>
  </StyledEngineProvider>
)

export default LayoutWrapper
