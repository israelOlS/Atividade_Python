"""try - tentar = tentar o código
excepet - exceto = exceto quando... - significa que houve um erro 
Tentar executar o código exceto quando houver um erro

pass ou ... serve para colocar algo dentro do try ou except pois esse blocos não pode ficar vazio dá erro
"""
numero = input('Dígite um número que devolverei o seu dobro: ')

try:
    print(numero)
    convertFloat = float(numero)
    print("FLOAT: ", numero)
    print(f'O dobro do número {numero} é {convertFloat * 2:.2f}')
except:
    print('Valor invalido, por favor dígite um número')

"""if numero.isdigit():
    convertFloat = float(numero)
    print(f'O dobro do número {numero} é {convertFloat *2:,.2f}')
else:
    print("Valor invalido, por favor dígite um número")"""