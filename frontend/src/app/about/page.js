import React from 'react'
import { Container, Typography, Paper } from "@mui/material";

export default function About() {
  return (
    <Container maxWidth="md" sx={{ marginTop: 4 }}>
      <Paper sx={{ padding: 4, textAlign: "center" }}>
        <Typography variant="h4" gutterBottom>About This App</Typography>
        <Typography variant="body1">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </Typography>
      </Paper>
    </Container>
  )
}
