# Write your solution here
# You can test your function by calling it within the following block

def same_chars(text, i, j):
    if i >= len(text) or j>= len(text):
        return False
    return text[i] == text[j]

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))