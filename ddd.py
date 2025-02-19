import random
from funcoes import classificar_carta

health = 20

# Construção do deck
naipes = [" ♠", " ♣", " ♥", " ♦"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = [
    f"{valor}{naipe}"
    for naipe in naipes
    for valor in valores
    if not (naipe in [" ♥", " ♦"] and valor in ["A", "K", "Q", "J"])
]


# função de definição de valores

def atribuir_valor_carta(valor_carta):
    if valor_carta == "J":
        return 11
    elif valor_carta == "Q":
        return 12
    elif valor_carta == "K":
        return 13
    elif valor_carta == "A":
        return 14
    elif valor_carta.isdigit():
        return int(valor_carta)  # Se for número, usa o valor numérico
    return 0

# função de compra de 4 cartas
def comprar_cartas(deck, health):
    cartas_compradas = []
    
    for i in range(4):
        carta_comprada = random.choice(deck)
        # Atualizar health dependendo do tipo de carta
        type_card = classificar_carta(carta_comprada)
        deck.remove(carta_comprada)  # Remove a carta comprada do deck
        cartas_compradas.append((carta_comprada, type_card))
    
    return cartas_compradas, health

# Função para o usuário escolher uma carta
def escolher_carta(cartas_compradas, health):
    power = 0

    for i in range(3):  # Repetir 3 vezes, restando apenas 1 carta no final
        print(f'❤️ {health} HP')
        print(f'⚔️ {power} Power')
        print("\nEscolha uma carta para usar (digite o número correspondente):")
        for j, (carta, tipo) in enumerate(cartas_compradas):
            print(f"{j + 1}. {carta} - {tipo}")
        
        escolha = int(input("Digite o número da carta que deseja usar: ")) - 1
        
        if 0 <= escolha < len(cartas_compradas):
            carta_escolhida, tipo = cartas_compradas.pop(escolha)  # Remove a carta escolhida da lista

            valor_carta = carta_escolhida[:-2]
            
            # Atribuir o valor da carta usando a função
            valor_carta = atribuir_valor_carta(valor_carta)            

            # Atualizar health dependendo do tipo de carta
            if tipo in ["Bat 🦇", "Skeleton 💀", "Zombie 🧟", "Ghost 👻", "Vampire 🧛", "Ooga Booga 👹", "Dragon 🐉", "Dark Wizard of Doom and Despair 🧙"]:
                health = health + (power - valor_carta)  # Monstros diminuem a vida
            elif tipo in ["Potion 🧪🩸"]:
                health += valor_carta  # Potion aumenta a vida
                if health >20:
                    health=20
            elif tipo in ["Weapon ⚔️"]:
                power = valor_carta

            print(f"\nVocê usou a carta {carta_escolhida} - {tipo}")
        else:
            print("Escolha inválida. Nenhuma carta foi usada.")
    
    return health


# chamando a função para append na lista cartas_compradas
cartas_compradas, health = comprar_cartas(deck, health)
health = escolher_carta(cartas_compradas, health)

# Exibir o número de cartas restantes no deck
print(f'\nCartas restantes no deck: {len(deck)}')
print(f'❤️ {health} HP')
print(f'⚔️ {power} Power')


# Game Over ou Win
if len(deck) == 0 and health > 0:
    print('You Win! 🎉')

if health <= 0:
    print('Game Over 💀')
