# Faça um programa que leia medidas de um terreno retangular e mostre o seguinte menu funcional:
# [1] ÁREA
# [2] PERÍMETRO
# [3] NOVOS VALORES
# [4] SAIR DO PROGRAMA

def area(x, y):
    return x * y

def perimetro(x, y):
    return (2 * x) + (2 * y)

print('-' * 30)
print('ENTRE COM AS MEDIDAS DO TERRENO')
print('-' * 30)
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))

while True:
    print('''[1] ÁREA
[2] PERÍMETRO
[3] NOVOS VALORES
[4] SAIR DO PROGRAMA''')
    opt = int(input('>>>>> Sua opção: '))
    
    if opt == 1:
        print('{:.2f} m²'.format(area(largura, comprimento)))
    elif opt == 2:
        print('{:.2f} m'.format(perimetro(largura, comprimento)))
    elif opt == 3:
        largura = float(input('Largura [m]: '))
        comprimento = float(input('Comprimento [m]: '))
    elif opt == 4:
        break
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente!')
    print()
