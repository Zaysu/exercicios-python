#entrada de dados
salaArea = float(input("digite area da sala(M²)"))
cozinhaArea = float(input("digite area da cozinha(M²)"))
banheiroSocialArea = float(input("digite area da banheiro(M²)"))
quartoArea = float(input("digite area da Quarto1(M²)"))
quarto2Area = float(input("digite area da Quarto2(M²)"))

#processamento
area_total = salaArea + cozinhaArea + banheiroSocialArea + quartoArea + quarto2Area

if (area_total >= 100):
    precoVenda = area_total * 1200

else:
    precoVenda = area_total * 1700

    print("area total %d" % (area_total,precoVenda))