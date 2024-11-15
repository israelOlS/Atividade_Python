#Recebe a idade de alguem em dias
#Desafio devolver a idade em anos, meses e dias

DiasTotais = int(input())
#Converção
Anos = DiasTotais//365
Meses = (DiasTotais%365)//30
Dias = (DiasTotais%365)%30

print(f'{Anos:.0f} ano(s)\n{Meses:.0f} mes(es)\n{Dias} dia(s)')