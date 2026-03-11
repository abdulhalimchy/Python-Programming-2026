# Write your solution here
def longest(strings: list):
    ans = ""

    for s in strings:
        if len(s) > len(ans):
            ans = s

    return ans

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

    strings = ["hi", "hiya", "hello", "c", "a"]
    print(longest(strings))

    strings = ["aassssssssdhi", "hziya", "hello", "howdydoody", "zzzzzzzzzzzzzzzzzz"]
    print(longest(strings))