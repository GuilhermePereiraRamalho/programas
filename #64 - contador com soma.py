#64 - contador com soma
i=0
soma=0
count = 0
while i != 999:
    i = int(input('Informe um numero: digite 999 para parar '))
    if i == 999:
        print('Operação Finalizada!')
    else:
        soma += i
        count += 1
print('Voce digitou {} numeros e a soma entre ele é: {}'.format(count,soma))
