import React from 'react';
import { render, screen } from '@testing-library/react';
import { AppProvider, useAppContext } from './AppContext';

const TestComponent: React.FC = () => {
  const { state, setCurrentPosition } = useAppContext();
  return (
    <div>
      <div data-testid="current-position">{state.currentPosition}</div>
      <button onClick={() => setCurrentPosition('new position')}>Update Position</button>
    </div>
  );
};

test('AppProvider provides initial state', () => {
  render(
    <AppProvider>
      <TestComponent />
    </AppProvider>
  );
  const positionElement = screen.getByTestId('current-position');
  expect(positionElement).toHaveTextContent('lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1');
});

// Add more tests for AppContext as needed