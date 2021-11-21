import sqlite3  #Linha 1

def cadastraNovoCliente():
    print("---------------------")
    print("CADASTRA NOVO CLIENTE")
    print("---------------------")
    nome  = input("NOME: ")
    cpf   = input("CPF: ")
    email = input("E-mail: ")
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO cliente (nome, cpf, email) VALUES (?, ?, ?)", [nome, cpf, email])
    con.commit()  #Enviar as consultas
    con.close()

def listarClientes():
    print("LISTA CLIENTES")
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cliente;")
    clientes = cursor.fetchall()  #Recupera todos os registros
    con.commit()
    con.close()
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
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM cliente WHERE id=?", [id])
    con.commit()
    con.close()

def atualizarCliente():
    print("---------------------")
    print(" ATUALIZAR CLIENTE ")
    print("---------------------")
    id = input("Informe o id do cliente: ")
    novoNome = input("Nome: ")
    novoCPF = input("CPF: ")
    novoEmail = input("E-mail: ")
    # realiza update no banco
    con = sqlite3.connect("meu_banco.db")
    cursor = con.cursor()
    cursor.execute("UPDATE cliente SET nome=?, cpf=?, email=? WHERE id=?", [novoNome, novoCPF, novoEmail, id])
    con.commit()
    con.close()


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

