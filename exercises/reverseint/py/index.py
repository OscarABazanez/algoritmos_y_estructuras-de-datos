from functools import reduce

def reverse(number):
    number = str(number)
    # Solucion 1
    if number[0] == '-':
        return '-' +  number[-1:0:-1]
    return number[::-1]

    # # Solucion 2
    # string = ''.join(reversed(str))
    # # return string

    # # Solucion 3
    # string = ''
    # for i in str:
    #     string = string + i
    # # return string

    # # Solucion 4
    # string = reduce(lambda original,rever: rever + original, str)
    # return string
    

print(reverse(15))
print(reverse(-83))
