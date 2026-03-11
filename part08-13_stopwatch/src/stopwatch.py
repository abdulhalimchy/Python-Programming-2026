# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        
    def tick(self):
        seconds = self.seconds + 1
        self.seconds = seconds % 60
        
        minutes = seconds // 60 + self.minutes
        self.minutes = minutes % 60
        
    def __str__(self):
        watch = ""
        if self.minutes < 10:
            watch += "0"
        watch += f"{self.minutes}:"
        
        if self.seconds < 10:
            watch += "0"
        
        watch += f"{self.seconds}"
        
        return watch
        
        
        

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()