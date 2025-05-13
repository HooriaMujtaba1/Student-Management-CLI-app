# 🎓 Student Management CLI App

A command-line interface (CLI) application for managing student records. This app supports creating, viewing, updating, and deleting student data stored in a JSON file, automatically syncs to a CSV file, features include reading external files and extracting specific columns from CSV files.

---

## 🚀 Features

- ✅ Add a new student
- 📋 View all students
- ✏️ Update existing student data
- 🗑️ Delete a student record
- 💾 Data persistence using `students.json`
- 📤 Automatic export to `students.csv` on every change
- 📂 Read file content from an absolute path
- 📊 Extract and display selected columns from a CSV file

---

## 🛠️ Technologies Used

- Python 3.x
- Standard libraries: `json`, `os`, `csv`

---
📁 Example Data Format
📄 CSV Format


ID,Name,Roll Number
1,Angel,1001
2,Mia,1002
3,Noor,1003
4,John,1004
📦 JSON Format

{
  "1": {
    "name": "Angel",
    "roll_number": "1001"
  },
  "2": {
    "name": "Mia",
    "roll_number": "1002"
  },
  "3": {
    "name": "Noor",
    "roll_number": "1003"
  },
  "4": {
    "name": "John",
    "roll_number": "1004"
  }
}


## 🧑‍💻 How to Use

1. **Clone the repository:**

   
   git clone https://github.com/HooriaMujtaba1/Student-Management-CLI-app
   
2. **Run the app:**

   python Student-CLI-app.py
   
   
## 📸 Example Screenshot
![Screenshot (378)](https://github.com/user-attachments/assets/e88a8d8c-5717-4220-8125-ef0068eed130)

## 📄 License

This project is available for learning, personal, and educational use. You are free to use, modify, and distribute it.

## 👤 Author

Project by: Hooria Mujtaba
Python CLI App: Student-Management-CLI App 


