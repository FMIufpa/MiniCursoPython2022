# Faça um programa que leia o nome, idade e altura (em metros) de uma pessoa, e em seguida, imprima esses valores.
print('{0}\n{1}\n{0}'.format('-' * 20, 'FORMULÁRIO'))
nome = input('Nome: ')
idade = int(input('Idade: '))
altura = float(input('Alutra: '))
print('Nome: {}\nIdade: {}\nAltura: {:.2f} m'.format(nome, idade, altura))
