# PROPÓSTA DA ATIVIDADE: Identificar se os batimentos estão ade3quados, acima ou abaixo do normal para a idade do usuário.

batimentos = int(input("Informe seus batimentos cardíacos: "))
idade = int(input("Informe sua idade: "))

if idade <= 2:
    if batimentos >= 120 and batimentos <= 140:
        print("ADEQUADA!")
    else:
        print("INADEQUADA!")
        if batimentos > 140:
            print("Batimentos acima do adequado!")
        elif batimentos < 120:
            print ("Batimentos abaixo do adequado!")
elif idade >= 8 and idade <= 17:
    if batimentos >= 80 and batimentos <= 100:
        print("ADEQUADA!")
    else:
        print("INADEQUADA!")
        if batimentos > 100:
            print("Batimentos acima do adequado!")
        elif batimentos < 80:
            print ("Batimentos abaixo do adequado!")
elif idade >= 18 and idade <= 60:
    if batimentos >= 70 and batimentos <= 80:
        print("ADEQUADA!")
    else:
        print("INADEQUADA!")
        if batimentos > 80:
            print("Batimentos acima do adequado!")
        elif batimentos < 70:
            print ("Batimentos abaixo do adequado!")
elif idade >= 60:
    if batimentos >= 50 and batimentos <= 60:
        print("ADEQUADA!")
    else:
        print("INADEQUADA!")
        if batimentos > 60:
            print("Batimentos acima do adequado!")
        elif batimentos < 50:
            print ("Batimentos abaixo do adequado!")
else:
    print("NÃO EXISTEM DADOS PARA A IDADE INFORMADA!")