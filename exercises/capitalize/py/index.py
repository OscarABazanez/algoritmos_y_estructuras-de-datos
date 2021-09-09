
def capital(str):

    # solucion 1
    str = str.lower().split(" ")
    resultado = []
    for i in range(len(str)):
        resultado.append(str[i][0].capitalize() + str[i][1::])
    return ' '.join(resultado)


print(capital('a sHort centence'))



