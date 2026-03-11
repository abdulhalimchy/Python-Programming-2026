# Write your solution here
password = input("Password: ")

while True:
    password_again = input("Repeat password: ")
    if password == password_again:
        print("User account created!")
        break
    else:
        print("They do not match!")