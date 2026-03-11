# Write your solution here

def get_grade(exam_p, ex_p):
    if exam_p < 10:
        return 0
    points = exam_p + ex_p

    if points >= 28:
        return 5
    elif points >= 24:
        return 4
    elif points >= 21:
        return 3
    elif points >= 18:
        return 2
    elif points >= 15:
        return 1
    else:
         return 0


def main():
    total_student = 0
    total_point = 0
    grade_cnt = [0] * 6

    while True:
        inp = input("Exam points and exercises completed: ")
        if not inp:
            break
    
        exam_p, ex_p = [int(n) for n in inp.split(" ")]
        ex_p = ex_p // 10

        total_point += exam_p + ex_p
        total_student += 1
        grade_cnt[get_grade(exam_p, ex_p)] += 1
    
    print("Statistics:")
    print(f"Points average: {(total_point/total_student):.1f}")
    print(f"Pass percentage: {(((total_student-grade_cnt[0])/total_student) * 100):.1f}")
    print("Grade distribution:")

    # print(grade_cnt)

    for i in range(5, -1, -1):
        print(f"{i}: {'*' * grade_cnt[i]}")
    

main()