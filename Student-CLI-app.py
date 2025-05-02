import json  # To handle JSON file operations 
import os  # To check if files exist
import csv  # To export/import student data in CSV format

class StudentManagementApp:
    
    def __init__(self, filename='students.json'):
        self.filename = filename  
        self.students = self.load_students() 

    # Loads the students data from a JSON file if it exists, otherwise returns an empty dictionary
    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)  
                except json.JSONDecodeError:
                    print("⚠️ Warning: JSON file is corrupted. Starting with empty data.")
                    return {}
        return {}

    # Saves the current students data to the JSON file
    def save_students(self):
        with open(self.filename, 'w') as file:
            # Write students data into JSON file with indentation for readability
            json.dump(self.students, file, indent=4)

    # Add a new student to the list
    def add_student(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            print("❌ Student with this ID already exists.")
            return
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        
        # Ensure age is a number
        if not age.isdigit():
            print("❌ Age must be a number.")
            return
        course = input("Enter student course: ")

        # Add the new student to the dictionary
        self.students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }
        self.save_students()
        print("✅ Student added successfully!")

    # View all students in the system
    def view_students(self):
        if not self.students:
            print("📭 No students found.")
            return

        print("\n📋 List of Students:")
        for sid, info in self.students.items():
            print(f"- ID: {sid}, Name: {info['name']}, Age: {info['age']}, Course: {info['course']}")

    # Update an existing student's details
    def update_student(self):
        student_id = input("Enter student ID to update: ")
        # Check if the student exists
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        student = self.students[student_id]
        print("Leave input empty to keep current value.")
        # Prompt user to update each field, using the existing value if left blank
        name = input(f"New name [{student['name']}]: ") or student['name']
        age = input(f"New age [{student['age']}]: ") or student['age']
        course = input(f"New course [{student['course']}]: ") or student['course']

        # Update the student details
        self.students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }
        # Save the updated student data
        self.save_students()
        print("✅ Student updated successfully!")

    # Delete a student from the system
    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        # Check if student exists
        if student_id in self.students:
            del self.students[student_id]  
            self.save_students()  
            print("✅ Student deleted.")
        else:
            print("❌ Student not found.")

    # Export student data to a CSV file
    def export_to_csv(self, csv_filename='students.csv'):
        if not self.students:
            print("📭 No students to export.")
            return

        # Open the CSV file for writing
        with open(csv_filename, mode='w', newline='') as file:
            # Create a CSV writer object, specifying the column headers
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Age", "Course"])
            writer.writeheader()  
            # Write each student's data as a new row in the CSV
            for student_id, data in self.students.items():
                writer.writerow({
                    "ID": student_id,
                    "Name": data["name"],
                    "Age": data["age"],
                    "Course": data["course"]
                })
        print(f"✅ Data exported successfully to '{csv_filename}'!")

    # Import student data from a CSV file
    def import_from_csv(self, csv_filename='students.csv'):
        if not os.path.exists(csv_filename):
            print("❌ CSV file not found.")
            return

        # Open the CSV file for reading
        with open(csv_filename, mode='r') as file:
            reader = csv.DictReader(file)
            count = 0
            # Read each row from the CSV and add it to the students dictionary
            for row in reader:
                student_id = row.get("ID")
                # Add only new students (avoiding duplicates)
                if student_id and student_id not in self.students:
                    self.students[student_id] = {
                        "name": row.get("Name", ""),
                        "age": row.get("Age", ""),
                        "course": row.get("Course", "")
                    }
                    count += 1
            self.save_students()
            print(f"✅ {count} students imported successfully from '{csv_filename}'!")

    # Exit the application
    def exit_app(self):
        print("👋 Exiting the app. Goodbye!")  
        exit()  

    # Main function that runs the CLI application and takes user input to perform actions
    def run(self):
        operations = {
            '1': self.add_student,
            '2': self.view_students,
            '3': self.update_student,
            '4': self.delete_student,
            '5': self.exit_app,
            '6': self.export_to_csv,
            '7': self.import_from_csv,
        }

        while True:
            print("\n📚 Student Management CLI App")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            print("6. Export to CSV")
            print("7. Import from CSV")

            choice = input("Choose an option (1-7): ")
            action = operations.get(choice)

            # Execute the corresponding action or display an error message
            if action:
                action()
            else:
                print("❌ Invalid option. Please choose between 1 and 7.")

# Execute the app if this file is run directly
if __name__ == "__main__":
    app = StudentManagementApp()  # Create an instance of the app
    app.run()  # Start the app's main loop

