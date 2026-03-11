# Write your solution here
import string

def get_default_variables():
    default_vars = {}
    location_dict = {}
    
    for v in string.ascii_uppercase:
        default_vars[v] = 0
    return default_vars

def get_integer_value(identifier: str, default_vars: dict):
    try:
        value = int(identifier)
        return value
    except:
        return default_vars[identifier]
        

def get_location_index(location: str, program: list):
    for i in range(len(program)):
        if program[i].startswith(location):
            return i
    return None

def is_condition_true(v1: int, v2: int, operator):
    if operator == "==":
        return v1 == v2
    if operator == "!=":
        return v1 != v2
    if operator == ">":
        return v1 > v2
    if operator == ">=":
        return v1 >= v2
    if operator == "<":
        return v1 < v2
    if operator == "<=":
        return v1 <= v2
    
        

def run(program: list):
    default_vars = get_default_variables()
    result = []
    i = 0
    while i < len(program):
        command = program[i].split(" ")
        i += 1
        # print(command)
        
        if command[0] == "END":
            break
        elif command[0] == "PRINT":
            result.append(get_integer_value(command[1], default_vars))
        elif command[0] == "MOV":
            default_vars[command[1]] = get_integer_value(command[2], default_vars)
        elif command[0] == "ADD":
            default_vars[command[1]] += get_integer_value(command[2], default_vars)
        elif command[0] == "SUB":
            default_vars[command[1]] -= get_integer_value(command[2], default_vars)
        elif command[0] == "MUL":
            default_vars[command[1]] *= get_integer_value(command[2], default_vars)
        elif command[0] == "JUMP":
            i = get_location_index(command[1], program) + 1
        elif command[0] == "IF":
            value1 = get_integer_value(command[1], default_vars)
            value2 = get_integer_value(command[3], default_vars)
            if is_condition_true(value1, value2, command[2]):
                i = get_location_index(command[5], program) + 1
            

    return result
    

# PRINT [value]: prints the value
# MOV [variable] [value]: assigns the value to the variable
# ADD [variable] [value]: adds the value to the variable
# SUB [variable] [value]: subtracts the value from the variable
# MUL [variable] [value]: multiplies the variable by the value
# [location]:: names a line of code, so it can be jumped to from elsewhere
# JUMP [location]: jumps to the location specified
# IF [condition] JUMP [location]: if the condition is true, jump to the location specified
# END: finish execution

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)