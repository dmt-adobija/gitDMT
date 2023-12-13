def isDigit(x):
    if(x == '1'):
        return True
    elif(x == '2'):
        return True
    elif(x == '3'):
        return True
    elif(x == '4'):
        return True
    elif(x == '5'):
        return True
    elif(x == '6'):
        return True
    elif(x == '7'):
        return True
    elif(x == '8'):
        return True
    elif(x == '9'):
        return True
    elif(x == '0'):
        return True
    else:
        return False


nrTelefonu = input("Podaj numer telefonu")
tab = []
output = "Poprawny"
if (len(nrTelefonu) == 9):
    for i in range(0, 9):
        if(isDigit(nrTelefonu[i])):
            continue
        else:
            output = "Niepoprawny"
            break
else:
    output = "Niepoprawny"
print(output)