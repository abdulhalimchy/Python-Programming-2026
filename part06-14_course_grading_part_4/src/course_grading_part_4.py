# tee ratkaisu tänne
# write your solution here
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
course_file = input("Course information: ")

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

# Read course information
with open(course_file) as f:
    line1 = f.readline().strip().split(": ")
    line2 = f.readline().strip().split(": ")

course_name = line1[1]
credits = line2[1]

# Open result files
txt = open("results.txt", "w")
csv = open("results.csv", "w")

# Write header to results.txt
txt.write(f"{course_name}, {credits} credits\n")
txt.write("======================================\n")
txt.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")

# Process students
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

    txt.write(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{total:<10}{grade:<10}\n")
    csv.write(f"{student_id};{name};{grade}\n")

txt.close()
csv.close()

print("Results written to files results.txt and results.csv")