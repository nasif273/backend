// Importing the required modules
const express = require('express');

// Creating an Express application
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello, world!\n');
});

// Define a route with a dynamic parameter
app.get('/greet/:name', (req, res) => {
  const name = req.params.name;
  res.send(`Hello, ${name}!\n`);
});

// Define a route to handle 404 errors
app.use((req, res, next) => {
  res.status(404).send('404 Not Found\n');
});