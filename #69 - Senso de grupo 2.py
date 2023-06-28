#69 - Senso de grupo 2
tot_m = cont_18 = tot_f = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]  
    if idade > 18:
        cont_18 += 1
    if sexo == 'M':
        tot_m += 1
    if sexo == 'F' and idade < 20:
        tot_f +=1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]   
    if cont == 'N':
        break
print('{:=^30}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {cont_18}')
print(f'Ao todo temos {tot_m} homens cadastrados')
print(f'E temos {tot_f} mulheres com menos de 20 anos')
