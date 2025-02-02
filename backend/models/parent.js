const mongoose = require('mongoose');

const ParentSchema = new mongoose.Schema({
    name: { type: String, required: true, minlength: 3 },
    studentRollNumber: { type: String, required: true, unique: true },
    password: { type: String, required: true, minlength: 6 }
});

module.exports = mongoose.model('parent', ParentSchema);
