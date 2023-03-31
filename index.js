const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.post('/users', (req, res) => {
  const { name, email } = req.body;
  // perform any necessary processing on the data
  res.send('User created successfully');
});


app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
