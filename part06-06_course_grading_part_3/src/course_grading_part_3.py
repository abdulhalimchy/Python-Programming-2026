# write your solution here
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

# student_file = "students1.csv"
# exercise_file = "exercises1.csv"
# exam_file = "exam_points1.csv"

students = {}

# Read student names
with open(student_file) as f:
    next(f)
    for line in f:
        parts = line.strip().split(";")
        students[parts[0]] = parts[1] + " " + parts[2]

# Read exercise data
exercise_count = {}
with open(exercise_file) as f:
    next(f)
    for line in f:
        parts = line.strip().split(";")
        student_id = parts[0]
        
        exercises = 0
        for x in parts[1:]:
            exercises += int(x)
            
        points = exercises // 4
        exercise_count[student_id] = exercises

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

print()
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")


for student_id in students:
    name = students[student_id]
    exec_nbr = exercise_count[student_id]
    exec_pts = exec_nbr // 4
    exm_pts = exam_points[student_id]
    total = exec_pts + exm_pts

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

    print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{total:<10}{grade:<10}")