const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = lines.slice(1);
      const fields = {};

      for (let i = 0; i < students.length; i++) {
        const line = students[i].split(',');
        const firstname = line[0];
        const field = line[3];

        if (firstname && field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      }

      const output = [];
      output.push(`Number of students: ${students.length}`);

      const fieldKeys = Object.keys(fields);
      for (let i = 0; i < fieldKeys.length; i++) {
        const field = fieldKeys[i];
        const names = fields[field];
        output.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve(output);
    });
  });
}

const app = express();
const port = 1245;
const DATABASE = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  try {
    const students = await countStudents(DATABASE);
    res.end(`${students.join('\n')}`);
  } catch (error) {
    res.end(error.message);
  }
});

app.listen(port);

module.exports = app;
