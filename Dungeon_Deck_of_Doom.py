import random

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

#### FUNÇÕES ###

# Recorde
def carregar_recordes():
    try:
        with open("recordes.txt", "r") as file:
            recordes = [linha.strip().split(", ") for linha in file.readlines()]
            recordes = [(int(cartas), int(andar)) for cartas, andar in recordes]  # Converte para tuplas de (cartas, andar)
            # Ordena pela quantidade de cartas de forma crescente e pelo andar
            return sorted(recordes, key=lambda x: (x[0], x[1]))[:5]  # Exibe apenas os 5 melhores
    except (FileNotFoundError, ValueError):
        return []
    
# Salvar Recorde
def salvar_recordes(cartas_restantes, andar):
    # Carrega todos os registros existentes
    recordes = carregar_recordes()  
    recordes.append((cartas_restantes, andar))  # Adiciona o novo registro

    # Salva todos os registros de volta no arquivo
    with open("recordes.txt", "w") as file:
        for cartas, andar in recordes:
            file.write(f"{cartas}, {andar}\n")  # Salva todos os jogos


# Classificador de carta
def classificar_carta(carta):
    valor = carta[:-2]  # Retira o naipe da carta para pegar o valor
    naipe = carta[-1]   # Pega o naipe da carta
    
    # Primeira verificação para Potion e Weapon
    if naipe == '♥':
        return "Potion 🧪🩸"
    elif naipe == '♦':
        if valor in ['2', '3']:
            return "Dagger ⚔️"
        elif valor in ['4', '5']:
            return "One-Handed Sword ⚔️" 
        elif valor in ['6', '7']:
            return "Elven Bow ⚔️"
        elif valor in ['8', '9']:
            return "Royal Shield ⚔️"
        elif valor == '10':
            return "Void Staff ⚔️"
    
    # Classificação para os monstros com base no valor
    if valor in ['2', '3']: 
        return "Bat 🦇"
    elif valor in ['4', '5']:
        return "Skeleton 💀"
    elif valor in ['6', '7', '8']:
        return "Zombie 🧟"
    elif valor in ['9', '10']:
        return "Ghost 👻"
    elif valor == 'J':
        return "Vampire 🧛"
    elif valor == 'Q':
        return "Ooga Booga 👹"
    elif valor == 'K':
        return "Dragon 🐉"
    elif valor == 'A':
        return "Dark Wizard of Doom and Despair 🧙"
    
    return "Desconhecido"


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

# função de compra de cartas em geral para loop
def comprar_cartas(deck, cartas_compradas, andar):
    deck_restante = [carta for carta in deck if carta not in [c[0] for c in cartas_compradas]]
    if len(cartas_compradas) == 1:
        novas_cartas = random.sample(deck_restante, min(3, len(deck_restante)))
        cartas_compradas.extend((carta, classificar_carta(carta)) for carta in novas_cartas)
        andar += 1
    elif len(cartas_compradas) == 0:
        novas_cartas = random.sample(deck_restante, min(4, len(deck_restante)))
        cartas_compradas.extend((carta, classificar_carta(carta)) for carta in novas_cartas)
    return cartas_compradas, andar

# Função para o usuário escolher uma carta
def jogar(deck, health):
    power = 0
    last_monster = None
    cartas_compradas = []
    andar = 1
    
    while len(deck) > 0 and health > 0:
        cartas_compradas, andar = comprar_cartas(deck, cartas_compradas, andar)
        
        print(f'\n❤️  {health} HP  |  ⚔️  {power} Power  |  Last Monster Power Level: {last_monster}  |  🏰 Andar {andar}')
        print(f'Faltam apenas {len(deck)} cartas para você sair vivo da dungeon.')
        print("\nEscolha uma carta para usar (digite o número correspondente):")
        for j, (carta, tipo) in enumerate(cartas_compradas):
            print(f"{j + 1}. {carta} - {tipo}")
        
        escolha = -1
        while escolha < 0 or escolha >= len(cartas_compradas):
            try:
                escolha = int(input("Digite o número da carta que deseja usar: ")) - 1
                if escolha < 0 or escolha >= len(cartas_compradas):
                    print("Escolha inválida. Por favor, digite um número válido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        
        carta_escolhida, tipo = cartas_compradas.pop(escolha)
        deck.remove(carta_escolhida)
        valor_carta = atribuir_valor_carta(carta_escolhida[:-2])
        
        if tipo in ["Bat 🦇", "Skeleton 💀", "Zombie 🧟", "Ghost 👻", "Vampire 🧛", "Ooga Booga 👹", "Dragon 🐉", "Dark Wizard of Doom and Despair 🧙"]:
            if last_monster is not None and valor_carta >= last_monster:
                power = 0
                health -= valor_carta
                last_monster = None
            elif power < valor_carta:
                health = health + (power - valor_carta)
                last_monster = valor_carta
            else: last_monster = valor_carta
        elif tipo == "Potion 🧪🩸":
            health = min(20, health + valor_carta)

        elif tipo in ["Dagger ⚔️", "One-Handed Sword ⚔️", "Elven Bow ⚔️", "Royal Shield ⚔️", "Void Staff ⚔️"]:
            power = valor_carta
            last_monster = None 
        
        print(f"\nVocê usou a carta {carta_escolhida} - {tipo}")
    
    return health, power, andar

 
# chamando a função
health, power, andar = jogar(deck, health)

# Exibir o número de cartas restantes no deck
print(f'\n❤️  {health} HP  |  ⚔️  {power} Power  | Cartas restantes no deck: {len(deck)}  |  🏰 Andar {andar}')

# Carregar recordes
recordes = carregar_recordes()

# Game Over ou Win
if len(deck) == 0 and health > 0:
    print('You Win! 🎉')

if health <= 0:
    print(f'Você foi derrotado, mais uma vez...')

# Salvar o novo recorde se necessário
if len(recordes) < 5 or len(deck) < min([r[0] for r in recordes]):
    salvar_recordes(len(deck), andar)  # Passa as cartas restantes e o andar
    print(f"🎉 Novo recorde! {len(deck)} cartas restantes  |  {andar}º Andar.")

# Exibir os Top 5 Recordes
print("\n🏆 Top 5 Recordes:")
recordes = sorted(carregar_recordes(), key=lambda x: (x[0], x[1]))[:5] # Carrega todos os recordes, ordena e exibe apenas os 5 melhores
for i, (cartas, andar) in enumerate(recordes, 1):
    print(f"{i}. {cartas} cartas restantes | {andar}º Andar.")
