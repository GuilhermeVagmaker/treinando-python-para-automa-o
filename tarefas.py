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

def remover_tarefa():
    
    if not tarefa:
        print("Nenhuma tarefa criada ate o momento...")
        return
    for i, tarefas in enumerate(tarefa, start = 1):
      status = "Concluida" if tarefas["concluida"] else "Ainda não concluida"
      print(f"\n{i}. Tarefa: {tarefas['titulo']} Status: {status}")
         
    nmr_tarefa = input("\nqual das tarefas você concluiu? ")
      
    if not nmr_tarefa.isdigit():
      print("Apenas números é valido")
      return
    
    indice = int(nmr_tarefa) - 1
    
    if indice < 0 or indice >= len(tarefa):
      print("Opção inválida!")
      return
    
    remove_tarefa = tarefa.pop(indice)
    print(f"Tarefa removida: {remove_tarefa["titulo"]} - Tarefa removida com sucesso!!")
      
while True:
  print("\n1 - Adicionar tarefa")
  print("2 - Listar tarefa")
  print("3 - Concluir tarefa")
  print("4 - Remover tarefa")
  print("5 - Encerrar")
  
  opcao = input("Escolha: ")
  
  if opcao == "1":
    adicionar_tarefa()
  elif opcao == "2":
    listar_tarefa()
  elif opcao == "3":
    concluir_tarefa()
  elif opcao == "4":
    remover_tarefa()  
  elif opcao == "5":
    
    print("\n1 - Salvar arquivo")
    print("2 - Encerrar programa")
    
    sub_opcao = input("\nEscolha um dos numeros acima: ")
    
    if sub_opcao == "1":
      with open("tarefas.csv", "w") as arquivo:
        arquivo.write("Tarefa, Status\n")
        
        for i in tarefa:
          status = "Concluida" if i["concluida"] else "Ainda não concluida"  
          arquivo.write(
            f"{i['titulo']},{status}\n"
          )

        print("arquivo salvo com sucesso!!!!")
      break
    elif sub_opcao == "2":
      print("Encerrando programa... Aguarde")
      break
  else:
    print("\nopção invalida, Escolha um dos numeros acima")
    

      
     
     
    