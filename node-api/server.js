const express = require('express');
const app = express();
const os = require('os');

app.get('/', (req, res) => {
    res.json({
        service: "Node.js Express 🟢",
        message: "I tell the time!",
        time: new Date().toISOString(),
        hostname: os.hostname()
    });
});

app.listen(3000, () => {
    console.log('Node server running on port 3000');
});