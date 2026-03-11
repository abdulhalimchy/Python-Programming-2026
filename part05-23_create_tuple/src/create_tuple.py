# Write your solution here

def create_tuple(x: int, y: int, z: int):
    l = sorted([x, y, z])
    
    return (l[0], l[2], x+y+z)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))