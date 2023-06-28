#66 - Soma e contador

cont = soma = 0

while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    else:
        soma += n
        cont +=1
print(f'A soma dos {cont} valores é {soma}')