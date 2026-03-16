# criando tuplas 
coordenadas = (10,20)
dias = ("segunda", "terça","quarta","quinta","sexta")

# acessando elementos 
print("x:",coordenadas[0], "| Y:", coordenadas[1])


# Slicing (fatiamento) em tuplas 
 print("primeiros 3 dias:", dias [:3])

#tamanho
print("tamanho da tupla'dias':", len(dias))

# verificar se um elemento está em tupla 
print("tem 'segunda'?", "segunda" in dias)

# contagem e indice em tuplas
print ("contagem de 'terça':", dias.count("terça"))
print ("indice de 'quarta':", dias.index("quarta"))