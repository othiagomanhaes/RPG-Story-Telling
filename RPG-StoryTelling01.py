#proposta de Jogo de RPG Story-Telly
import funcionalidades
import time
import random
import sys

def parcialVidas():
    print('=' * 25)
    print(f'Sua vida: {life}hp.')
    print(f'Vida do Goblin1: {gob1Life}hp.')
    print(f'Vida do Goblin2: {gob2Life}hp.')
    print('=' * 25)
    time.sleep(1.5)
    print('')

def parcialVidasCav():
    print('=' * 25)
    print(f'Sua vida: {life}hp.')
    print(f'Vida do Diabrete1: {diablife1}hp.')
    print(f'Vida do Diabrete2: {diablife2}hp.')
    print('=' * 25)
    time.sleep(1.5)
    print('')

def printLbL(texto):
    for c in texto:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.03)


printLbL('Olá, Bravo Aventureiro. Este é o começo da tua jornada nesta saga épica.\n')
time.sleep(2)
printLbL('Iremos desbravar locais hostis e inóspitos, lutaremos contra criaturas terríveis e cruéis.\n')
time.sleep(2)
printLbL('Desvendaremos mistérios profundos e, se sobrevivermos a tudo isso, grandes recompensas nos aguardam.\n')
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

if classe == 'mago':
    printLbL("""Após se destacar na antiga e mais respeitada fraternidade de magos do norte de Ravendor,\n
          a fraternidade Garfenir, você foi enviado como o mago mais apto para atender o chamado do rei de\n
          Ravendor, Fostan.\n""")
    print('')
    time.sleep(1.5)
    printLbL("""Fostan é um rei muito astuto e queria se assegurar de que Garfenir estava enviando alguém\n 
          de qualidade para atender o seu chamado e resolveu montar uma armadilha para avaliar suas\n
          habilidades. Quando você estava em sua carruagem na estrada para o castelo de Ravendor,\n
          você foi surpreendido por duas criaturas no meio do caminho que pararam tua carruagem e\n 
          começaram a esbravejar algo estranho.\n""")
    print('')
    time.sleep(2)

    luta1 = input("""Eram dois goblins combatentes. Não são criaturas ameaçadoras, 
                mas você teme que elas sejam apenas uma isca para algo pior.
                O que você vai fazer? Lutar/Fugir: """).strip().lower()

    life = 45
    gob1Life: int = 10
    gob2Life: int = 10
    ataques: int = 0
    inimigo = 0

    if luta1 == 'lutar':
        parcialVidas()
        print('=' * 75)
        print('Lista de ataques: [1] Bola de fogo , [2] Chuva de raios, [3] Névoa venenosa')
        print('=' * 75)

    print('')
    while (ataques != 1) and (ataques != 2) and (ataques != 3):
        ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
    time.sleep(1.5)
    if ataques == 1:
        while (inimigo != 1) and (inimigo != 2):
            inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))
        print('')

    while (life > 0) and (gob1Life > 0 or gob2Life > 0):
        if ataques == 1 and inimigo == 1:
            printLbL("""Você concentrou sua energia com um misto de raiva por essa desagradável surpresa e\n
            disparou uma poderosa bola de fogo na direção do Goblin1.\n""")
            fireball = random.randint(1, 10)
            print('')
            print(f'Seu ataque causou um dano de {fireball}hp naquele goblin.')
            gob1Life = gob1Life - fireball
            parcialVidas()

            if gob1Life > 0:
                print('=====O turno do Goblin1=====')
                atakgob1 = random.randint(0, 3)
                life = life - atakgob1
                print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
                parcialVidas()

            time.sleep(2)
            print('')

            if gob2Life > 0:
                print('=====O turno do Goblin2=====')
                atakgob2 = random.randint(0, 3)
                life = life - atakgob2
                print(f'O ataque do Goblin1 causou {atakgob2} de dano.')
                parcialVidas()

            ataques: int = 0
            inimigo: int = 0

            if (gob1Life > 0) or (gob2Life > 0):
                while (ataques != 1) and (ataques != 2) and (ataques != 3):
                    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
                time.sleep(1.5)
                if ataques == 1:
                    while (inimigo != 1) and (inimigo != 2):
                        inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))

        elif ataques == 1 and inimigo == 2:
            printLbL("""Você concentrou sua energia com um misto de raiva por essa desagradável surpresa e\n
                    disparou uma poderosa bola de fogo na direção do Goblin2.\n""")
            fireball = random.randint(1, 10)
            print('')
            print(f'Seu ataque causou um dano de {fireball}hp naquele goblin.')
            gob2Life = gob2Life - fireball
            parcialVidas()

            if gob1Life > 0:
                print('=====O turno do Goblin1=====')
                atakgob1 = random.randint(0, 3)
                life = life - atakgob1
                print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
                parcialVidas()

            time.sleep(2)
            print('')

            if gob2Life > 0:
                print('=====O turno do Goblin2=====')
                atakgob2 = random.randint(0, 3)
                life = life - atakgob2
                print(f'O ataque do Goblin2 causou {atakgob2} de dano.')
                parcialVidas()

            ataques: int = 0
            inimigo: int = 0

            if (gob1Life > 0) or (gob2Life > 0):
                while (ataques != 1) and (ataques != 2) and (ataques != 3):
                    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
                time.sleep(1.5)
                if ataques == 1:
                    while (inimigo != 1) and (inimigo != 2):
                        inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))

        elif ataques == 2:
            printLbL("""Diante dessa situação você não pensou duas vezes, evocou as forças da natureza a seu favor e\n
                  atraiu uma mística nuvem negra na direção daqueles goblins e houve uma tempestade de raios sobre eles.\n""")

            thunderstorm = random.randint(1, 7)
            print('')
            print(f'Seu ataque causou um dano de {thunderstorm}hp em cada goblin.')
            gob1Life = gob1Life - thunderstorm
            gob2Life = gob2Life - thunderstorm
            parcialVidas()

            if (gob1Life > 0):
                print('=====O turno do Goblin1=====')
                atakgob1 = random.randint(0, 3)
                life = life - atakgob1
                print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
                parcialVidas()

            if (gob2Life > 0):
                print('=====O turno do Goblin2=====')
                atakgob2 = random.randint(0, 3)
                life = life - atakgob2
                print(f'O ataque do Goblin2 causou {atakgob2} de dano.')
                parcialVidas()

            ataques: int = 0
            inimigo: int = 0

            if (gob1Life > 0) or (gob2Life > 0):
                while (ataques != 1) and (ataques != 2) and (ataques != 3):
                    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
                time.sleep(1.5)
            if ataques == 1:
                while (inimigo != 1) and (inimigo != 2):
                    inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))


        elif ataques == 3:
            printLbL("""Ao analisar rapidamente a situação você usou a névoa do ambiente para disfarçar\n 
            seu ataque mortal. Uma névoa venenosa sobe em volta daqueles goblins e os envenena.\n""")
            poisoncloud = random.randint(1, 5)
            print(f"""Seu ataque causou um dano de {poisoncloud}hp em cada goblin.""")
            gob1Life = gob1Life - poisoncloud
            gob2Life = gob2Life - poisoncloud
            poisoneffect = random.randint(1,2)
            gob1Life = gob1Life - poisoneffect
            gob2Life = gob2Life - poisoneffect
            print('')
            printLbL(f"""A névoa realmente infectou aqueles goblins. Eles sofreram mais um dano de {poisoneffect}hp por efeito do veneno.\n""")
            parcialVidas()

            if (gob1Life > 0):
                print('=====O turno do Goblin1=====')
                atakgob1 = random.randint(0, 3)
                life = life - atakgob1
                print(f'O ataque do Goblin1 causou {atakgob1} de dano.')
                parcialVidas()

            if gob2Life > 0:
                print('=====O turno do Goblin2=====')
                atakgob2 = random.randint(0, 3)
                life = life - atakgob2
                print(f'O ataque do Goblin2 causou {atakgob2} de dano.')
                parcialVidas()

            ataques: int = 0
            inimigo: int = 0

            if (gob1Life > 0) or (gob2Life > 0):
                while (ataques != 1) and (ataques != 2) and (ataques != 3):
                    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
                time.sleep(1.5)
            if ataques == 1:
                while (inimigo != 1) and (inimigo != 2):
                    inimigo = int(input('O ataque será no Goblin1 ou Goblin2? [1]/[2]: '))


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
    diante de meros goblins. Vamos! Você precisa se recuperar para se encontrar com o rei.\n""")
    elif (15 > life > 1):
        print(f"""Rápido! Você precisa de cuidados médicos com urgência! O grande {nome} quase 
    morreu pelcas mãos de pequenos goblins. Talvez você não seja tão bom como sua fama tem dito por aí.\n""")

if classe == 'cavaleiro':
    printLbL(f"""{nome} perdeu seus pais num ataque de tribos bárbaras quando ainda era bebê
            e foi criado por um capitão da guarda do castelo de Ravendor. Cresceu junto aos soldados e
            jurou que sempre iria proteger o reino destas ameaças.\n""")

    time.sleep(1)
    printLbL(f"""{nome} se tornou um excelente cavaleiro, leal e devoto ao trono de Ravendor,
            que hoje pertence a Fostan.
            Porém, Fostan não acredita totalmente nesta lealdade e convoca {nome} para uma missão especial.
            Algo sigiloso e extremamente arriscado.\n""")

    printLbL("""Ao aceitar a missão para provar sua lealdade ao rei Fostan,
            você foi enviado para a mística floresta de Fulgerit,
            onde encontra-se apenas as ruínas desta antiga cidade.\n""")

    luta1 = input(f"""Após entrar a floresta e caminhar por volta de meia hora numa antiga trilha
            que mal se enxerga os sinais dela, {nome} percebeu que estava sendo observado do alto das árvores.
            Duas criaturas pulam bem na sua frente. 
            Dois diabretes que se apresentam em sua forma normal e prontos para atacar.
            E agora, {nome}? Lutar/Fugir: \n""").strip().lower()

    if luta1 == 'lutar':
        ataques = int(input("""Lista de ataques:
        [1] Espada Longa (1d10)
        [2] Besta leve (1d8)
        [3] Rede (prende o inimigo por alguns turnos)
        Sua escolha: """))

    inimigo = int(input("""Qual diabrete você vai atacar 
    [1] O de trás 
    [2] O da frente
    Sua escolha: """))

    diablife1 = 10
    diablife2 = 10
    life = 70
    while (life > 0) and (diablife1 > 0 or diablife2 > 0):
        if ataques == 1 and inimigo == 1:
            longsword = random.randint(1, 10)
            printLbL(f"""{nome} num ato de coragem e agilidade puxa sua espada longa, gira o corpo 
            para trás e acerta um golpe no diabrete que ali estava o ameaçando.\n""")
            diablife1 -= longsword

            print(f"O seu golpe tira {longsword} hitpoints do Diabrete de trás(1).\n")
            parcialVidasCav()


            if diablife1 > 0:
                print('=====O turno do Diabrete1=====')
                atakdiab1 = random.randint(0, 3)
                life = life - atakdiab1
                print(f'O ataque do Diabrete1 causou {atakdiab1} de dano.')
                parcialVidasCav()

            if diablife2 > 0:
                print('=====O turno do Diabrete2=====')
                atakdiab2 = random.randint(0, 3)
                life = life - atakdiab2
                print(f'O ataque do Diabrete2ca causou {atakdiab2} de dano.')
                parcialVidasCav()

            ataques: int = 0
            inimigo: int = 0

            if (diablife1 > 0) or (diablife2 > 0):
                while (ataques != 1) and (ataques != 2) and (ataques != 3):
                    ataques = int(input('Escolha o seu ataque: [1], [2], [3]: '))
                time.sleep(1.5)
            if ataques == 1:
                while (inimigo != 1) and (inimigo != 2):
                    inimigo = int(input('O ataque será no Diabrete1 ou Diabrete2? [1]/[2]: '))


