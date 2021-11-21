import sqlite3  #Linha 1

def cadastraNovoCliente():
    print("---------------------")
    print("CADASTRA NOVO CLIENTE")
    print("---------------------")
    nome  = input("NOME: ")
    cpf   = input("CPF: ")
    email = input("E-mail: ")
    # insere no banco

def listarClientes():
    print("LISTA CLIENTES")
    #
    clientes = []  # implementar recuperação do banco
    for linha in clientes:
        print("--------------------------")
        print("Id:", linha[0])
        print("Nome:", linha[1])
        print("CPF:", linha[2])
        print("E-mail:", linha[3])
        print("--------------------------")

def removerCliente():
    print("---------------------")
    print(" REMOÇÃO DO CLIENTE ")
    print("---------------------")
    id = input("Informe o id a ser removido: ")
    # remove no banco

def atualizarCliente():
    print("---------------------")
    print(" ATUALIZAR CLIENTE ")
    print("---------------------")
    id = input("Informe o id do cliente: ")
    novoNome = input("Nome: ")
    novoCPF = input("CPF: ")
    novoEmail = input("E-mail: ")
    # realiza update no banco


# Menu
opcao = 1
while (opcao!=9):
    print("CADASTRO DE CLIENTES")
    print("--------------------")
    print(" Menu de Opções")
    print("   1. Cadastrar novo cliente")
    print("   2. Lista clientes")
    print("   3. Atualizar cliente")
    print("   4. Remover cliente")
    print("   9. SAIR")

opcao = int(input("Informe a opção desejada: "))

if (opcao==1):
    cadastraNovoCliente()
elif (opcao==2):
    listarClientes()
elif (opcao==3):
    atualizarCliente()
elif (opcao==4):
    removerCliente()
elif (opcao==9):
    print("Tchau!")
else:
    print("Opção invalida!")

