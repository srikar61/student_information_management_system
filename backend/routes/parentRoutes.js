const express = require('express');
const Parent = require('../models/parent');

const router = express.Router();

// Parent Signup
router.post('/signup', async (req, res) => {
    try {
        const { name, studentRollNumber, password } = req.body;

        // Check if roll number is already registered
        const existingParent = await Parent.findOne({ studentRollNumber });
        if (existingParent) {
            return res.status(400).json({ message: "Parent with this student roll number already exists" });
        }

        // Create new parent
        const newParent = new Parent({ name, studentRollNumber, password });
        await newParent.save();

        res.json({ message: "Parent account created successfully" });
    } catch (error) {
        res.status(500).json({ message: "Internal server error", error });
    }
});

// Parent Login
router.post('/login', async (req, res) => {
    try {
        const { studentRollNumber, password } = req.body;
        const parent = await Parent.findOne({ studentRollNumber, password });

        if (!parent) return res.status(400).json({ message: "Invalid credentials" });

        res.json({ message: "Login successful" });
    } catch (error) {
        res.status(500).json({ message: "Internal server error", error });
    }
});

module.exports = router;
