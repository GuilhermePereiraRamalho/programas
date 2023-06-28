#56 - senso de um grupo
soma_idade = 0
maior_idade = 0
soma_mulheres = 0
for i in range(1,5):
    nome = input('Qual seu nome? ')
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual seu sexo? (masculino/feminino) ')
    soma_idade += idade
    if idade > maior_idade and sexo.lower() == 'masculino':
        maior_idade = idade
        nome_maior = nome
    if idade < 20 and sexo.lower() == 'feminino':
        soma_mulheres += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos, o homem mais velho se chama {} e a quantidade de mulheres abaixo dos 20 anos é {}'.format(media_idade,nome_maior,soma_mulheres))