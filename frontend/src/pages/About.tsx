import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const About: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          About Joseki Craft Lab
        </Typography>
        <Typography variant="body1" paragraph>
          Joseki Craft Lab is an innovative tool designed for creating, managing, and analyzing shogi opening strategies.
        </Typography>
        <Typography variant="body1" paragraph>
          Using graph database technology, we provide a unique and powerful way to explore and understand complex opening sequences in shogi.
        </Typography>
        {/* TODO: Add more content, such as:
          - Team information
          - Project history
          - Technology stack
        */}
      </Box>
    </Container>
  );
};

export default About;