
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Start: {func._name_}")
        result = func(*args, **kwargs)
        print(f"End: {func._name_}\n")
        return result
    return wrapper

# List to store student details
students = []

# Function to add a student
@log
def add_student(name, *marks, **info):
    student = {
        'name': name,
        'marks': marks,
        'info': info
    }
    students.append(student)

# Function to show results
@log
def show_results():
    for s in students:
        print(f"Student: {s['name']}")
        avg = sum(s['marks']) / len(s['marks'])

        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        else:
            grade = 'D'

        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")
        if s['info']:
            print("Extra Info:", s['info'])
        print("-" * 30)

# Adding students
add_student("Sruj", 95, 90, 88, age=21, branch="CSE")
add_student("ayitha", 70, 68, 75)
add_student("kyaa", 55, 60, 58, branch="EEE")

# Showing results
show_results()
