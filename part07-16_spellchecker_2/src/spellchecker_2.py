# Write your solution here
import difflib

# load dictionary
with open("wordlist.txt") as f:
    words = [line.strip() for line in f]

dictionary = set(words)

text = input("write text: ")
parts = text.split()

misspelled = []

result = []

for word in parts:
    if word.lower() in dictionary:
        result.append(word)
    else:
        result.append(f"*{word}*")
        misspelled.append(word)

print()
print(" ".join(result))

print("suggestions:")
for word in misspelled:
    suggestions = difflib.get_close_matches(word.lower(), words)
    print(f"{word}: {', '.join(suggestions)}")