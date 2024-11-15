# -*- coding: utf-8 -*-

notasGeral = int(input())
print(notasGeral)
#notas de 100
notas100 = notasGeral//100
notasGeral = notasGeral%100
#notas de 50 
notas50 = notasGeral//50
notasGeral = notasGeral%50
#notas de 20
notas20 = notasGeral//20
notasGeral = notasGeral%20
#notas de 10
notas10 = notasGeral//10
notasGeral = notasGeral%10
#notas de 5
notas5 = notasGeral//5
notasGeral = notasGeral%5
#notas de 2
notas2 = notasGeral//2
notas1 = notasGeral%2 

print(f'{notas100} (s) de R$ 100,00')
print(f'{notas50} (s) de R$ 50,00')
print(f'{notas20} (s) de R$ 20,00')
print(f'{notas10} (s) de R$ 10,00')
print(f'{notas5} (s) de R$ 5,00')
print(f'{notas2} (s) de R$ 2,00')
print(f'{notas1} (s) de R$ 1,00')