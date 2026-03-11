# Write your solution here

items = []

print("The list is now []")

while True:
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "x":
        print("Bye!")
        break
    if operation == "d":
        items.append(len(items)+1)
    else:
        items.pop()

    print(f"The list is now {items}")
    
