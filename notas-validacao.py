# Aluno: Ana Júlia Lopes Varoni- Questão: "Várias Notas com Validação"

while True:
    nota1 = float(input("Digite aprimeira nota: "))
    while nota1 < 0 or nota1 > 10:
        print("Nota inválida. Digite novamente.")
        nota1 = float(input("Digite aprimeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota inválida. Digite novamente.")
        nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    print("Média semestral:", media)

    codigo = int(input("Novo cálculo (1-sim 2-não): "))
    while codigo != 1 and codigo != 2:
        print("Código inválido. Digite novamente.")
        codigo = int(input("Novo cálculo (1-sim 2-não): "))

    if codigo == 2:
        break

#O que eu pensei foi, utilizar o while para que o código possa se repetir,
#primeiramente eu peço que informe a primeira e segunda nota, e se caso for menor que 0 ou maior que 10 apareça a frase
# 'nota inválida' e pede para digitar mais uma vez, depois o codigo pergunta se quer um novo calculo, se caso dizer que sim
# ele retorna as perguntas do começo e se falar que não ele dá a média. E se a nota final for 2 , o programa para.

