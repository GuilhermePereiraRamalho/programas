#fraça um pograma que leia uma frase pelo teclado e mostre quantas letras "A" em que posicao ela aparece primeiro e qual posição dela pela ultima vez

frase = str(input('Informe uma frase: ')).strip()
print('''Sua frase possui {} letras "A" 
O primeiro A aparece na posição {}
O Ultimo na posição {}'''.format(frase.upper().count('A'),frase.find('A')+1,frase.rfind('A')+1))