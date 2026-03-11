# Write your solution here

def add_student(students: dict, name: str):
    if name not in students:
        students[name] = [] # later will store course information
        
    
def add_course(students: dict, name: str, course: tuple):
    if course[1] == 0:
        return
    
    if name in students:
        existing_courses = students[name]
        already_done_course = None
        
        for c in existing_courses:
            if c[0] == course[0]: # checking name
                already_done_course = c
                break
        
        
        if already_done_course: # Check better grade or ignor
            if already_done_course[1] < course[1]:  # better grade
                existing_courses.remove(already_done_course)
                existing_courses.append(course)
        else: # Newly completed
            existing_courses.append(course)

       
def get_avg_grade(courses: list):
    total_grade = 0
    for c in courses:
        total_grade += c[1]
        
    return total_grade / len(courses)

def print_courses(courses: list):
    print(f" {len(courses)} completed courses:")
    for c in courses:
        print(f"  {c[0]} {c[1]}")  # name, grade


def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        
        courses = students[name]
        if len(courses) == 0:
            print(" no completed courses")
        else:
            print_courses(courses)
            print(f" average grade {get_avg_grade(courses)}")
    else:
        print(f"{name}: no such person in the database")
        
def summary(students: dict):
    most_comp = 0
    most_comp_by = None
    best_grade = 0
    best_grade_by = None
    
    for name, courses in students.items():
        if len(courses) > most_comp:
            most_comp = len(courses)
            most_comp_by = name
            
        avg_grade = get_avg_grade(courses)
        if avg_grade > best_grade:
            best_grade = avg_grade
            best_grade_by = name
    
    print(f"students {len(students)}")
    print(f"most courses completed {most_comp} {most_comp_by}") 
    print(f"best average grade {best_grade} {best_grade_by}") 


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Eliza")
    
    summary(students)