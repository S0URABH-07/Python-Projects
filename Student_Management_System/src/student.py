class Student:
    def __init__(self, student_id, name, age, grade, courses=None):
        # Setting up the student's information using simple variables
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        
        # Simple condition: if no courses list is given, create an empty one
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def enroll_course(self, course_name):
        # Check if the course is already in our list
        if course_name in self.courses:
            print("Student is already enrolled in this course!")
            return False
        else:
            # If it's a new course, add it to the list
            self.courses.append(course_name)
            return True

    def to_dict(self):
        # Convert our object data into a simple dictionary
        # This makes it easy to save into a file later
        student_dictionary = {
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "courses": self.courses
        }
        return student_dictionary

    def __str__(self):
        # Return a simple, easy-to-read line of text about the student
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Courses: {self.courses}"