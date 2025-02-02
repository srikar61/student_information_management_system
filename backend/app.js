const express = require('express');
const mongoose = require('mongoose');
const session = require('express-session');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true
}));

// MongoDB Connection
mongoose.connect('mongodb://127.0.0.1:27017/sims', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Import Routes
const adminRoutes = require('./routes/adminRoutes');
const studentRoutes = require('./routes/studentRoutes');
const parentRoutes = require('./routes/parentRoutes');
const studentAuth = require('./routes/studentAuth');
app.use('/admin', adminRoutes);
app.use('/student', studentRoutes);
app.use('/parent', parentRoutes);
app.use('/api/student', studentAuth);
app.listen(5000, () => console.log('Server running on port 5000'));
