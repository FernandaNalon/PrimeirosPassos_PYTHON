# PROPÓSTA DA ATIVIDADE: Identificar a classe do passageiro e a condição de desconto que ele ganhará com base na quantidade de viajantes presentes da mesma família.

valor_bruto = float(input(" Digite o valor bruto da viagem: R$"))
categoria = (input("Digite a categoria de seus assentos, sendo: EC = economica, EX = executiva e PC = primeira classe: "))
viajantes = int(input("Digite a quantidade de passageiros: "))
valor_desc = 0

if categoria.upper() == "EC":
    if viajantes == 2:
        valor_desc = valor_bruto * 0.03
    elif viajantes == 3:
        valor_desc = valor_bruto * 0.04
    elif viajantes >= 4:
        valor_desc = valor_bruto * 0.05
elif categoria.upper() == "EX":
    if viajantes == 2:
        valor_desc = valor_bruto * 0.05
    elif viajantes == 3:
        valor_desc = valor_bruto * 0.07
    elif viajantes >= 4:
        valor_desc = valor_bruto * 0.08
elif categoria.upper() == "PC":
    if viajantes == 2:
        valor_desc = valor_bruto * 0.10
    elif viajantes == 3:
        valor_desc = valor_bruto * 0.15
    elif viajantes >= 4:
        valor_desc = valor_bruto * 0.20
else:
    print("Desconto não concedido, as informações não atendem aos requisitos!")

valor_liquido = valor_bruto - valor_desc
media_viajante = valor_liquido/viajantes

print("O valor bruto da viagem é de R${}".format(valor_bruto))
print("O valor do desconto recebido é de: R${}".format(valor_desc))
print("O valor a ser pago será de: R${}".format(valor_liquido))
print("O valor aproximado por viajante é de: R${}".format(media_viajante))