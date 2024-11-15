'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes,mostre a mensagem correspondente “Impossivel calcular”,caso haja uma divisão por 0 ou raiz de numero negativo.

Imprima o resultado das raízes com 5 dígitos após o ponto
'''
#importar a biblioteca math para calc a raiz quadrada

import math

A, B, C = map(float, input(": ").split())

if A == 0 : #se A for 0, a conta toda deixará de ser Bhaskara
    print("Impossivel calcular")
else:
    delta = (B**2)-(4*A*C)#calcular o Delta

    if delta < 0 :#se o delta for menor que 0 (NEGATIVO) o calculo tbm dará errado
        print("Impossivel calcular")
    else:
        X1 = (-B + math.sqrt(delta)) / (2*A)
        X2 = (-B - math.sqrt(delta)) / (2*A)
        
        print(f'R1 = {X1:.5f}')#5f pq o programa quer com 5 casas decimais 
        print(f'R2 = {X2:.5f}')