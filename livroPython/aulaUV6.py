nota1 = float(input("nota 1 pls:"))
nota2 = float(input("nota 2 pls:"))

#%d
#%f
#processar

media = (nota1 + nota2) /2

#if (media >= 7):
#    print("aluno aprovado")
#    print(" sua media é.. %s" %(media))
#else
#    print("você Precisa melhorar :'c")
 #   print("Sua media é %s." %(media))

if (media >= 7):
    situacao = "APROVADO"

elif (media >=4 and media <7):
    situacao = "EXAME FINAL"

else:
    Situcao = "REPROVADO"

