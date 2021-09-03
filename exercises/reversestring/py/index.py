from functools import reduce

def reverse(str):
    # Solucion 1
    string = str[::-1]
    # return string

    # Solucion 2
    string = ''.join(reversed(str))
    # return string

    # Solucion 3
    string = ''
    for i in str:
        string = string + i
    # return string

    # Solucion 4
    string = reduce(lambda original,rever: rever + original, str)
    return string


