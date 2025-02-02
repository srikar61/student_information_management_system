const mongoose = require('mongoose');

const StudentSchema = new mongoose.Schema({
    name: { type: String, required: true, trim: true },
    rollNumber: { type: String, required: true, unique: true, trim: true },
    marks: { type: Number, required: true, min: 0, max: 100 },
    rank: { type: Number, required: true, min: 1 },
    attendance: { type: Number, required: true, min: 0, max: 100 }
});

module.exports = mongoose.model('Student', StudentSchema);
