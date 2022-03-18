# Faça um programa que leia o peso de 5 pessoas, e em seguida, mostre o menor e o maior peso lido.
lista = []
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    lista.append(peso)
lista.sort()
print('O maior peso lido foi: {}, e o menor peso lido foi: {}'.format(lista[0], lista[4]))
