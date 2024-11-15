"""
Fatiamento de strings
posição do indice 

fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caract. da string

P = Passos - define quantos em quantos ele vai pular, normalmente é de 1 em 1
"""
variavel ='olá mundo'
print(variavel[-4]) 
print(variavel[4:])
print(variavel[-8:-2])

resultado = 'reprovado'
print(len(resultado)) 
#Metodo len - length pega o tamanho do indice
print(resultado[0:len(resultado):2])
#Igual a print(resultado [0:9:2])
print (resultado [0:9:2])


