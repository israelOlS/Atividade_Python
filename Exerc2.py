Curso = "PyThOn"
print(Curso.upper())#Upper deixa MAIUSCULO

print(Curso.lower())#lower deixa minusculo

print(Curso.title())#Deixa a primeira letra Maiuscula 
#-----------------------------------

Teste ="  Python" #Teste de ajuste de espaçamento
print(Teste.strip())#Remove os espaços em branco

print(Teste.lstrip())#Remove os espaço do lado esquerdo L= left
print(Teste.rstrip())#Remoce os espaços do lado direito R= right

#--------------------------------------------------------------------
print(Curso.center(10,'#'))
#adiciona 10 carcacteres(com a ceriavel inclusa) e coloca ela no centro com o elmento '#' em volta
#Curso = Python que tem 6 caracteres ou seja vai incluir mais 4 "#" para dar 10 que foi solicitado
print(Curso.center(20,'!'))

print(".".join(Curso))#Join JUNTA o primeiro caractere inserido para dentro da variavel
print("!".join(Teste))
#Vai passar item a item e incluir o caratere inserido antes do join
