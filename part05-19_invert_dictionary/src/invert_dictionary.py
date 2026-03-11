# Write your solution here
def invert(d: dict):
    new_d = {}
    for key, value in d.items():
        new_d[key] = value
    
    d.clear()
    for key, value in new_d.items():
        d[value] = key
    
    new_d.clear()

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)