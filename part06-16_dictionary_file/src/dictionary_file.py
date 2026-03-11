# Write your solution here
dictionary = []

# read existing entries
with open("dictionary.txt") as file:
    for line in file:
        finnish, english = line.strip().split(";")
        dictionary.append((finnish, english))



while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")

    if function == "1":
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")

        dictionary.append((finnish, english))

        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish};{english}\n")

        print("Dictionary entry added")

    elif function == "2":
        term = input("Search term: ")

        for finnish, english in dictionary:
            if term in finnish or term in english:
                print(f"{finnish} - {english}")

    elif function == "3":
        print("Bye!")
        break