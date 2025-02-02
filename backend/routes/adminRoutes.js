const express = require('express');
const Admin = require('../models/Admin');


const router = express.Router();

// Admin Signup
router.post('/signup', async (req, res) => {
    try {
        const { username, password } = req.body;

        // Check if username exists
        const existingAdmin = await Admin.findOne({ username });
        if (existingAdmin) {
            return res.status(400).json({ message: "Admin already exists" });
        }

        // Create new admin
        const newAdmin = new Admin({ username, password });
        await newAdmin.save();

        res.json({ message: "Admin created successfully" });
    } catch (error) {
          // Log the error for debugging purposes
        res.status(500).json({ message: error });
    }
});

// Admin Login
router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        const admin = await Admin.findOne({ username, password });

        if (!admin) return res.status(400).json({ message: "Invalid credentials" });

        req.session.admin = admin._id;
        res.json({ message: "Login successful" });
    } catch (error) {
         // Log the error for debugging purposes
        res.status(500).json({ message: error });
    }
});

module.exports = router;
