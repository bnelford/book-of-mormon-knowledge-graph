const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to set Content Security Policy headers
app.use((req, res, next) => {
  res.setHeader('Content-Security-Policy', "default-src 'self'; connect-src 'self'; script-src 'self' https://d3js.org 'sha256-5pyOZXZ43bXyNzbq3kuAIeDN5y8dVTsaduIngUAhqMM='; style-src 'self' 'unsafe-inline'; img-src 'self';");
  next();
});

// Serve static files (e.g., index.html)
app.use(express.static(path.join(__dirname)));

// Explicitly serve index.html for the root route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Endpoint to serve the knowledge graph data
app.get('/api/data', (req, res) => {
  const dataPath = path.join(__dirname, 'data.json');
  fs.readFile(dataPath, 'utf8', (err, data) => {
    if (err) {
      res.status(500).send('Error reading data file.');
    } else {
      res.json(JSON.parse(data));
    }
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});