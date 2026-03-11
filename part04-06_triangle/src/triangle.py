# Copy here code of line function from previous exercise
def line(l, text):
    if not text:
        text = "*"
    text = text[0]

    print(text * l)

def triangle(size):
    # You should call function line here with proper parameters
    limit = 1
    while limit <= size:
        line(limit, "#")
        limit += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
