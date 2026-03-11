# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if self.get_sum() == 0:
            return 0
        return self.get_sum() / self.count_numbers()


numStats = NumberStats()
evenNumStats = NumberStats()
oddNumStats = NumberStats()

while True:
    n = int(input("Please type in integer numbers: "))
    if n == -1:
        break
    
    numStats.add_number(n)
    
    if n % 2 == 1:
        oddNumStats.add_number(n)
    else:
        evenNumStats.add_number(n)

print(f"Sum of numbers: {numStats.get_sum()}")
print(f"Mean of numbers: {numStats.average()}")
print(f"Sum of even numbers: {evenNumStats.get_sum()}")
print(f"Sum of odd numbers: {oddNumStats.get_sum()}")
    