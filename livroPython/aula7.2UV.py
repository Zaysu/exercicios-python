quantida int(input("Qual quantidade ? "))

soma - 0
leitura = 0

while (leitura < quantida):
    preco = float(input("qual preço?"))
    soma = soma + preco
    leitura = leitura + 1

    media = soma / quantida

    print("media %d" % (media))