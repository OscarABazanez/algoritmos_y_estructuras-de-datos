from collections import Counter


def chunk(array,size):

    # solucion 1
    chunked_list = []
    i = 0
    while i < len(array):
        if i % size == 0:
            chunked_list.append([])
        chunked_list[len(chunked_list)-1].append(array[i])
        i = i + 1
    return chunked_list 


# print(chunk([1, 2, 3, 4], 2))
# print(chunk([1, 2, 3, 4, 5], 2))


