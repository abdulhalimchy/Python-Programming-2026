# Write your solution here
nums = int(input("How many items: "))
items = []

for i in range(nums):
    item = int(input(f"Item {i+1}: "))
    items.append(item)

print(items)