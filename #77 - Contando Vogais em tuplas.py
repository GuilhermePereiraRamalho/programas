#77 - Contando Vogais em tuplas
palavras = ('morango', 'banana', 'uva', 'pera',
            'abacate', 'limao', 'laranja', 'abacaxi',
            'melao', 'bergamota', 'caju', 'kiwi')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
