"""Conversor de notas e moedas

Receberemos um valor aleatorio em reias, e verifcar o quantas e os tipos notas e moedas que compoem este valor

As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
"""
valorRecebido = float(input())

NotasDe100 = valorRecebido//100
ValorRestante = valorRecebido%100

NotasDe50 = ValorRestante//50
ValorRestante = ValorRestante%50

NotasDe20 = ValorRestante//20
ValorRestante = ValorRestante%20

NotasDe10 = ValorRestante//10
ValorRestante = ValorRestante%10

NotasDe05 = ValorRestante//5
ValorRestante = ValorRestante%5

NotasDe02 = ValorRestante//2
ValorRestante= ValorRestante%2

#Moedas
MoedasDe_1 = ValorRestante//1
ValorRestante = ValorRestante%1

MoedasDe_50 = ValorRestante//0.5
ValorRestante = ValorRestante%0.5

MoedasDe_25 = ValorRestante//0.25
ValorRestante = ValorRestante%0.25

MoedasDe_10 = ValorRestante//0.10
ValorRestante = ValorRestante%0.10

MoedasDe_05 = ValorRestante//0.05
ValorRestante = ValorRestante%0.05

MoedasDe_01 = ValorRestante//0.01
ValorRestante = ValorRestante%0.01

print('NOTAS:')
print(f'{NotasDe100:.0f} nota(s) de R$ 100.00')
print(f'{NotasDe50:.0f} nota(s) de R$ 50.00')
print(f'{NotasDe20:.0f} nota(s) de R$ 20.00')
print(f'{NotasDe10:.0f} nota(s) de R$ 10.00')
print(f'{NotasDe05:.0f} nota(s) de R$ 5.00')
print(f'{NotasDe02:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{MoedasDe_1:.0f} moeda(s) de R$ 1.00')
print(f'{MoedasDe_50:.0f} moeda(s) de R$ 0.50')
print(f'{MoedasDe_25:.0f} moeda(s) de R$ 0.25')
print(f'{MoedasDe_10:.0f} moeda(s) de R$ 0.10')
print(f'{MoedasDe_05:.0f} moeda(s) de R$ 0.05')
print(f'{MoedasDe_01:.0f} moeda(s) de R$ 0.01')