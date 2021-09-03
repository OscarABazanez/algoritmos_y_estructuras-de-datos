from functools import reduce


def palindrome(str):
    # Solucion 1
    result = str.replace(' ','').lower()
    # return str == result[::-1]

    # Solucion 2
    result = ''.join(reversed(str))
    # return result == result[::-1]
    
    # Solucion 3
    # result = reduce(lambda rever, original: rever + original, str)

    # Solucion 3
    r = ''
    for i in str:
        r = r+i
    # return result == result[::-1]

    # Solucion 4
    if len(str) == 0:
        return str
    return palindrome(str[1:]) + str[0]


print(palindrome("abba"))
print( palindrome("abcdefg"))

