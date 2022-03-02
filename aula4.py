frase = 'lis,Ta De nOm,es'
lista_nomes = ['joao', 'junior', 'lol', 'zaysu', 'crush', 'joao']

lista_nomes.append('geraldina')
lista_nomes.append('laura')
lista_nomes.remove('lol')
lista_nomes.insert(3, 'fran')

contador_nomes = lista_nomes.count('joao')

print(frase[0:10:2])
print(lista_nomes[0:6])
print(lista_nomes)
print(contador_nomes)

print(len(lista_nomes))


print(lista_nomes.pop() )

print(frase.lower())

separando_frase = frase.split(',')
print(separando_frase)

dev_jr = frase+ 'Dev Junior'
print(dev_jr)