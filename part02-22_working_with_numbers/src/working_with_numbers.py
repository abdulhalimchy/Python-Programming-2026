# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")

count, pos_count, neg_count, summ = 0, 0, 0, 0

while True:
    num = int(input("Number: "))

    if num == 0:
        break

    count += 1
    summ += num
    if num > 0:
        pos_count += 1
    if num < 0:
        neg_count += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {summ}")
print(f"The mean of the numbers is {summ/count}")
print(f"Positive numbers {pos_count}")
print(f"Negative numbers {neg_count}")