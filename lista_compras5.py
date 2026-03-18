fila = ["Ana", "Bruno"]
print("Fila inicial:", fila)

# 2. Ler dois novos nomes e adicionar com extend()
novos = []
for i in range(2):
    nome = input(f"Digite o {i+1}º novo cliente: ")
    novos.append(nome)
fila.extend(novos)
print("Fila após chegadas:", fila)

# 3. Ler cliente prioritário e inserir na posição 1
prioritario = input("Digite o nome do cliente prioritário: ")
fila.insert(1, prioritario)
print("Fila após inserir prioritário:", fila)

# 4. Atender (remover e capturar) o primeiro da fila com pop(0)
atendido = fila.pop(0)
print("Cliente atendido:", atendido)
print("Fila após atendimento:", fila)
