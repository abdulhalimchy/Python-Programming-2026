# Write your solution here:
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def tick(self):
        seconds = self.seconds + 1
        self.seconds = seconds % 60
        
        minutes = seconds // 60 + self.minutes
        self.minutes = minutes % 60
        
        hours = minutes // 60 + self.hours
        self.hours = hours % 24
        
    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

        
    def __str__(self):
        watch = ""
        if self.hours < 10:
            watch += "0"
        watch += f"{self.hours}:"
        
        if self.minutes < 10:
            watch += "0"
        watch += f"{self.minutes}:"
        
        if self.seconds < 10:
            watch += "0"
        
        watch += f"{self.seconds}"
        
        return watch
        
        
        

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)