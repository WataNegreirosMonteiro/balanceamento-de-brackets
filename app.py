def balancear(texto):
    tamanho = len(texto)
    
    indice = 0
    for caracter in texto:

        if (caracter == '{'):
            par = '}'
        elif (caracter == '('):
            par = ')'
        else:
            par = ']'

       
        print(texto[tamanho - indice-1] == par)

        indice += 1

        if (indice == tamanho/2):
            break

    
    print(texto)

balancear('[{()}]')

