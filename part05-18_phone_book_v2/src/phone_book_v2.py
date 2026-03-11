# Write your solution here
# Write your solution here
def add():
    name = input("name: ")
    number = input("number: ")
    
    if name not in phone_book:
        phone_book[name] = []
    phone_book[name].append(number)
    print("ok!")
    
def search():
    name = input("name: ")
    if name in phone_book:
        for number in phone_book[name]:
            print(number)
    else:
        print("no number")
    

phone_book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    
    if command == 1:
        search()
    elif command == 2:
        add()

# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...