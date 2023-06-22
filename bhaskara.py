# Aluno: Ana Júlia Lopes Varoni- Questão: "Fórmula de Bhaskara"

a = float(input("informe seu a: "))
b = float(input("informe seu b: "))
c = float(input("informe seu c: "))
delta = b**2 - 4 * a * c

if delta < 0 or a == 0:
    print("Impossível calcular")

x1 = (-b) + delta **0.5
x2 = (-b) - delta **0.5

print('O valor de x1 é ', x1, 'e do x2:', x2)

#Nesse código eu achei mais fácil, o programa em peimeiro plano pede para a pessoa informar os 3
#primeiros valores flutuantes, e eles sendo informados, o programa realiza a formula de bhaskara, descobrindo o delta,
# e se caso o mesmo for negativo ou igual a zero imprime um mensagem informando que é impossivel calcular. Já se
# delta for positivo, ele realiza a conta para descobrir o x1 e o x2





























