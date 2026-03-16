frutas = ["maça", "banana", "uva"]
numeros = [1,2,3,4]

# acessando elementos 
print ("primeira fruta:", frutas [0])   #"maçã"#
print("última fruta:", frutas[-1])      # "uva"

# alterando elementos 
frutas[1] = "banana-nanica"
print("apos alterar:", frutas)

# adicionando elementos 
frutas.append("morango")    #adiciono ao final
frutas.insert(1, "pera")    #adiciona no posição 1 

print("apos adicionar:", frutas)

# removendo elementos 
frutas.remove ("uva")      # remove pelo valor 
ultima = frutas.pop()      # remove e retorna o ultimo
print("após remover 'uva' e pop():", frutas, "ultimo removido", ultima)