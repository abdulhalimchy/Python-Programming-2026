# Write your solution here
def filter_solutions():
    corrects = []
    incorrects = []
    
    with open("solutions.csv") as solutions:
        
        for line in solutions:
            line = line.strip()
            name, problem, result = line.split(";")
            result = int(result)

            if "+" in problem:
                a, b = problem.split("+")
                answer = int(a) + int(b)
            else:
                a, b = problem.split("-")
                answer = int(a) - int(b)

            if answer == result:
                corrects.append(line)
            else:
                incorrects.append(line)
                
    with open("correct.csv", "w") as correct:
        for line in corrects:
            correct.write(line + "\n")
      
    with open("incorrect.csv", "w") as incorrect:
        for line in incorrects:
            incorrect.write(line + "\n")
        