import time
import random
life = 45

print('Olá, Bravo Aventureiro. Este é o começo da tua jornada nesta saga épica.')
time.sleep(2)
print('Iremos desbravar locais hostis e inóspitos, lutaremos contra criaturas terríveis e crueis.')
time.sleep(2)
print('Desvendaremos mistérios profundos e se sobrevivermos a tudo isso, grandes recompensas nos aguardam.')
time.sleep(2)
print('')

classe = ''
while 'mago' != classe !='cavaleiro':
    classe = str(input("""Para darmos início a nossa aventura, por favor, 
nos diga qual será a classe do teu personagem? (Mago ou Cavaleiro): """)).strip().lower()
    if classe != 'mago' and classe != 'cavaleiro':
        print('Classe inválida. Tente novamente entre Mago ou Cavaleiro.')
print('')
time.sleep(2)
if classe == 'cavaleiro':
    print('Então você será um bravo Cavaleiro. Ótima escolha, Sir!')
elif classe == 'mago':
    print('Vejo que optou por ser um poderoso Mago. Escolha interessante, Milord!')

print('')
nome = input('E como será o nome desse personagem nessa épica aventura? ').strip()
print(f'Excelente, {nome}! nossa aventura vai começar agora! ')
print('='*100)
print('')
time.sleep(1.5)
print("""Após se destacar na antiga e mais respeitada fraternidade de magos do norte de Ravendor,
      a fraternidade Garfenir, você foi enviado como o mago mais apto para atender o chamado do rei de
      Ravendor, Fostan.""")
print('')
time.sleep(1.5)
print("""Fostan é um rei muito astuto e queria se assegurar de que Garfenir estava enviando alguém 
      de qualidade para atender o seu chamado e resolveu montar uma armadilha para avaliar suas
      habilidades. Quando você estava em sua carroagem na estrada para o castelo de Ravendor,
      você foi surpreendido por duas criaturas no meio do caminho que pararam tua carroagem e 
      começaram a esbravejar algo estranho.""")
print('')
time.sleep(2)

luta1 = input("""Eram dois goblins combatentes. Não são criaturas ameaçadoras, 
            mas você teme que elas sejam apenas uma isca para algo pior.
            O que você vai fazer? Lutar/Fugir: """).strip().lower()

gob1Life: int = 10
gob2Life: int = 10
ataques: int = 0
inimigo = 0

if luta1 == 'lutar':
    print('=' * 25)
    print(f'Sua vida: {life}hp.')
    print(f'Vida do Goblin1: {gob1Life}hp.')
    print(f'Vida do Goblin1: {gob2Life}hp.')
    print('=' * 25)
    print('')
    time.sleep(2)
    print('=' * 75)
    print('Lista de ataques: [1] Bola de fogo , [2] Chuva de raios, [3] Névoa venenosa')
    print('=' * 75)

print('')
while (ataques != 1) and (ataques != 2) and (ataques != 3):
    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
time.sleep(1.5)
while (inimigo != 1) and (inimigo != 2):
    inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))
print('')

while (life > 0) and (gob1Life > 0 or gob2Life > 0):
    if ataques == 1 and inimigo == 1:
        print("""Você concentrou sua energia com um misto de raiva por essa desagradável surpresa e
        disparou uma poderosa bola de fogo na direção do Goblin1.""")
        fireball = random.randint(1, 10)
        print('')
        print(f'Seu ataque causou um dano de {fireball}hp naquele goblin.')
        gob1Life = gob1Life - fireball
        print('=' * 25)
        print(f'Sua vida: {life}hp.')
        print(f'Vida do Goblin1: {gob1Life}hp.')
        print(f'Vida do Goblin1: {gob2Life}hp.')
        print('=' * 25)
        time.sleep(1.5)
        print('')

        if (gob1Life > 0):
            print('=====O turno do Goblin1=====')
            atakgob1 = random.randint(0, 3)
            life = life - atakgob1
            print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
            print('=' * 25)
            print(f'Sua vida: {life}hp.')
            print(f'Vida do Goblin1: {gob1Life}hp.')
            print(f'Vida do Goblin1: {gob2Life}hp.')
            print('=' * 25)

        time.sleep(2)
        print('')

        if (gob2Life > 0):
            print('=====O turno do Goblin2=====')
            atakgob2 = random.randint(0, 3)
            life = life - atakgob2
            print(f'O ataque do Goblin1 causou {atakgob2} de dano.')
            print('=' * 25)
            print(f'Sua vida: {life}hp.')
            print(f'Vida do Goblin1: {gob1Life}hp.')
            print(f'Vida do Goblin1: {gob2Life}hp.')
            print('=' * 25)

        ataques: int = 0
        inimigo: int = 0

        if (gob1Life > 0) or (gob2Life > 0):
            while (ataques != 1) and (ataques != 2) and (ataques != 3):
                ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
            time.sleep(1.5)
            while (inimigo != 1) and (inimigo != 2):
                inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))

    elif ataques == 1 and inimigo == 2:
        print("""Você concentrou sua energia com um misto de raiva por essa desagradável surpresa e
                disparou uma poderosa bola de fogo na direção do Goblin2.""")
        fireball = random.randint(1, 10)
        print('')
        print(f'Seu ataque causou um dano de {fireball}hp naquele goblin.')
        gob2Life = gob2Life - fireball
        print('=' * 25)
        print(f'Sua vida: {life}hp.')
        print(f'Vida do Goblin1: {gob1Life}hp.')
        print(f'Vida do Goblin1: {gob2Life}hp.')
        print('=' * 25)
        time.sleep(1.5)
        print('')

        if (gob1Life > 0):
            print('=====O turno do Goblin1=====')
            atakgob1 = random.randint(0, 3)
            life = life - atakgob1
            print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
            print('=' * 25)
            print(f'Sua vida: {life}hp.')
            print(f'Vida do Goblin1: {gob1Life}hp.')
            print(f'Vida do Goblin1: {gob2Life}hp.')
            print('=' * 25)

        time.sleep(2)
        print('')

        if (gob2Life > 0):
            print('=====O turno do Goblin2=====')
            atakgob2 = random.randint(0, 3)
            life = life - atakgob2
            print(f'O ataque do Goblin2 causou {atakgob2} de dano.')
            print('=' * 25)
            print(f'Sua vida: {life}hp.')
            print(f'Vida do Goblin1: {gob1Life}hp.')
            print(f'Vida do Goblin1: {gob2Life}hp.')
            print('=' * 25)

        ataques: int = 0
        inimigo: int = 0

        if (gob1Life > 0) or (gob2Life > 0):
            while (ataques != 1) and (ataques != 2) and (ataques != 3):
                ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
            time.sleep(1.5)
            while (inimigo != 1) and (inimigo != 2):
                inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))

    # elif ataques == 2:

    # elif ataques == 3:
print('')
print('='*80)
if (life > 38):
    print(f"""Parabéns, {nome}! Com grande destreza e habilidade você mostrou que não foi escolhido
    para essa missão por mera casualidade! Acabou com aqueles goblins!""")
elif (38 > life > 30):
    print(f"""Ufa! Acabar com aqueles goblins não foi tão fácil quanto você pensou!
     Mas você conseguiu, parabéns, {nome}!""")
elif (30 > life > 15):
    print(f"""INACREDITÁVEL! Que surra você levou! Por pouco o grande {nome} não teria sucumbido
diante de meros goblins. Vamos! Você precisa se recuperar para se encontrar com o rei.""")
elif (15 > life > 1):
    print(f"""Rápido! Você precisa de cuidados médicos com urgência! O grande {nome} quase 
morreu pelas mãos de pequenos goblins. Talvez você não seja tão bom como sua fama tem dito por aí.""")