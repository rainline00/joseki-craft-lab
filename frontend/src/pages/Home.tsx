import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const Home: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Welcome to Joseki Craft Lab
        </Typography>
        <Typography variant="body1">
          This is the home page of Joseki Craft Lab. Here you can explore and create shogi opening strategies.
        </Typography>
        {/* TODO: Add more content, such as:
          - Quick start guide
          - Featured openings
          - Recent activity
        */}
      </Box>
    </Container>
  );
};

export default Home;