# Aluno: Ana Júlia Lopes Varoni- Questão: "Coordenadas de um ponto"

x, y = input("Digite as coordenadas do ponto (x y): ").split() #informar o eixo x e y
x = float(x) #ambos são numeros
y = float(y)

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")

# primeiramente eu pedi para que a pessoa informar o eixo x e y, depois coloquei as coordenadas.