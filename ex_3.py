#PROPÓSTA DA ATIVIDADE: Identificar os votos de cada colaborador e informar qual console será escolhido na votação.

voto1 = input("Informe qual console deseja ganhar: PLAYSTATION, XBOX ou NINTENDO? ")
voto2 = input("Informe qual console deseja ganhar: PLAYSTATION, XBOX ou NINTENDO? ")
voto3 = input("Informe qual console deseja ganhar: PLAYSTATION, XBOX ou NINTENDO? ")
voto4 = input("Informe qual console deseja ganhar: PLAYSTATION, XBOX ou NINTENDO? ")
voto5 = input("Informe qual console deseja ganhar: PLAYSTATION, XBOX ou NINTENDO? ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("OPÇÃO INVÁLIDA, voto anulado!")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("OPÇÃO INVÁLIDA, voto anulado!")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("OPÇÃO INVÁLIDA, voto anulado!")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("OPÇÃO INVÁLIDA, voto anulado!")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("OPÇÃO INVÁLIDA, voto anulado!")

print("O placar é igual a:\nPLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if playstation > xbox and playstation > nintendo:
    print("O console ganhador foi: PLAYSTATION")
elif xbox > playstation and xbox > nintendo:
    print("O console ganhardor foi: XBOX")
elif nintendo > playstation and nintendo > xbox:
    print("O console ganhador foi: NINTENDO")
else:
    print("Houve empate, favor realizar a votação novamente!")