# Copy here code of line function from previous exercise and use it in your solution
def line(l, text):
    if not text:
        text = "*"
    text = text[0]

    print(text * l)

def triangle(size, char):
    row = 1
    while row <= size:
        line(row, char)
        row += 1

def rectangle(width, height, char):
    while height:
        line(width, char)
        height -= 1

def shape(width, tri_char, height, rec_char):
    triangle(width, tri_char)
    rectangle(width, height, rec_char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")