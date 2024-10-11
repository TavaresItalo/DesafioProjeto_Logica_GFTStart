# Criando variáveis que serão utilizadas durante o algoritmo
nomeHeroi = input("Digite o nome do Herói: ")
xpHeroi = int(input("Digite o nível do Herói: "))
nivelHeroi = ""

# Criando condicionias que definirão o nível do herói
if(xpHeroi <= 1000) :
    nivelHeroi = "Ferro"
elif(xpHeroi >= 1001 and xpHeroi <= 2000) :
    nivelHeroi = "Bronze"
elif(xpHeroi >= 2001 and xpHeroi <= 5000) :
    nivelHeroi = "Prata"
elif(xpHeroi >= 5001 and xpHeroi <= 7000) :
    nivelHeroi = "Ouro"
elif(xpHeroi >= 7001 and xpHeroi <= 8000) :
    nivelHeroi = "Platina"
elif(xpHeroi >= 8001 and xpHeroi <= 9000) :
    nivelHeroi = "Ascendente"
elif(xpHeroi >= 9001 and xpHeroi <= 10000) :
    nivelHeroi = "Imortal"
else :
    nivelHeroi = "Radiante"

# Printnado saída do algoritmo
print(f"O Herói de nome: {nomeHeroi} está no nível de {nivelHeroi}")