import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { AppProvider } from '../../contexts/AppContext';
import Chessboard from './Chessboard';

describe('Chessboard', () => {
  it('renders the chessboard title', () => {
    render(
      <AppProvider>
        <Chessboard />
      </AppProvider>
    );
    expect(screen.getByText('Shogi Board')).toBeInTheDocument();
  });

  it('displays the current position', () => {
    render(
      <AppProvider>
        <Chessboard />
      </AppProvider>
    );
    expect(screen.getByText(/Current position \(SFEN\):/i)).toBeInTheDocument();
  });

  it('updates the position when the button is clicked', async () => {
    render(
      <AppProvider>
        <Chessboard />
      </AppProvider>
    );
    const initialPosition = screen.getByText(/lnsgkgsnl\/1r5b1\/ppppppppp\/9\/9\/9\/PPPPPPPPP\/1B5R1\/LNSGKGSNL b - 1/);
    expect(initialPosition).toBeInTheDocument();

    const updateButton = screen.getByText('Update Position (Demo)');
    await userEvent.click(updateButton);

    const updatedPosition = await screen.findByText(/lnsgkgsnl\/1r5b1\/ppppppppp\/9\/9\/9\/PPPPPPPPP\/1B5R1\/LNSGKGSNL w - 1/);
    expect(updatedPosition).toBeInTheDocument();
  });
});