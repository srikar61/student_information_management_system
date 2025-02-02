const express = require('express');
const Student = require('../models/Student');

const router = express.Router();

// Create Student
router.post('/add', async (req, res) => {
    
    try {
        const { name, rollNumber, marks, rank, attendance } = req.body;

        if (!name || !rollNumber || marks === undefined || !rank || attendance === undefined) {
            return res.status(400).json({ message: "All fields are required" });
        }

        // Check if student already exists
        const existingStudent = await Student.findOne({ rollNumber });
        if (existingStudent) {
            return res.status(400).json({ message: "Student already exists" });
        }

        const student = new Student({ name, rollNumber, marks, rank, attendance });
        await student.save();

        res.status(201).json({ message: "Student added successfully!" });
    } catch (error) {
       
        res.status(500).json({ message: "Server error", error: error.message });
    }
});

// Get Student by Roll Number
router.get('/:rollNumber', async (req, res) => {
    try {
        const student = await Student.findOne({ rollNumber: req.params.rollNumber });
        if (!student) return res.status(404).json({ message: "Student not found" });

        res.json(student);
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
});

// Get All Students
router.get('/', async (req, res) => {
    try {
        const students = await Student.find();
        res.json(students);
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
});

// Update Student
router.put('/update/:rollNumber', async (req, res) => {
    try {
        const { name, marks, rank, attendance } = req.body;

        // Validate attendance before update
        if (isNaN(attendance)) {
            return res.status(400).json({ message: "Attendance must be a valid number" });
        }

        // Ensure that attendance is a number (if required by your schema)
        const updatedData = {
            name,
            marks,
            rank,
            attendance: Number(attendance) // Convert attendance to a number before updating
        };

        const student = await Student.findOneAndUpdate(
            { rollNumber: req.params.rollNumber },
            updatedData,
            { new: true, runValidators: true } // Ensure validation runs
        );

        if (!student) {
            return res.status(404).json({ message: "Student not found" });
        }

        res.json({ message: "Student updated successfully", student });
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
});


// Delete Student
router.delete('/delete/:rollNumber', async (req, res) => {
    try {
        const student = await Student.findOneAndDelete({ rollNumber: req.params.rollNumber });

        if (!student) return res.status(404).json({ message: "Student not found" });

        res.json({ message: "Student deleted successfully" });
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
});

module.exports = router;
