import json
import os
from src.student import Student

class StudentManagementSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        # This dictionary will hold all students. 
        # Key will be Student ID, Value will be the Student Object.
        self.students = {}
        
        # Load any existing data as soon as the system starts
        self.load_data()

    def load_data(self):
        """Reads student data from the JSON file."""
        # Check if the file exists using the os module
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                # Load the raw dictionary from the file
                file_data = json.load(file)
                
                # Convert the raw data back into proper Student Objects
                for student_id, info in file_data.items():
                    saved_student = Student(
                        student_id=student_id,
                        name=info["name"],
                        age=info["age"],
                        grade=info["grade"],
                        courses=info["courses"]
                    )
                    # Add it to our internal dictionary
                    self.students[student_id] = saved_student
        else:
            # If the file doesn't exist yet, just start with an empty dictionary
            self.students = {}

    def save_data(self):
        """Saves current student data back to the JSON file."""
        output_dictionary = {}
        
        # Loop through all our student objects and convert them to dictionaries
        for student_id, student_object in self.students.items():
            output_dictionary[student_id] = student_object.to_dict()
            
        with open(self.file_path, "w") as file:
            # json.dump writes the dictionary into the file. indent=4 makes it pretty to read!
            json.dump(output_dictionary, file, indent=4)
        print("Data saved successfully!")

    def add_student(self, student_id, name, age, grade):
        """Creates and adds a new student."""
        # Check if the ID already exists
        if student_id in self.students:
            print("Error: A student with this ID already exists!")
            return False
        
        # Create a new Student object using our class
        new_student = Student(student_id, name, age, grade)
        
        # Add it to our storage dictionary
        self.students[student_id] = new_student
        print(f"Student {name} added successfully!")
        return True

    def view_all_students(self):
        """Displays all students."""
        if len(self.students) == 0:
            print("No students found in the system.")
            return
        
        print("\n--- Student List ---")
        for student_id, student_object in self.students.items():
            print(student_object)
        print("---------------------\n")

    def search_student(self, student_id):
        """Searches for a single student by ID."""
        if student_id in self.students:
            student_object = self.students[student_id]
            print("\nStudent Found:")
            print(student_object)
            return student_object
        else:
            print("Student not found.")
            return None

    def delete_student(self, student_id):
        """Removes a student from the system."""
        if student_id in self.students:
            # pop removes the item from the dictionary
            self.students.pop(student_id)
            print("Student records deleted successfully.")
            return True
        else:
            print("Error: Student ID not found.")
            return False