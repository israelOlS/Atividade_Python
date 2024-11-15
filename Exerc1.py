nome = input("Dígite o seu nome: ")
idade = int(input("Dígite o sua idade: "))

if nome and idade:
    print(f'Seu nome é {nome}\nSeu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A letra do seu nome é "{nome[-1]}"')
    
else:
    print("Parece que você esqueceu de preencher os dados solicitados")