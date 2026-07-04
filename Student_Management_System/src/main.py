import os
from src.system import StudentManagementSystem

def display_menu():
    """Prints the available choices for the user."""
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Enroll Student in a Course")
    print("5. Delete Student Record")
    print("6. Save and Exit")
    print("=======================================")

def main():
    # Define where to save the data file. 
    # We will save it in a folder named 'data' as 'students.json'
    data_directory = "data"
    file_path = os.path.join(data_directory, "students.json")
    
    # Simple check: Make sure the 'data' directory exists on your computer
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    # Initialize our system core engine
    system = StudentManagementSystem(file_path)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Add New Student ---")
            student_id = input("Enter Unique Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            
            # Use try-except to safely handle age input
            try:
                age = int(input("Enter Student Age: "))
            except ValueError:
                print("Error: Age must be a valid whole number!")
                continue # Skips the rest of the loop and goes back to the menu
                
            grade = input("Enter Student Grade (e.g., A, B, C): ").strip()
            
            # Send the data to our system engine
            system.add_student(student_id, name, age, grade)
            
        elif choice == "2":
            system.view_all_students()
            
        elif choice == "3":
            print("\n--- Search Student ---")
            student_id = input("Enter Student ID to search: ").strip()
            system.search_student(student_id)
            
        elif choice == "4":
            print("\n--- Enroll in a Course ---")
            student_id = input("Enter Student ID: ").strip()
            
            # First, check if the student actually exists
            student = system.search_student(student_id)
            if student != None:
                course_name = input("Enter Course Name to add: ").strip()
                # Run the enroll function from our Student class object
                if student.enroll_course(course_name):
                    print(f"Successfully enrolled in {course_name}!")
            
        elif choice == "5":
            print("\n--- Delete Student ---")
            student_id = input("Enter Student ID to delete: ").strip()
            system.delete_student(student_id)
            
        elif choice == "6":
            print("\nSaving data and closing the system...")
            system.save_data()
            print("Goodbye!")
            break # Breaks the infinite loop, ending the program
            
        else:
            print("Invalid choice! Please select a valid number between 1 and 6.")

# This line ensures the main function runs only when you execute this file directly
if __name__ == "__main__":
    main()