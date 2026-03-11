# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(s: str):
    is_palindrome = True
    i, j = 0, len(s)-1

    while i<=j:
        if s[i]!=s[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
        
    return is_palindrome
        
    

while True:
    s = input("Please type in a palindrome: ")
    if palindromes(s):
        print(f"{s} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

