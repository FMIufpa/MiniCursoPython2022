#include <stdio.h>
#include <math.h>

float calcularDelta(float a, float b, float c)
{
    float delta;
    delta = (b * b) - (4 * a * c);
    if (delta > 0)
    {
        printf("Delta positivo! DUAS RAÍZES REAIS E DISTINTAS!\n");
    }
    else if (delta == 0)
    {
        printf("Delta igual a zero! DUAS RAÍZES REAIS E IGUAIS!\n");
    }
    else
    {
        printf("Delta negativo! SEM RAÍZES REAIS!\n");
    }
    return(delta);
}

float calcularRaizes(float a, float b, float c)
{
    float delta;
    delta = calcularDelta(a, b, c);
    if (delta >= 0)
    {
        float x1;
        float x2;
        x1 = (-b + pow(delta, 0.5)) / (2 * a);
        x2 = (-b - pow(delta, 0.5)) / (2 * a);
        printf("RAÍZES DA FUNÇÃO:\n");
        printf("X1: %.2f\n", x1);
        printf("X2: %.2f\n", x2);
    }
    return 0.0;
}

int calculaMaximoMinimo(float a, float b, float c)
{
   float xVertice = (-b) / (2 * a);
   float yVertice = (-((b * b) - 4 * a * c)) / (4 * a);
   if (a > 0)
   {
       printf("PONTO DE MÍNIMO\n");
   }
   else
   {
       printf("PONTO DE MÁXIMO\n");
   }
   printf("X do vértice: %.2f\n", xVertice);
   printf("Y do vértice: %.2f\n", yVertice);
   return 0;
}

int concavidade(float a)
{
    printf("CONCAVIDADE DA FUNÇÃO:\n");
    if (a > 0)
    {
        printf("Função concava para cima\n");
    }
    else
    {
        printf("Função concava para baixo\n");
    }
    return 0;
}

int main()
{
    
    float a;
    float b;
    float c;
    
    printf("FUNÇÃO DO SEGUNDO GRAU: f(x) = a x² + b x + c\n");
    printf("Entre com o valor de a: ");
    scanf("%f", &a);
    printf("Entre com o valor de b: ");
    scanf("%f", &b);
    printf("Entre com o valor de c: ");
    scanf("%f", &c);
    printf("Função informada: f(x) = %.2f x² + %.2f x + %.2f\n", a, b, c);
    
    while (1)
    {
        if (a == 0)
        {
            printf("A FUNÇÃO INFORMADA NÃO É DO SEGUNDO GRAU!\n");
            printf("O coeficiente 'a' deve ser diferente de 0");
            break;
        }
        
        int escolha;
        printf("O QUE VOCÊ DESEJA CALCULAR?\n");
        printf("[1] Raízes\n");
        printf("[2] Ponto Máximo ou Mínimo\n");
        printf("[3] Concavidade da Função\n");
        printf("[4] Sair do Programa\n");
        printf(">>>>> Sua escolha: ");
        scanf("%d", &escolha);
        
        if (escolha == 1)
        {
            calcularRaizes(a, b, c);
        }
        else if (escolha == 2)
        {
            calculaMaximoMinimo(a, b, c);
        }
        else if (escolha == 3)
        {
            concavidade(a);
        }
        else if (escolha == 4)
        {
            printf("Obrigado pela preferência!");
            break;
        }
        else
        {
            printf("Opção inválida!\n");
        }
    }
  
    return 0;
}
