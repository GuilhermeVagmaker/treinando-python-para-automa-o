tarefa = []

def adicionar_tarefa():
  titulo = input("Escreva uma tarefa: ")
  tarefa.append({
    "titulo": titulo,
    "concluida": False
  }) 
  print("tarefa adicionada com sucesso!!")
  

def listar_tarefa():
    if not tarefa:
      print("Nenhuma tarefa criada ate o momento...")
      return
    for i, tarefas in enumerate(tarefa, start = 1):
      status = "Concluida" if tarefas["concluida"] else "Ainda não concluida"
      print(f"\n{i}. Tarefa: {tarefas['titulo']} Status: {status}")

def concluir_tarefa():
    
    if not tarefa:
        print("Nenhuma tarefa criada ate o momento...")
        return
    for i, tarefas in enumerate(tarefa, start = 1):
      status = "Concluida" if tarefas["concluida"] else "Ainda não concluida"
      print(f"\n{i}. Tarefa: {tarefas['titulo']} Status: {status}")
         
    tarefa_concluida = input("\nqual das tarefas você concluiu? ")
      
    if not tarefa_concluida.isdigit():
      print("Apenas números é valido")
      return
    
    indice = int(tarefa_concluida) - 1
    
    if indice < 0 or indice >= len(tarefa):
      print("Opção inválida!")
      return
    
    if tarefa[indice]["concluida"]:
      print("tarefa já concluida")
    else:
      tarefa[indice]["concluida"] = True
      print("\nTarefa concluida com sucesso")
      return
      
while True:
  print("\n1 - adicionar tarefa")
  print("2 - listar tarefa")
  print("3 - Concluir tarefa")
  print("4 - Encerrar")
  
  opcao = input("Escolha: ")
  
  if opcao == "1":
    adicionar_tarefa()
  elif opcao == "2":
    listar_tarefa()
  elif opcao == "3":
    concluir_tarefa()
  elif opcao == "4":
    print("Encerrando... Aguarde")
    
    with open("tarefas.txt", "w") as arquivo:
      arquivo.write("TAREFAS\n")
      arquivo.write("====================================================\n")
      
      for i in tarefa:
        status = "Concluida" if i["concluida"] else "Ainda não concluida"
        
        arquivo.write(f"Tarefa: {i['titulo']}\n")
        arquivo.write(f"Status: {status}\n")
        arquivo.write("---------------------------------------------------\n")
      
      print("arquivo salvo com sucesso!!!!")
    break
  else:
    print("opção invalida, Escolha um dos numeros acima")
    

      
     
     
    