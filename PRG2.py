from collections import namedtuple

# Define a namedtuple to represent each student's data
Student = namedtuple('Student', ['ID', 'MARKS', 'CLASS', 'NAME'])

if __name__ == "__main__":
    # Input the number of students
    num_students = int(input())

    # Input the column names in any order
    columns = input().split()

    # Find the index of each column
    id_index = columns.index('ID')
    marks_index = columns.index('MARKS')
    class_index = columns.index('CLASS')
    name_index = columns.index('NAME')

    # Initialize a variable to store the total marks
    total_marks = 0

    # Input the data for each student and calculate the total marks
    for _ in range(num_students):
        student_data = input().split()
        student = Student(ID=int(student_data[id_index]),
                          MARKS=int(student_data[marks_index]),
                          CLASS=student_data[class_index],
                          NAME=student_data[name_index])
        total_marks += student.MARKS

    # Calculate the average marks and print it to 2 decimal places
    average_marks = total_marks / num_students
    print("{:.2f}".format(average_marks))
