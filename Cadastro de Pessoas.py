import time
posiçao = 1
base_dados = []
contador = a = 0
pessoa_c = 0
print(f"{'Bem Vindo - CADASTRO DE PESSOAS':-^50}\n\n") 
while True: #Testando nessa linha
    print("escolha uma opção! ")
    print("\n[1] - Cadastrar pessoa ")
    print("[2] - Motrar os dados do sistema em ordem alfabetica",)
    print("[3] - Finalizar programa")
    op = str(input("\nDigite sua opção : " ))
    print('-='*26)
    if op == "1": # CADASTRO DE PESSOAS
        cadastro = []
        print("\nOk ,então vamos ao cadastro! ")
        nome = str(input("\nDigite o nome completo da pessoa : ")).strip().capitalize()
        idade = int(input("Digite a idade da pessoa : "))
        telefone = int(input("Digite o telefone da pessoa : "))
        cadastro.insert(0,nome)
        cadastro.insert(1,idade)
        cadastro.insert(2,telefone)
        print("\nEsses são os dados da pessoa , Nome : {} , Idade : {} anos ,Telefone : {}".format(cadastro[0],cadastro[1],cadastro[2]))
        base_dados.append(cadastro)
        print("\nPessoa cadastrada com sucesso!")
        time.sleep(2)
    elif op == "2": # ORDEM ALFABETICA
        contador = 0
        posiçao = 1
        base_alfabetica = sorted(base_dados)
        print(base_alfabetica)
        print("\nOs dados estão em ordem alfabética! ")
        time.sleep(2)
        a = 0
        while a == 0:
            try:
                print("\nEsse é o nome da {}° pessoa : {}".format(posiçao,base_alfabetica[contador][0].capitalize()))
                print("Essa é a idade da {}º pessoa : {} anos".format(posiçao,base_alfabetica[contador][1]))
                print("Esse é o telefone da {}° pessoa : {}".format(posiçao,base_alfabetica[contador][2]))
                contador = contador + 1
                posiçao = posiçao + 1
            except:
                a = 1
                print("\nEsses são todos os dados do sistema!")
                time.sleep(2)              
            (4)
    elif op == "3":
        break
        print("Finalizando programa...")
        time.sleep(3)
    else:
        print("Digite apenas números entre 1 e 3")    
        time.sleep(2)
        
