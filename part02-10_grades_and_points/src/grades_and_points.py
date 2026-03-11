# Write your solution here
points = int(input("How many points [0-100]: "))
if points > 100 or points < 0:
    grade = "impossible!"
elif points <= 49:
    grade = "fail"
else:
    if points == 100:
        points -= 1
    grade = (points // 10) - 4

print("Grade:", grade)