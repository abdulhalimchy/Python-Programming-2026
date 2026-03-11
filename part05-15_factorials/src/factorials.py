# Write your solution here

def fact(n: int):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def factorials(n: int):
    k = {}
    for i in range(1, n+1):
        k[i] = fact(i)
    
    return k

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])