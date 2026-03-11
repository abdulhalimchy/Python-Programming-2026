# Write your solution here
def filter_incorrect():
    lottery_numbers = open("lottery_numbers.csv")
    correct_numbers = open("correct_numbers.csv", "w")

    for line in lottery_numbers:
        line = line.strip()

        try:
            week_part, numbers_part = line.split(";")

            # check week format
            week_word, week_number = week_part.split()
            if week_word != "week":
                continue
            week_number = int(week_number)

            numbers = numbers_part.split(",")

            if len(numbers) != 7:
                continue

            nums = []
            for n in numbers:
                num = int(n)
                if num < 1 or num > 39:
                    raise ValueError
                nums.append(num)

            if len(set(nums)) != 7:
                continue

            correct_numbers.write(line + "\n")

        except:
            continue

    lottery_numbers.close()
    correct_numbers.close()