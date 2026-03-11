# Copy here code of line function from previous exercise
def line(l, text):
    if not text:
        text = "*"
    text = text[0]

    print(text * l)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    limit = size
    while limit:
        line(size, "#")
        limit -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
