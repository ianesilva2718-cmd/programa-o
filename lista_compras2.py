lista = []  # começamos com uma lista vazia
for i in range(4):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(numero)  # adicionamos cada número à lista

# 2. Mostrar o tamanho da lista antes da remoção
print("Lista criada:", lista)
print("Tamanho antes da remoção:", len(lista))  # len() retorna o tamanho

# 3. Ler o valor alvo
alvo = int(input("Digite um valor alvo para remover: "))

# 4. Teste de pertencimento com 'in' e remoção
if alvo in lista:  # verifica se o alvo está na lista
    lista.remove(alvo)  # remove o primeiro alvo encontrado
    print(f"O valor {alvo} foi removido.")
else:
    print(f"O valor {alvo} não está na lista.")

# 5. Mostrar o tamanho da lista depois da remoção
print("Lista atualizada:", lista)
print("Tamanho depois da remoção:", len(lista))