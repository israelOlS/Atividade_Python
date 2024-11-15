#Recebe um valor em segundos e retorna em horas,min e seg
# / faz a divisão normal o // faz a divisão em int

Horario = int(input())
Hora = Horario//3600
Minutos = (Horario%3600)//60
Segundos = Horario%60

print(f'{Hora:.0f}:{Minutos:.0f}:{Segundos}')