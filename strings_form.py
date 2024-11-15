"""(Caractere) (><^) (quantidade)
> - esquerda
< - direita
^ - centro
= - Força os números a aparecerem antes do zero
Sinal -+ ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.5086445:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500: 08x}')
print(f'{1000.45785455478659:,.1f}')