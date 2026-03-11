# write your solution here
text = input("Write text: ")


words = []
with open("wordlist.txt") as file:
    for line in file:
        words.append(line.strip().lower())

result = []
for word in text.split():
    if word.lower() in words:
        result.append(word)
    else:
        result.append("*" + word + "*")


for word in result:
    print(f"{word} ", end="")