#94 - Unindo dicionarios e listas
dados = dict()
pessoas = list()
soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp in 'nN':
        break
print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = soma/len(pessoas)
print(f'- A média de idade do Grupo é de {media:5.2f} anos')
print('- As mulheres cadastradas foram: ', end = '')
for c in range(0,len(pessoas)):
    if pessoas[c]['sexo'] == 'F':
        print(f'[{pessoas[c]["nome"]}]', end = ' ')
print('\nLista de pessoas acima da média:')
print()
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('<< ENCERRADO >>')

