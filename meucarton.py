meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontrei = False

while cartaoLido != 0 and not encontrei:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontrei = True

if encontrei:
    print("Opa, encontrado!")
else:
    print("Não está nesta lista!")