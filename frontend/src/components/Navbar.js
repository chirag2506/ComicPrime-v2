"use client";
import { AppBar, Toolbar, IconButton, Button, Box, Drawer } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import { useState } from "react";
import Image from "next/image";
import appOldIcon from "@/assets/cpOldLogo.png"
import Link from "next/link";

export default function Navbar() {
    const [mobileOpen, setMobileOpen] = useState(false);

    const handleDrawerToggle = () => {
        setMobileOpen(!mobileOpen);
    };

    return (
        <>
            <AppBar position="static" sx={{ backgroundColor: "#FF5722" }}>
                <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
                    <Link href="/" passHref>
                        <Box sx={{ width: 50, height: 50, position: "relative" }}>
                            <Image src={appOldIcon.src} alt="App Logo" layout="fill" objectFit="contain" />
                        </Box>
                    </Link>

                    {/* Desktop Navigation (Hidden on Small Screens) */}
                    <Box sx={{ display: { xs: "none", md: "flex" }, gap: 2 }}>
                        <Link href="/about" passHref><Button color="inherit">About</Button></Link>
                        <Button color="inherit">News</Button>
                        <Button color="inherit">Comics</Button>
                    </Box>

                    {/* Mobile Menu Button (Visible on Small Screens) */}
                    <IconButton
                        edge="end"
                        color="inherit"
                        aria-label="menu"
                        onClick={handleDrawerToggle}
                        sx={{ display: { xs: "flex", md: "none" } }}
                    >
                        <MenuIcon />
                    </IconButton>

                    {/* Login Button (Always on the Right) */}
                    <Button color="inherit" sx={{ display: { xs: "none", md: "flex" } }}>
                        Login
                    </Button>
                </Toolbar>
            </AppBar>

            {/* Mobile Navigation Drawer */}
            <Drawer
                anchor="right"
                open={mobileOpen}
                onClose={handleDrawerToggle}
                sx={{
                    "& .MuiDrawer-paper": { width: 200, backgroundColor: "#FF5722" },
                }}
            >
                <Box sx={{ display: "flex", flexDirection: "column", p: 2 }}>
                    <Link href="/about" passHref><Button color="inherit" onClick={handleDrawerToggle}>About</Button></Link>
                    <Button color="inherit" onClick={handleDrawerToggle}>News</Button>
                    <Button color="inherit" onClick={handleDrawerToggle}>Comics</Button>
                    <Button color="inherit" onClick={handleDrawerToggle}>Login</Button>
                </Box>
            </Drawer>
        </>
    );
}
