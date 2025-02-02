const express = require('express');
const router = express.Router();
const StudentAuth = require('../models/studentAuth'); // Import the studentAuth model

// Student Signup API
router.post('/signup', async (req, res) => {
  try {
    const { rollNumber, password } = req.body;

    // Check if student already exists
    const existingStudent = await StudentAuth.findOne({ rollNumber });
    if (existingStudent) {
      return res.status(400).json({ error: "Student already exists" });
    }

    // Create new student for authentication
    const newStudent = new StudentAuth({ rollNumber, password });
    await newStudent.save();
    
    res.json({ message: "Signup successful", rollNumber: newStudent.rollNumber });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Student Login API
router.post('/login', async (req, res) => {
  try {
    const { rollNumber, password } = req.body;

    const student = await StudentAuth.findOne({ rollNumber });
    if (!student) return res.status(404).json({ error: "Student not found" });

    // Check password
    if (student.password !== password) {
      return res.status(401).json({ error: "Invalid password" });
    }

    res.json({ message: "Login successful", rollNumber: student.rollNumber });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get Student Data by Roll Number (This can be updated to pull data from a different model)
router.get('/:rollNumber', async (req, res) => {
  try {
    const student = await StudentAuth.findOne({ rollNumber: req.params.rollNumber });
    if (!student) return res.status(404).json({ error: "Student not found" });

    res.json(student);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
