def IsBracesValid(string):
    bracesStack = []
    for i in string:
        if i == "(":
            bracesStack.append(i)
        elif i == ")":
            if len(bracesStack) == 0:
                return False
            else:
                bracesStack.pop()
    if len(bracesStack) == 0:
        return True
    else:
        return False

string = input("Введите строку, содержащую скобки для ее проверки: ")

print(IsBracesValid(string))
