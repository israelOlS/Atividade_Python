"""
Faça um programa que leia um valor e apresente uma mensagem dizendo em qual dos seguintes intervalos abaixo este valor se encontra.
([0,25], (25,50], (50,75], (75,100]) 
Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

"""
NumeroQualquer = float(input())

if NumeroQualquer < 0 or NumeroQualquer> 100:
    print("Fora de intervalo")
elif NumeroQualquer >= 0 and NumeroQualquer<= 25:
    print("Intervalo (0,25]")
elif NumeroQualquer >25 and NumeroQualquer<= 50:
    print("Intervalo (25,50]")
elif NumeroQualquer >50 and NumeroQualquer<= 75:
    print("Intervalo (50,75]")
else: 
    print("Intervalo (75,100]")