def insercion(lista):
    for numero in range(0,len(lista)-1):
        if lista[numero]>lista[numero+1]:
            temp=lista[numero+1]
            lista[numero+1]=lista[numero]
            for numero2 in range(numero-1,0,-1):
                if temp> lista[numero2]:
                    lista[numero2+1]=temp
                    break
                else:
                    lista[numero2+1]=lista[numero2]
    return lista
lista=[0,1,3,2,5,4,7,6,9,8]
lista=insercion(lista)  
print(lista)                  



