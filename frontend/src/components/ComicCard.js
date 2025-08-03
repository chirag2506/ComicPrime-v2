import { Card, CardContent, Typography, Box, Chip, Button, CardActions } from "@mui/material";
import LaunchIcon from "@mui/icons-material/Launch";

export default function ComicCard({
  title,
  volume,
  issue,
  coverMonth,
  coverYear,
  releaseDate,
  reprint,
  toBeRead,
  url,
}) {
  return (
    <Card
      sx={{
        backgroundColor: "#f7fdf9",
        borderRadius: 3,
        padding: 2,
        boxShadow: 4,
        display: "flex",
        flexDirection: "column",
        gap: 1.5,
      }}
    >
      <CardContent>
        <Typography variant="h6" sx={{ fontWeight: "bold", color: "#0c9b48" }}>
          {title} (Vol. {volume}) #{issue}
        </Typography>

        <Typography variant="body2" color="textSecondary">
          Cover Date: {coverMonth} {coverYear}
        </Typography>

        <Typography variant="body2" color="textSecondary">
          Release Date: {releaseDate}
        </Typography>

        <Box sx={{ display: "flex", flexWrap: "wrap", gap: 1, marginTop: 1 }}>
          <Chip
            label="Reprint"
            sx={{
              backgroundColor: reprint ? "#ffd54f" : "transparent",
              border: "1px solid #ffd54f",
              color: reprint ? "black" : "#888",
            }}
          />
          <Chip
            label="To Be Read"
            sx={{
              backgroundColor: toBeRead ? "#81c784" : "transparent",
              border: "1px solid #81c784",
              color: toBeRead ? "black" : "#888",
            }}
          />
        </Box>
      </CardContent>

      <CardActions sx={{ justifyContent: "space-between" }}>
        <Button
          variant="outlined"
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          endIcon={<LaunchIcon />}
          sx={{
            borderColor: "#0c9b48",
            color: "#0c9b48",
            textTransform: "none",
            fontWeight: "bold",
          }}
        >
          View on Wiki
        </Button>

        <Button
          variant="contained"
          sx={{
            backgroundColor: "#0c9b48",
            color: "white",
            textTransform: "none",
            fontWeight: "bold",
          }}
        >
          Dive into {title} (Vol. {volume})
        </Button>
      </CardActions>
    </Card>
  );
}
