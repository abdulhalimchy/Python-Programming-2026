# Write your solution here
# You can test your function by calling it within the following block
def line(l, text):
    if not text:
        text = "*"
    text = text[0]

    print(text * l)


if __name__ == "__main__":
    line(5, "x")