# 🃏 Dungeon Deck of Doom (DDD): Scoundrel Solo Dungeon Crawler  

**Dungeon Deck of Doom** é um jogo de cartas roguelike no terminal, onde estratégia e sorte definem seu destino. Você se aventura em uma masmorra cheia de criaturas sombrias, poções místicas e armas poderosas. Cada carta representa uma escolha crítica: atacar, se defender ou se curar. Seu objetivo? Sobreviver até o final do baralho!  

## 🎮 Como Jogar  
- O jogo começa com **4 cartas na mesa**.  
- Sempre que restar apenas **1 carta na mesa**, você compra **3 novas cartas** do deck.  
- Seu objetivo é **sobreviver até o fim do baralho** enfrentando criaturas e utilizando armas e poções com sabedoria.  

### 🃏 Tipos de Cartas  
- **Monstros:** Cada criatura tem uma **força de ataque**. Se seu poder de defesa for menor, você recebe dano no HP.  
- **Armas:** Aumentam seu **poder de defesa**, mas **quebram** caso você enfrente um inimigo mais forte do que o último derrotado com ela.  
- **Poções:** Restauram parte do seu **HP** para ajudar na sobrevivência.  

### ⚔️ Mecânica de Combate  
- Se seu **poder de defesa** for **maior ou igual** à força do inimigo, você derrota o monstro sem sofrer dano, se for **menor**, você **perde HP** igual à diferença entre os valores.  
- Sempre que você usa uma **arma**, ela **substitui** a anterior, e só continua ativa se o inimigo derrotado não for mais forte que o último enfrentado com essa arma. Caso contrário, a arma **se quebra** e você perde sua defesa.

### 🏆 Objetivo  
- O jogo termina quando **todas as cartas forem usadas** (vitória) ou quando seu **HP chegar a zero** (derrota).  
- O sistema de **recordes** armazena os **5 melhores desempenhos** (menos cartas restantes ao vencer).  


## 🏆 Recordes  
O jogo salva automaticamente os **5 melhores recordes** (menor número de cartas restantes ao vencer). Será que você consegue superar seu próprio desempenho?  

## 🚀 Tecnologias Utilizadas  
- **Python** para a lógica do jogo.  
- **Arquivos de texto (`recordes.txt`)** para salvar os recordes dos jogadores.  
- **Uso de `random`** para embaralhar cartas e garantir partidas sempre diferentes.  

## 📌 Instalação e Execução  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seuusuario/dungeon-deck.git
