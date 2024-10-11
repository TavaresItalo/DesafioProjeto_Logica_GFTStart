# Hero Experience Classifier

Este repositório contém um algoritmo que classifica um herói de acordo com seu nível de experiência. O algoritmo é implementado em Python e pode ser utilizado como base para jogos de RPG, onde personagens acumulam experiência e mudam de classificação ao atingir determinados níveis.

## Linguagem Utilizada
O código é desenvolvido em **Python**, uma linguagem de programação de alto nível, conhecida por sua simplicidade e versatilidade.

## Funcionalidade
O algoritmo classifica o herói em diferentes categorias, de acordo com seu nível de experiência. Os níveis de experiência e as respectivas classificações de herói são:

### Classificação de Herói por Nível
- **Ferro**: até 1000 pontos de experiência
- **Bronze**: 1001 - 2000 pontos de experiência
- **Prata**: 2001 - 5000 pontos de experiência
- **Ouro**: 5001 - 7000 pontos de experiência
- **Platina**: 7001 - 8000 pontos de experiência
- **Ascendente**: 8001 - 9000 pontos de experiência
- **Imortal**: 9001 - 10000 pontos de experiência
- **Radiante**: Acima de 10000 pontos de experiência

### Exemplo de Uso
```python
# Criando variáveis que serão utilizadas durante o algoritmo
nomeHeroi = input("Digite o nome do Herói: ")
xpHeroi = int(input("Digite o nível do Herói: "))
nivelHeroi = ""

# Criando condicionais que definirão o nível do herói
if xpHeroi <= 1000:  
    nivelHeroi = "Ferro"
elif xpHeroi >= 1001 and xpHeroi <= 2000:
    nivelHeroi = "Bronze"
elif xpHeroi >= 2001 and xpHeroi <= 5000:
    nivelHeroi = "Prata"
elif xpHeroi >= 5001 and xpHeroi <= 7000:
    nivelHeroi = "Ouro"
elif xpHeroi >= 7001 and xpHeroi <= 8000:
    nivelHeroi = "Platina"
elif xpHeroi >= 8001 and xpHeroi <= 9000:
    nivelHeroi = "Ascendente"
elif xpHeroi >= 9001 and xpHeroi <= 10000:
    nivelHeroi = "Imortal"
else:
    nivelHeroi = "Radiante"

# Exibindo a saída do algoritmo
print(f"O Herói de nome: {nomeHeroi} está no nível de {nivelHeroi}")
