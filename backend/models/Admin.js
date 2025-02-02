const mongoose = require('mongoose');

const AdminSchema = new mongoose.Schema({
    username: { type: String, required: true ,minlength: 4},
    password: { type: String, required: true, minlength: 8 } // Enforce minimum 8 characters
});
module.exports = mongoose.model('Admin', AdminSchema);
