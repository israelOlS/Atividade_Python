primeiro_valor = input("Digíte o primeiro valor: ")
segundo_valor = input("Dígite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor = {primeiro_valor}, é maior que o segundo valor = {segundo_valor}")
elif primeiro_valor == segundo_valor:
    print(f"O primeiro valor = {primeiro_valor} é igual ao segundo valor = {segundo_valor}")
else:
    print(f"O primeiro valor = {primeiro_valor}, é menor que o segundo valor = {segundo_valor}")