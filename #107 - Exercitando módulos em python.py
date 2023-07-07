#107 - Exercitando módulos em python
import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {Moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {Moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R$ {Moeda.aumentar(p):.2f}')
print(f'Reduzindo 13%, temos R$ {Moeda.diminuir(p):.2f}')