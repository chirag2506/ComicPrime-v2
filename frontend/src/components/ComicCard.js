import {
  Card,
  CardContent,
  Typography,
  Box,
  Chip,
  Button,
  CardActions,
} from "@mui/material";
import LaunchIcon from "@mui/icons-material/Launch";
import Image from "next/image";
import { useEffect, useRef, useState } from "react";

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
  backgroundImage,
}) {
  const canvasRef = useRef(null);
  const [textColor, setTextColor] = useState("#0c9b48");
  const [buttonColor, setButtonColor] = useState("#0c9b48");

  const getAverageColor = (img) => {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    let r = 0, g = 0, b = 0, count = 0;

    for (let i = 0; i < imageData.length; i += 4 * 100) { // Sample every 100th pixel
      r += imageData[i];
      g += imageData[i + 1];
      b += imageData[i + 2];
      count++;
    }

    r = Math.floor(r / count);
    g = Math.floor(g / count);
    b = Math.floor(b / count);

    const brightness = (r * 299 + g * 587 + b * 114) / 1000;

    if (brightness < 130) {
      setTextColor("#ffffff");
      setButtonColor("#ffffff");
    } else {
      setTextColor("#0c9b48");
      setButtonColor("#0c9b48");
    }
  };

  useEffect(() => {
    if (!backgroundImage) return;

    const img = document.createElement("img");
    img.crossOrigin = "anonymous";
    img.src = backgroundImage;
    img.onload = () => getAverageColor(img);
  }, [backgroundImage]);

  return (
    <Card
      sx={{
        position: "relative",
        overflow: "hidden",
        borderRadius: 3,
        padding: 2,
        boxShadow: 4,
        display: "flex",
        flexDirection: "column",
        gap: 1.5,
        minHeight: "260px",
        transition: "transform 0.3s, box-shadow 0.3s",
        '&:hover': {
          transform: "scale(1.02)",
          boxShadow: 6,
        },
      }}
    >
      {backgroundImage && (
        <Box
          sx={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            opacity: 0.35,
            zIndex: 0,
          }}
        >
          <Image src={backgroundImage} alt="Comic BG" layout="fill" objectFit="cover" />
        </Box>
      )}

      <CardContent sx={{ position: "relative", zIndex: 1 }}>
        <Typography variant="h6" sx={{ fontWeight: "bold", color: textColor }}>
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

      <CardActions sx={{ justifyContent: "space-between", position: "relative", zIndex: 1 }}>
        <Button
          variant="outlined"
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          endIcon={<LaunchIcon />}
          sx={{
            borderColor: buttonColor,
            color: buttonColor,
            textTransform: "none",
            fontWeight: "bold",
          }}
        >
          View on Wiki
        </Button>

        <Button
          variant="contained"
          sx={{
            backgroundColor: buttonColor,
            color: buttonColor === "#ffffff" ? "black" : "white",
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
