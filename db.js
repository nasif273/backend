const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();

const conn = process.env.conn;

mongoose.connect(conn);

// Check if the connection was successful
const dbb = mongoose.connection;
dbb.on('error', console.error.bind(console, 'connection error:'));
dbb.once('open', () => {
  console.log('Connected to MongoDB Atlas');
});