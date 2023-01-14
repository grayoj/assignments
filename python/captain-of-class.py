# Gerald Maduabuchi, 2023
# Create a program that collects the names of students in a class
# and identifies “captain” of the football team

# Create and empty array to collect students in an array.
students = []

# Retrieve the names of students in the class
# While Loop
while True:
    student_name = input(
        "Enter the name of a student in the class, or end the program by pressing 'q' : ")
    # Exit program
    if student_name == 'q':
        break
    students.append(student_name)

# Identify the captain of the football team
captain = input("Enter the name of the football team captain:")
