# 🎓 Student Management System (OOP)

A modular, command-line Student Management System built with Python using Object-Oriented Programming (OOP) principles. The application encapsulates student records within custom classes and handles data persistence seamlessly using JSON serialization.

---

## ✨ Features

- ➕ Add new student records with unique IDs
- 📋 View all stored students in a clean format
- 🔍 Search student records by ID or Name
- 🗑️ Delete student records by ID
- 💾 Automatic JSON data storage
- 🔄 Data persistence across application runs
- ⚠️ Built-in input validation and duplicate ID handling
- 🖥️ Object-Oriented CLI design

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (Classes, Objects, Class Methods, Constructors)
- JSON Serialization
- File Handling & Exception Handling
- Data Structures (Lists & Dictionaries)
- Git & GitHub

---

## 📂 Project Structure

student_management_system/
│
├── student_manager.py
├── students.json
├── README.md
└── .gitignore


---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/veereshkallapally555-maker/student-management-system.git
```
### Navigate to the project

```Bash
cd student-management-system
```

### Run the application

```Bash
python student_manager.py
```

---

## 📸 Sample Output

```

====== Student Management System (OOP) ======

1. Add Student
2. View All Students
3. Search Student
4. Delete Student
5. Exit

Enter Choice (1-5): 1

Enter Student ID: 101
Enter Name: Veeresh Kallapally
Enter Age: 21
Enter Grade (e.g., A, B, C): A

✅ Student 'Veeresh Kallapally' added successfully!
📄 Example students.json
JSON
[
    {
        "student_id": "101",
        "name": "Veeresh Kallapally",
        "age": 21,
        "grade": "A"
    },
    {
        "student_id": "102",
        "name": "Rahul Sharma",
        "age": 22,
        "grade": "B"
    }
]
```

---


## 🎯 Skills Demonstrated

- Object-Oriented Programming (OOP) Principles
- Instance & Class Methods (@classmethod)
- JSON Data Serialization & Deserialization
- Exception & Input Validation Handling
- Command Line Interface (CLI) Architecture
- Version Control with Git & GitHub

---


## 🔮 Future Improvements

- Connect to SQLite database for relational storage
- Calculate average class GPA / grades
- Filter students by grade or age
- Export student records to CSV or Excel
- Graphical User Interface (Tkinter / PyQt)

👨‍💻 Author
Veeresh Kallapally

If you found this project helpful, consider giving it a ⭐ on GitHub!

🌐 Connect with Me

🐙 GitHub: [@veereshkallapally555-maker](https://github.com/veereshkallapally555-maker)

💼 LinkedIn: [Veeresh Kallapally](https://www.linkedin.com/in/veeresh-kallapally-a87164390/)
