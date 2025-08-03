"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Container, Typography, Paper, MenuItem, Select, FormControl, InputLabel, Button, Box, } from "@mui/material";



import ComicCard from "@/components/ComicCard";
import bg1 from "@/assets/comicBackgrounds/bg1.png";


const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",];

const publishers = ["Marvel"];

const currentYear = new Date().getFullYear();
const years = Array.from({ length: currentYear - 1900 }, (_, i) => 1901 + i); // taking start as 1900

export default function Browse() {
  const [month, setMonth] = useState(0);
  const [year, setYear] = useState(currentYear);
  const [publisher, setPublisher] = useState("Marvel");
  const router = useRouter();

  const handleSubmit = () => {
    router.push(`/browse/${String(month + 1).padStart(2, "0")}-${year}`);
  };

  return (
    <Container maxWidth="sm" sx={{ marginTop: 4 }}>
      <Paper sx={{ padding: 4, borderRadius: 3 }}>
        <Typography variant="h5" sx={{ textAlign: "center", marginBottom: 3 }}>
          Browse Comics by Cover Date
        </Typography>

        <Box sx={{ display: "flex", flexDirection: "column", gap: 3 }}>
          <FormControl fullWidth>
            <InputLabel>Month</InputLabel>
            <Select
              value={month}
              label="Month"
              onChange={(e) => setMonth(Number(e.target.value))}
            >
              {months.map((m, index) => (
                <MenuItem key={index} value={index}>
                  {m}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl fullWidth>
            <InputLabel>Year</InputLabel>
            <Select
              value={year}
              label="Year"
              onChange={(e) => setYear(Number(e.target.value))}
            >
              {years.map((y) => (
                <MenuItem key={y} value={y}>
                  {y}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl fullWidth>
            <InputLabel>Publisher</InputLabel>
            <Select
              value={publisher}
              label="Publisher"
              onChange={(e) => setPublisher(e.target.value)}
            >
              {publishers.map((p, index) => (
                <MenuItem key={index} value={p}>
                  {p}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <Button
            variant="contained"
            onClick={handleSubmit}
            sx={{
              backgroundColor: "#0c9b48",
              color: "white",
              textTransform: "none",
              fontWeight: "bold",
              fontSize: "1rem",
              paddingY: 1.2,
            }}
          >
            View Comics
          </Button>
        </Box>
      </Paper>
      <ComicCard
        title="'Breed II"
        volume={1}
        issue="1"
        coverMonth="November"
        coverYear={1994}
        releaseDate="November 14, 1994"
        reprint={true}
        toBeRead={false}
        url="https://marvel.fandom.com/wiki/%27Breed_II_Vol_1_1"
        backgroundImage={bg1}
        textColor="#ffffff"
        buttonColor="#ffd600"
      />
    </Container>
  );
}
