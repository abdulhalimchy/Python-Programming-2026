# Write your solution here
l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")

mid = ""

if (l1>l2 and l1<l3) or (l1>l3 and l1<l2):
    mid = l1
elif (l2>l1 and l2<l3) or (l2>l3 and l2<l1):
    mid = l2
elif (l3>l1 and l3<l2) or (l3>l2 and l3<l1):
    mid = l3

if mid:
    print(f"The letter in the middle is {mid}")