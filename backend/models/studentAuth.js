const mongoose = require('mongoose');

const StudentAuthSchema = new mongoose.Schema({
    rollNumber: { type: String, required: true, unique: true },
    password: { type: String, required: true, minlength: 6 }
});

// Explicitly set the collection name to 'studentauth'
module.exports = mongoose.model('studentauth', StudentAuthSchema, 'studentauth');
