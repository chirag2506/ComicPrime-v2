import React from 'react'
import { Container, Typography, Paper } from "@mui/material";
import Link from 'next/link';

export default function About() {
  return (
    <Container maxWidth="md" sx={{ marginTop: 4 }}>
      <Paper sx={{ padding: 4, textAlign: "center" }}>
        <Typography variant="h4" gutterBottom>About This App</Typography>
        <Typography variant="body1" sx={{ textAlign: "justify" }}>
          This project aims to help comic readers out there who might want to read comics (Marvel only, for now) in order of release from the beginning (they called me a Madman).
        </Typography>
        <Typography variant="body1" sx={{ textAlign: "justify" }}>
          I started this way back in 2020 (<Typography component={Link} href="https://github.com/chirag2506/ComicsPRIME-Android-" sx={{ color: "#0c9b48", fontWeight: "bold", textDecoration: "underline" }} underline="hover" target="_blank" rel="noopener noreferrer">Version 1</Typography>). Back then, the idea was to maintain the list of comics I have read. But then, I decided to read all Marvel comics published, so wrote a Python script to scrap the comics from official Marvel website into a word document.
        </Typography>
        <Typography variant="body1" sx={{ textAlign: "justify" }}>
          But it seems to be missing some comics, so I spent (wasted) much time comparing the scrapped list with the comics list available on the Marvel fandom, as and when I complete reading comics having cover date of a particular month. Now the problem in this is, there are a lot of titles that are just reprint titles or some are the ones that don't really matter to the greater comics continuity. Remembering each of these titles month after month seems to be a hassle, so I thought of solving this programmatically.
        </Typography>
      </Paper>
    </Container>
  )
}
