import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2];

    try {
      const students = await readDatabase(database);
      let output = 'This is the list of our students\n';

      const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      for (let i = 0; i < fields.length; i++) {
        const field = fields[i];
        const names = students[field];
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        if (i < fields.length - 1) {
          output += '\n';
        }
      }

      res.status(200).send(output);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const database = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(database);
      const names = students[major] || [];
      res.status(200).send(`List: ${names.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
