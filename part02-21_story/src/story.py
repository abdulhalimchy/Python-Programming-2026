# Write your solution here

prev_word = ""
story = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or prev_word == word:
        break;
    
    if len(story):
        story += " "
    story += word
    prev_word = word

print(story)
