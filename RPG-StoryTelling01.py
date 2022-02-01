import time
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
    print('')
    if classe != 'mago' and classe != 'cavaleiro':
        print('Classe inválida. Tente novamente entre Mago ou Cavaleiro.')
print('')

if classe == 'cavaleiro':
    nome = str(input("""Então você será um bravo Cavaleiro, ótima escolha! 
E como será o teu nome? """))

else:
    nome = str(input("""Vejo que optou por ser um poderoso Mago, ótima escolha! 
E como será o teu nome? """))