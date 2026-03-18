notas = [] for i in range(3):    
 valor = float(input(f"Digite a {i+1}ª nota: "))    
  notas.append(valor)  media_inicial = sum(notas) / len(notas)
   print("Notas iniciais:", notas) print("Média inicial:", media_inicial)  menor = min(notas)                     
  # encontra a menor nota indice_menor = notas.index(menor)     
   
 # pega o índice da menor nota
     nova_nota = float(input("Digite a nova nota para substituir a menor: "))
     notas[indice_menor] = nova_nota        
  # substitui no índice correto 
     notas.sort()  media_final = sum(notas) / len(notas) 
     print("Notas atualizadas e ordenadas:", notas)
     print("Nova média:", media_final)