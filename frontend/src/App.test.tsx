import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import { AppProvider } from './contexts/AppContext';
import theme from './styles/theme';
import App from './App';

const renderWithProviders = (ui: React.ReactElement, { route = '/' } = {}) => {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <ThemeProvider theme={theme}>
        <AppProvider>
          {ui}
        </AppProvider>
      </ThemeProvider>
    </MemoryRouter>
  );
};

test('renders Joseki Craft Lab title in AppBar', () => {
  renderWithProviders(<App />);
  const titleElement = screen.getByRole('heading', { name: /Joseki Craft Lab/i });
  expect(titleElement).toBeInTheDocument();
});

test('renders Home link', () => {
  renderWithProviders(<App />);
  const homeLink = screen.getByRole('link', { name: /home/i });
  expect(homeLink).toBeInTheDocument();
});

test('renders About link', () => {
  renderWithProviders(<App />);
  const aboutLink = screen.getByRole('link', { name: /about/i });
  expect(aboutLink).toBeInTheDocument();
});

test('renders welcome message on home page', () => {
  renderWithProviders(<App />);
  const welcomeMessage = screen.getByRole('heading', { name: /Welcome to Joseki Craft Lab/i, level: 1 });
  expect(welcomeMessage).toBeInTheDocument();
});