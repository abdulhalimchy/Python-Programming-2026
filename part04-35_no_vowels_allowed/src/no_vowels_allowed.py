# Write your solution here
def no_vowels(my_string):
    my_string = my_string.replace("o", "")
    my_string = my_string.replace("a", "")
    my_string = my_string.replace("e", "")
    my_string = my_string.replace("i", "")
    my_string = my_string.replace("u", "")

    return my_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))