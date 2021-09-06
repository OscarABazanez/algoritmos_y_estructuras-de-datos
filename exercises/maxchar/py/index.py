from collections import Counter


def reverse(str):

    # solucion 1
    char_map = {}
    max = 0
    max_char = ''

    for char in str:
        char_map.setdefault(char, 0)
        char_map[char] += 1
    
    for char in char_map:
        if char_map[char] > max:
            max = char_map[char]
            max_char = char

    # return max_char

    # solucion 2
    char_map = {}
    for char in str:
        char_map.setdefault(char,0)
        char_map[char] += 1

    # return max(char_map, key=char_map.get)


    # Solucion 3
    return Counter(str).most_common(1)[0][0]

# print(reverse("abcccccccd"))
# print(reverse("apple 1231111"))
