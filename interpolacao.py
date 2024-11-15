
"""Interpolação básica de strings
s - string
d/i - int
f - float
x (para minusculo) e  X (para maisculo) - Hexadecimal (ABCDEF0123456789) a-f e 0-9
usar o % para chamar as varias e substituir as letras
para fazer formatação com fstring %.2f - duas casas decimais
"""
nome = 'Luiz'
preco = 1000.9587643
variavel = '%s, o preço é R$%.2f'% (nome, preco)
print(variavel)
print('O hexadecimal de %i é %04X' %(1500,1500))
