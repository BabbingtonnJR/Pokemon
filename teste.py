import random
nome = input("Olá, bem vindo ao mundo Pokémon, eu sou o Professor Carvalho, um pesquisador Pokémon.\nQual seu nome?: ")
introducao = print(f"Ah, então você é {nome}, preprare-se para embarcar numa emocionante jornada Pokémon!")
pokedex = []
mato = ["Swablu", "Caterpie", "Pidgeon", "Oddish", "Venonat"]
caverna = ["Zubat", "Woobat", "Geodude", "Sandslash", "Diglett"]
indiceM = 0
indiceC = 0
while True:
    indiceM = random.randint(0,4)
    indiceC = random.randint(0,4)
    capturaC = random.randint(0,34)
    capturaM = random.randint(0,49)
    caverna[indiceC] = (caverna[indiceC])
    mato[indiceM] = (mato[indiceM])
    acao = int(input("Qual sua próxima ação?\n1. Ir para a caverna\n2. Ir para o mato\n3. Abrir a Pokédex\n4. Sair\nEscolha a sua opção: "))
    if acao == 4:
        print("Até mais")
        break
    if acao == 1:
        cavernaCaptura = input(f"Você entrou na caverna e encontrou um {caverna[indiceC]}!\nVocê quer capturar esse Pokémon? (s/n): ")
        if cavernaCaptura == "s":
            if capturaC % 2 == 0:
                pokedex.append(caverna[indiceC])
                print("Você capturou esse pokémon com sucesso! ")
            else:
                print("Você não conseguiu capturar esse pokémon")
                continue
    if acao == 2:
        matoCaptura = input(f"Você entrou na caverna e encontrou um {mato[indiceM]}!\nVocê quer capturar esse Pokémon? (s/n): ")
        if matoCaptura == "s":
            if capturaM % 2 == 0:
                pokedex.append(mato[indiceM])
                print("Você capturou esse pokémon com sucesso!")
            else:
                print("Você não conseguiu capturar esse pokémon")
                continue
    if acao == 3:
        print(pokedex)
    else:
        print("Opção inválida, tente novamente")