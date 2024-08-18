import React from 'react';
import { Box, Typography, Button } from '@mui/material';
import { useAppContext } from '../../contexts/AppContext';

const Chessboard: React.FC = () => {
  const { state, setCurrentPosition } = useAppContext();

  // 仮の局面更新関数
  const updatePosition = () => {
    const newPosition = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 1';
    setCurrentPosition(newPosition);
  };

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Shogi Board
      </Typography>
      <Box
        sx={{
          width: '400px',
          height: '440px',
          border: '1px solid black',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Typography>Current position (SFEN):</Typography>
        <Typography fontFamily="monospace" marginY={2}>
          {state.currentPosition}
        </Typography>
        <Button variant="contained" onClick={updatePosition}>
          Update Position (Demo)
        </Button>
      </Box>
    </Box>
  );
};

export default Chessboard;