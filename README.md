# School Management System

A simple, lightweight **School Management System** built in Python. This project allows a school administrator to register students and teachers, assign and manage grades by subject, and view all registered details in a clean, organized way — all from the command line, with no external dependencies required.

It's designed as a beginner-to-intermediate friendly project for learning core Python concepts such as object-oriented programming, data validation, file handling, and simple menu-driven applications.

---

## Table of Contents

- [Features](#features)
- [Project Motivation](#project-motivation)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Example Workflow](#example-workflow)
- [Sample Code Structure](#sample-code-structure)
- [Validation Rules](#validation-rules)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

### 🎓 Student Management
- Register new students with:
  - Roll Number (unique identifier)
  - Full Name
  - Email Address
- Prevent duplicate roll numbers from being registered
- View a complete list of all registered students

### 👩‍🏫 Teacher Management
- Register new teachers with:
  - Full Name
  - Employee ID (unique identifier)
  - Email Address
- Prevent duplicate employee IDs from being registered
- View a complete list of all registered teachers

### 📊 Grade Management
- Add grades for a student, organized by subject
- Support multiple subjects per student
- View a student's grades across all subjects
- Basic validation to ensure grades are recorded against valid, registered students

### 🔍 Viewing & Reporting
- View all student records in a formatted, readable output
- View all teacher records in a formatted, readable output
- View grade reports for individual students

### 🛠️ Simple, Menu-Driven Interface
- Console-based interactive menu
- No external libraries or database setup required
- Runs entirely in-memory (with optional file persistence, depending on implementation)

---

## Project Motivation

Schools and small institutions often need lightweight tools to keep track of student and teacher information without the overhead of a full database system or web application. This project demonstrates how core Python data structures (dictionaries, lists, and classes) can be used to build a functional record-keeping system that's easy to understand, extend, and maintain.

It's also a great learning exercise for:
- Practicing **Object-Oriented Programming (OOP)** in Python
- Understanding **CRUD operations** (Create, Read, Update, Delete) conceptually
- Building **menu-driven console applications**
- Handling **user input validation**
- Structuring a small but real-world-style Python project

---

## System Requirements

- Python 3.7 or higher
- No external packages required (uses only Python's standard library)
- Works on Windows, macOS, and Linux

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/SchoolManagementProject.git
   cd SchoolManagementProject
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

No additional dependencies need to be installed since the project relies solely on Python's built-in libraries.

---

## Usage

Once you run the program, you'll be presented with a menu of options similar to the following:

```
========== School Management System ==========
1. Register a Student
2. Register a Teacher
3. Add Grade for a Student
4. View All Students
5. View All Teachers
6. View Student Grades
7. Exit
================================================
Enter your choice:
```

Simply enter the number corresponding to the action you'd like to perform, and follow the on-screen prompts.

### Registering a Student
You'll be asked to provide:
- Roll Number
- Full Name
- Email Address

### Registering a Teacher
You'll be asked to provide:
- Full Name
- Employee ID
- Email Address

### Adding Grades
You'll be asked to provide:
- Student Roll Number
- Subject Name
- Grade/Score

### Viewing Records
Choose the relevant menu option to display a formatted list of all students, teachers, or a specific student's grades.

---

## Project Structure

A typical structure for this project might look like:

```
SchoolManagementProject/
│
├── main.py                # Entry point - runs the menu-driven interface
├── student.py              # Student class and related logic
├── teacher.py               # Teacher class and related logic
├── grades.py                 # Grade management logic
├── utils.py                   # Helper functions (validation, formatting, etc.)
├── data/                        # Optional folder for persisted data (if using file storage)
│   └── records.json
├── README.md                      # Project documentation (this file)
└── requirements.txt                # (Optional) dependency list, if any are added later
```

*Note: The exact structure may vary depending on how the project is implemented — it can also be written as a single script for simplicity.*

---

## Data Model

### Student
| Field       | Type   | Description                          |
|-------------|--------|---------------------------------------|
| Roll No     | String/Int | Unique identifier for the student |
| Name        | String | Full name of the student              |
| Email       | String | Contact email address                 |
| Grades      | Dict   | Subject-wise grades (e.g., `{"Math": "A", "Science": "B+"}`) |

### Teacher
| Field         | Type   | Description                        |
|---------------|--------|--------------------------------------|
| Employee ID   | String/Int | Unique identifier for the teacher |
| Name          | String | Full name of the teacher            |
| Email         | String | Contact email address               |

---

## Example Workflow

Here's a sample interaction showing how the system might be used end-to-end:

1. **Register a student**
   ```
   Enter Roll No: 101
   Enter Name: Aditi Sharma
   Enter Email: aditi.sharma@example.com
   ✅ Student registered successfully!
   ```

2. **Register a teacher**
   ```
   Enter Employee ID: T001
   Enter Name: Mr. Rajesh Kumar
   Enter Email: rajesh.kumar@example.com
   ✅ Teacher registered successfully!
   ```

3. **Add a grade**
   ```
   Enter Student Roll No: 101
   Enter Subject: Mathematics
   Enter Grade: A
   ✅ Grade added successfully!
   ```

4. **View all students**
   ```
   Roll No: 101 | Name: Aditi Sharma | Email: aditi.sharma@example.com
   ```

5. **View a student's grades**
   ```
   Grades for Aditi Sharma (Roll No: 101):
   Mathematics: A
   ```

---

## Sample Code Structure

Below is a simplified illustration of how the core classes might be organized (implementation details may vary):

```python
class Student:
    def __init__(self, roll_no, name, email):
        self.roll_no = roll_no
        self.name = name
        self.email = email
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade


class Teacher:
    def __init__(self, employee_id, name, email):
        self.employee_id = employee_id
        self.name = name
        self.email = email


class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def register_student(self, roll_no, name, email):
        if roll_no in self.students:
            print("Error: A student with this roll number already exists.")
            return
        self.students[roll_no] = Student(roll_no, name, email)
        print("Student registered successfully!")

    def register_teacher(self, employee_id, name, email):
        if employee_id in self.teachers:
            print("Error: A teacher with this employee ID already exists.")
            return
        self.teachers[employee_id] = Teacher(employee_id, name, email)
        print("Teacher registered successfully!")
```

This structure keeps each entity (`Student`, `Teacher`) as its own class, with a central `SchoolManagementSystem` class coordinating registration, validation, and reporting.

---

## Validation Rules

To keep the data consistent and reliable, the system should enforce the following rules:

- **Roll numbers and employee IDs must be unique** — duplicate entries should be rejected with a clear error message.
- **Email addresses should follow a basic valid format** (e.g., contain `@` and a domain).
- **Names should not be empty** and should ideally not contain numeric-only values.
- **Grades should only be added for students who are already registered.**
- **Input fields should be trimmed** of leading/trailing whitespace before being stored.

---

## Future Enhancements

This project can be extended in a number of directions, including:

- 💾 **Persistent storage** — save and load data using JSON, CSV, or a lightweight database like SQLite
- 🖥️ **Graphical User Interface (GUI)** — using Tkinter or PyQt for a more user-friendly experience
- 🌐 **Web-based interface** — using Flask or Django to turn this into a web application
- 🔐 **Authentication** — admin login system to restrict access to registration and editing features
- 📈 **Grade analytics** — calculate averages, class rankings, and generate report cards
- 📤 **Export functionality** — export student/teacher records and grade reports to PDF or Excel
- ✏️ **Update and delete operations** — allow editing or removing existing student/teacher records
- 🔎 **Search and filter** — search students/teachers by name, roll number, or subject
- ✅ **Unit tests** — add automated tests using `unittest` or `pytest` to ensure reliability

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes and commit them (`git commit -m "Add your feature"`)
4. Push to your branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request describing your changes

Please make sure your code follows clean, readable Python conventions (PEP 8) and includes comments where helpful.

---

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it for personal or educational purposes.

---

## Acknowledgements

This project was built as a learning exercise in Python fundamentals, object-oriented design, and simple application architecture. Thanks to everyone who contributes ideas, feedback, or code to help it grow.

---

*If you find this project useful, consider giving it a ⭐ on GitHub!*
