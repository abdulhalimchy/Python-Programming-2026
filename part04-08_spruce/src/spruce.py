# Write your solution here
# You can test your function by calling it within the following block

def spruce(size):
    print("a spruce!")
    stars = 1
    limit = size*2-1
    while stars <= limit:
        spaces = (limit-stars) // 2
        if spaces:
            print(" " * spaces, end="")
        
        print("*" * stars)
        stars += 2
    
    print(" " * (limit // 2), end="")
    print("*")

if __name__ == "__main__":
    spruce(5)