import os

# Function to input grades and store them in a file
def input_grades():
    grades = []
    while True:
        try:
            # Ask the user to input grades
            grade = input("Enter a grade for the subject (or type 'done' to finish): ")
            if grade.lower() == 'done':
                break
            # Convert the grade to a float
            grade = float(grade)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a valid numeric grade or 'done' to finish.")
    return grades

# Function to calculate the average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Function to store grades in a file
def store_grades(grades, filename="grades.txt"):
    try:
        with open(filename, "a") as file:
            for grade in grades:
                file.write(f"{grade}\n")
    except Exception as e:
        print(f"An error occurred while saving the grades: {e}")

# Function to read grades from a file
def read_grades(filename="grades.txt"):
    grades = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    try:
                        grade = float(line.strip())  # Convert each line to a float
                        grades.append(grade)
                    except ValueError:
                        print(f"Invalid grade value in file: {line.strip()}")
        except Exception as e:
            print(f"An error occurred while reading the grades: {e}")
    else:
        print(f"The file {filename} does not exist.")
    return grades

# Main function to interact with the user
def main():
    print("Welcome to the Student Grade Tracker")
    
    # Read existing grades from the file
    grades = read_grades()
    print("\nCurrent grades from the file:")
    if grades:
        print(grades)
    else:
        print("No grades found in the file.")

    # Get new grades from the user and store them
    new_grades = input_grades()
    store_grades(new_grades)
    
    # Update the grades list
    grades.extend(new_grades)
    
    # Calculate and display the average grade
    if grades:
        average = calculate_average(grades)
        print(f"\nThe average grade is: {average:.2f}")
    else:
        print("\nNo grades entered, cannot calculate average.")

if __name__ == "__main__":
    main()
