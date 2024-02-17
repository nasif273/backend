// Importing the required modules
const express = require('express');
const mongoose = require('mongoose');
const db = require('./db');
require('dotenv').config();
const app = express();

app.use(express.json());


// Define a route
app.get('/', (req, res) => {
  res.send('Hello, world!\n');
});



// Define a route to handle 404 errors
app.use((req, res, next) => {
  res.status(404).send('404 Not Found\n');
});

// Starting the server
const PORT = 8000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
