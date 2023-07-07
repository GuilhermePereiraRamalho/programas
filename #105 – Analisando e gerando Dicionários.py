#105 – Analisando e gerando Dicionários
def notas(*n, sit = False):
    """
     -> Função para analisar notas e situações de vários alunos.
     :param n: uma ou mais notas dos alunos(aceia várias)
     :param sit: valor opcional, indicando se deve ou não adicionar a situação
     :return: dicionario com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#programa principal
resp = notas(5.5, 2.5, 1.5, sit = True)
print(resp)
help(notas)