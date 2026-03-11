# write your solution here
# write your solution here

def read_fruits():
    fruits_dict = {}

    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits_dict[parts[0]] = float(parts[1])

    return fruits_dict

if __name__ == "__main__":
    print(read_fruits())