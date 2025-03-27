import { Button, Box, Typography, Container, Card, CardContent } from "@mui/material";
import Link from "next/link";

export default function Home() {
  return (
    <Container maxWidth="lg" sx={{ textAlign: "center", padding: "40px 20px" }}>
      <Typography variant="h2" fontWeight="bold" gutterBottom>
        ComicsPRIME
      </Typography>
      <Typography variant="h6" color="textSecondary" paragraph>
        your friendly neighborhood comic guide...
      </Typography>
      <Button
        variant="contained"
        color="primary"
        sx={{ marginTop: 2, backgroundColor: "#0c9b48" }}
        component={Link}
        href="/dashboard"
      >
        Get Started
      </Button>
      
      {/* Feature Section */}
      <Box mt={6} display="flex" flexDirection={{ xs: "column", md: "row" }} gap={3}>
        <Card sx={{ flex: 1, padding: 2, boxShadow: 3 }}>
          <CardContent>
            <Typography variant="h5" fontWeight="bold">Track Your Progress</Typography>
            <Typography color="textSecondary">Never lose track of where you left off in your favorite comics.</Typography>
          </CardContent>
        </Card>
        <Card sx={{ flex: 1, padding: 2, boxShadow: 3 }}>
          <CardContent>
            <Typography variant="h5" fontWeight="bold">Discover New Comics</Typography>
            <Typography color="textSecondary">Get recommendations based on your reading history.</Typography>
          </CardContent>
        </Card>
        <Card sx={{ flex: 1, padding: 2, boxShadow: 3 }}>
          <CardContent>
            <Typography variant="h5" fontWeight="bold">Organize Your Library</Typography>
            <Typography color="textSecondary">Keep track of your collection and reading habits easily.</Typography>
          </CardContent>
        </Card>
      </Box>
    </Container>
  );
}
