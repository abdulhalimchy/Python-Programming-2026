# write your solution here
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

students = {}

# Read student names
with open(student_file) as f:
    next(f)
    for line in f:
        parts = line.strip().split(";")
        students[parts[0]] = parts[1] + " " + parts[2]

# Read exercise data
exercise_points = {}
with open(exercise_file) as f:
    next(f)
    for line in f:
        parts = line.strip().split(";")
        student_id = parts[0]
        
        exercises = 0
        for x in parts[1:]:
            exercises += int(x)
            
        points = exercises // 4
        exercise_points[student_id] = points

# Read exam data
exam_points = {}
with open(exam_file) as f:
    next(f)
    for line in f:
        parts = line.strip().split(";")
        student_id = parts[0]
        
        points = 0
        for x in parts[1:]:
            points += int(x)
        
        exam_points[student_id] = points

# Calculate grades
for student_id in students:
    total = exercise_points[student_id] + exam_points[student_id]

    if total <= 14:
        grade = 0
    elif total <= 17:
        grade = 1
    elif total <= 20:
        grade = 2
    elif total <= 23:
        grade = 3
    elif total <= 27:
        grade = 4
    else:
        grade = 5

    print(students[student_id], grade)