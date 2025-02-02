// backend/middleware/authMiddleware.js
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

dotenv.config(); // Load environment variables from .env file

module.exports = (req, res, next) => {
    const token = req.header('Authorization'); // Get token from request header

    if (!token) {
        return res.status(401).json({ error: 'Access denied. No token provided.' });
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET); // Verify token
        req.user = decoded; // Attach user data to request object
        next(); // Move to the next middleware or route handler
    } catch (error) {
        res.status(400).json({ error: 'Invalid token' });
    }
};
