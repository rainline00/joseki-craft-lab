import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { AppBar, Toolbar, Typography, Container, Box } from '@mui/material';
import { AppProvider } from './contexts/AppContext';
import theme from './styles/theme';
import Home from './pages/Home';
import About from './pages/About';

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppProvider>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Joseki Craft Lab
            </Typography>
            <Box>
              <Link to="/" style={{ color: 'white', marginRight: '10px', textDecoration: 'none' }}>Home</Link>
              <Link to="/about" style={{ color: 'white', textDecoration: 'none' }}>About</Link>
            </Box>
          </Toolbar>
        </AppBar>
        <Container>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </Container>
      </AppProvider>
    </ThemeProvider>
  );
};

export default App;