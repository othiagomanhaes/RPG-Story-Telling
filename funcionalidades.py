import sys
import time

def printLbL(texto):
    for c in texto:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.03)

def cavaleiro():
    global nome
    printLbL(f"""{nome} perdeu seus pais num ataque de tribos bárbaras quando ainda era bebê
        e foi criado por um capitão da guarda do castelo de Ravendor. Cresceu junto aos soldados e
        jurou que sempre iria proteger o reino destas ameaças.""")
    print('')
    time.sleep(1)
    printLbL(f"""{nome} se tornou um excelente cavaleiro, leal e devoto ao trono de Ravendor,
        que hoje pertence a Fostan.
        Porém, Fostan não acredita totalmente nesta lealdade e convoca {nome} para uma missão especial.
        Algo sigiloso e extremamente arriscado.""")

    printLbL("""Ao aceitar a missão para provar sua lealdade ao rei Fostan,
        você foi enviado para a mística floresta de Fulgerit,
        onde agora apenas se encontra somente as ruínas desta cidade.""")
    print('')

    luta1 = input(f"""Após entrar a floresta e caminhar por volta de meia hora numa antiga trilha
        que mal se enxerga os sinais dela, {nome} percebeu que estava sendo observado do alto das árvores.
        Duas criaturas pulam bem na sua frente. E agora, {nome}? Lutar/Fugir: """).strip().lprintLbL(f"""{nome} perdeu seus pais num ataque de tribos bárbaras quando ainda era bebê
        e foi criado por um capitão da guarda do castelo de Ravendor. Cresceu junto aos soldados e
        jurou que sempre iria proteger o reino destas ameaças.""")
    print('')
    time.sleep(1)
    printLbL(f"""{nome} se tornou um excelente cavaleiro, leal e devoto ao trono de Ravendor,
        que hoje pertence a Fostan.
        Porém, Fostan não acredita totalmente nesta lealdade e convoca {nome} para uma missão especial.
        Algo sigiloso e extremamente arriscado.""")

    printLbL("""Ao aceitar a missão para provar sua lealdade ao rei Fostan,
        você foi enviado para a mística floresta de Fulgerit,
        onde agora apenas se encontra somente as ruínas desta cidade.""")
    print('')

    luta1 = input(f"""Após entrar a floresta e caminhar por volta de meia hora numa antiga trilha
        que mal se enxerga os sinais dela, {nome} percebeu que estava sendo observado do alto das árvores.
        Duas criaturas pulam bem na sua frente. E agora, {nome}? Lutar/Fugir: """).strip().lower()
