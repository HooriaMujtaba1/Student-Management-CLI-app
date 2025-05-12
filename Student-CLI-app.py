import json
import os
import csv

class StudentManagementApp:

    def __init__(self, filename='students.json', csv_filename='students.csv'):
        self.filename = filename
        self.csv_filename = csv_filename
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("⚠️ Warning: JSON file is corrupted. Starting with empty data.")
                    return {}
        return {}

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)
        self.export_to_csv_auto()  # Automatically update CSV

    def export_to_csv_auto(self):
        if not self.students:
            return
        with open(self.csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Roll Number"])
            writer.writeheader()
            for student_id, data in self.students.items():
                writer.writerow({
                    "ID": student_id,
                    "Name": data["name"],
                    "Roll Number": data["roll_number"]
                })

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("❌ Student with this ID already exists.")
            return
        name = input("Enter Student Name: ")
        roll_number = input("Enter Student Roll Number: ")

        self.students[student_id] = {
            "name": name,
            "roll_number": roll_number
        }
        self.save_students()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("📭 No students found.")
            return

        print("\n📋 List of Students:")
        for sid, info in self.students.items():
            print(f"- ID: {sid}, Name: {info['name']}, Roll Number: {info['roll_number']}")

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        student = self.students[student_id]
        print("Leave input empty to keep current value.")
        name = input(f"New name [{student['name']}]: ") or student['name']
        roll_number = input(f"New roll number [{student['roll_number']}]: ") or student['roll_number']

        self.students[student_id] = {
            "name": name,
            "roll_number": roll_number
        }
        self.save_students()
        print("✅ Student updated successfully!")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            self.save_students()
            print("✅ Student deleted.")
        else:
            print("❌ Student not found.")

    def read_file_from_path(self):
        path = input("Enter absolute file path: ")
        if not os.path.isfile(path):
            print("❌ File not found.")
            return
        with open(path, 'r') as file:
            content = file.read()
            print("\n📄 File Contents:\n")
            print(content)

    def bonus_feature_csv_columns(self):
        path = input("Enter absolute CSV file path: ").strip()
        if not os.path.isfile(path):
            print("❌ File not found at given path.")
            return

        try:
            with open(path, mode='r') as file:
                reader = csv.DictReader(file)
                print(f"\nAvailable columns: {', '.join(reader.fieldnames)}")
                num_columns = int(input("How many columns do you want to extract? "))
                selected_columns = []
                for i in range(num_columns):
                    col = input(f"Enter column name #{i+1}: ").strip()
                    selected_columns.append(col)

                print("\n📊 Extracted Data:")
                for row in reader:
                    for col in selected_columns:
                        if col in row:
                            print(f"{col}: {row[col]}", end=" | ")
                    print()
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def run(self):
        operations = {
            '1': self.add_student,
            '2': self.view_students,
            '3': self.update_student,
            '4': self.delete_student,
            '5': self.read_file_from_path,
            '6': self.bonus_feature_csv_columns
        }

        while True:
            print("\n📚 Student Management CLI App")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Read File from Absolute Path")
            print("6. Extract Specific Columns from CSV File")

            choice = input("Choose an option (1-6): ")
            action = operations.get(choice)
            if action:
                action()
            else:
                print("❌ Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    app = StudentManagementApp()
    app.run()
























































