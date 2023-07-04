#90 - Dicionario em python
boletim = dict()
aluno = list()

boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
aluno.append(boletim.copy())
for d in aluno:
    for k, v in d.items():
        print(f'{k} é igual a {v}')

