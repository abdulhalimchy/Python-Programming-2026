# Write your solution here

def list_sum(a, b):
    for i in range(len(a)):
        a[i] += b[i]
    return a

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]