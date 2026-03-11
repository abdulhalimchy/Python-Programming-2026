# Write your solution here
def most_common_character(text):
    chars = list(text)

    mc = chars[0]
    mx_cnt = 0

    for c in chars:
        cnt = chars.count(c)
        if cnt > mx_cnt:
            mx_cnt =cnt
            mc = c
    
    return mc


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))