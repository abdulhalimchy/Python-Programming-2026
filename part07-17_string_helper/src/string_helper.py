# Write your solution here
import string

def change_case(orig_string: str) -> str:
    result = ""
    for char in orig_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result


def split_in_half(orig_string: str) -> tuple:
    middle = len(orig_string) // 2
    return (orig_string[:middle], orig_string[middle:])


def remove_special_characters(orig_string: str) -> str:
    allowed = string.ascii_letters + string.digits + " "
    result = ""

    for char in orig_string:
        if char in allowed:
            result += char

    return result


if __name__ == "__main__":
    test = "Well hello there!"
    print(change_case(test))

    p1, p2 = split_in_half(test)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)