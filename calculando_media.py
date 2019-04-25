# importando o tipo array as dando nome ao
import array as arr

# f é o tipo de conteúdo que esse array suporta
Nota = arr.array('f');

# Digita a quantidade de períodos
Periodos = int(input("Digite a quantidade de periodos: "))

for PeriodoAtual in range(0, Periodos):
    teste = PeriodoAtual + 1
    # Está transformando o input em um tipo float e adicionando ao array
    Nota.append(float(input("Digite a sua {}ª nota: ".format(teste))))
    while ((Nota[PeriodoAtual] < 0) or (Nota[PeriodoAtual] > 10)):
        Nota[PeriodoAtual] = float(input("Digite uma nota válida: "))

Media = sum(Nota[:])/Periodos

print("Sua média é: {:.2f}".format(Media))
input("Aperte [ENTER] para sair")
