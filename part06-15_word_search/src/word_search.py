# Write your solution here

def find_words(search_term: str):
    results = []

    with open("words.txt") as file:
        for line in file:
            word = line.strip()

            # exact match
            if "*" not in search_term and "." not in search_term:
                if word == search_term:
                    results.append(word)

            elif "*" in search_term:
                if search_term[0] == "*":
                    s = search_term[1:]
                    if word.endswith(s):
                        results.append(word)

                elif search_term[-1] == "*":
                    s = search_term[:-1]
                    if word.startswith(s):
                        results.append(word)

            # dot wildcard
            else:
                if len(word) != len(search_term):
                    continue

                match = True
                for i in range(len(word)):
                    if search_term[i] == ".":
                        continue
                    if search_term[i] != word[i]:
                        match = False
                        break

                if match:
                    results.append(word)

    return results

if __name__ == "__main__":
    print(find_words("cat"))
    # print(find_words("*cat"))
#     print(find_words("cat*"))
#     print(find_words("p.ng*"))
#     print(find_words(".ng*"))