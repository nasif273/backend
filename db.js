const express = require('express');
const mongoose = require('mongoose');

const conn = "mongodb+srv://admin:admin@cluster0.w3n0vll.mongodb.net/?retryWrites=true&w=majority";

mongoose.connect(conn, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Check if the connection was successful
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB Atlas');
});