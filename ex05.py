# Faça um programa que leia o primeiro termo e a razão de uma PA, e em seguida imprima na tela seus primeiros 10 termos.
primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
for i in range(10):
    print(primeiro + (razao * i))
