from collections import Counter

def anagrams(stringA, stringB):

    # solucion 1
    return sorted(stringA) == sorted(stringB)

print(anagrams('rail safety', 'fairy tales'))
# print(chunk([1, 2, 3, 4], 2))
# print(chunk([1, 2, 3, 4, 5], 2))


