export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentsByCity = students.filter(
    (student) => student.location === city
  );

  return studentsByCity.map((student) => {
    let grade = "N/A";

    for (let i = 0; i < newGrades.length; i++) {
      if (newGrades[i].studentId === student.id) {
        grade = newGrades[i].grade;
      }
    }

    return {
      id: student.id,
      firstName: student.firstName,
      location: student.location,
      grade: grade,
    };
  });
}
