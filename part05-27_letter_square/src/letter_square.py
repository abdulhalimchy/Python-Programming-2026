# Write your solution here
layers = int(input("Layers: "))

size = (layers * 2) - 1  # total layers
for i in range(size):
    row = ""
    for j in range(size):
        layer = max(abs(i - (layers - 1)), abs(j - (layers - 1)))
        char = chr(ord('A') + layer)
        row += char
    print(row)