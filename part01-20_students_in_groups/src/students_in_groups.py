# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
num_of_group = students // group_size + (students % group_size > 0)
print(f"Number of groups formed: {num_of_group}")