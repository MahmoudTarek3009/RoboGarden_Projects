class Student:
    def __init__(self, name, age, grades):
        # Initialize student with name, age, and a list of grades
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        # Method to display the student's information
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def average_grade(self):
        # Method to calculate the average grade of the student
        if len(self.grades) == 0:
            return 0  # Avoid division by zero if no grades are available
        return sum(self.grades) / len(self.grades)


class StudentDatabase:
    def __init__(self):
        # Initialize the student database as an empty list
        self.students = []

    def add_student(self, name, age, grades):
        # Method to add a new student to the database
        student = Student(name, age, grades)
        self.students.append(student)

    def display_all_students(self):
        # Method to display all students in the database
        if not self.students:
            print("No students in the database.")
        else:
            for student in self.students:
                student.display_info()
                print(f"Average Grade: {student.average_grade()}\n")


# Main function to simulate a simple interaction with the student database system
def main():
    # Create an instance of StudentDatabase
    database = StudentDatabase()

    # Example scenario: Adding students to the database
    database.add_student("Alice", 20, [85, 90, 92])
    database.add_student("Bob", 22, [78, 80, 85, 88])

    # Display all students and their information
    print("Student Database Informati")
