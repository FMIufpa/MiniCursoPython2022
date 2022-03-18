# Calcula delta e quantidade de raízes reais
def calcularDelta(): 
    delta = (b ** 2) - 4 * a * c
    if delta > 0:
        print('Delta positivo! DUAS RAÍZES REAIS E DISTINTAS!')
    elif delta == 0:
        print('Delta igual a zero! DUAS RAÍZES REAIS E IGUAIS!')
    else:
        print('Delta negativo! SEM RAÍZES REAIS!\n')
    return delta

# Calcula e imprime as raízes da função
def calcularRaizes(): 
    delta = calcularDelta()
    if delta >= 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print('''RAÍZES DA FUNÇÃO:
        X1: {:.2f}
        x2: {:.2f}
        '''.format(x1, x2))

# Calcula ponto de máximo ou mínimo
def calculaMaximoMinimo():
    xVertice = (-b) / (2 * a)
    yVertice = (-((b ** 2) - 4 * a * c)) / (4 * a)
    print('''PONTO DE {}
    X do vértice: {:.2f}
    Y do vértice: {:.2f}
    '''.format('MÍNIMO' if a > 0 else 'MÁXIMA', xVertice, yVertice))

# Imprime a concavidade da função
def concavidade():
    print('''CONCAVIDADE DA FUNÇÃO:
Função concava para {}\n'''.format('cima' if a > 0 else 'baixo'))

# Aqui o usuário vai entrar com os valores da função
print('FUNÇÃO DO SEGUNDO GRAU: f(x) = a X² + b X + c')
a = float(input('Entre com o valor de a: '))    
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))
print('FUNÇÃO INFORMADA: {} X² + {} X + {}\n'.format(a, b, c))

while True:
    if a == 0:
        print('A FUNÇÃO INFORMADA NÃO É DO SEGUNDO GRAU!')
        print('O coeficiente \'a\' deve ser diferente de 0')
        break
    
    print('''O QUE VOCÊ DESEJA CALCULAR?
    [1] Raízes
    [2] Ponto Máximo ou Mínimo
    [3] Concavidade da Função
    [4] Sair''')
    escolha = input('Sua escolha: ')
    
    if escolha == '1':
        calcularRaizes()
    elif escolha == '2':
        calculaMaximoMinimo()
    elif escolha == '3':
        concavidade()
    elif escolha == '4':
        print('Obrigado pela preferência!')
        break
    else:
        print('Opção inválida!\n')
