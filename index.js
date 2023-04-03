const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

users = {}

app.post('/users', (req, res) => {
  const { name, score } = req.body;
  users.push({
    "name": name,
    "score": score
  })
  res.send('User created successfully');
});

app.get('/users', (req, res) => {
  res.send(users)
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
