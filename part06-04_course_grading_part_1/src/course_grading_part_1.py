# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}

# Read student information
with open(student_info) as file:
    next(file)  # skip header
    for line in file:
        parts = line.strip().split(";")
        student_id = parts[0]
        first = parts[1]
        last = parts[2]
        students[student_id] = f"{first} {last}"

# Read exercise data and print totals
with open(exercise_data) as file:
    next(file)  # skip header
    for line in file:
        parts = line.strip().split(";")
        student_id = parts[0]
        total_exercises = 0
        for x in parts[1:]:
            total_exercises += int(x)

        print(students[student_id], total_exercises)