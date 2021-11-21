# Um sistema de gerenciamento de lista de contato
# Nome, Telefone, Email

contatos = dict()

def cabecalho():
    print("---------------------------------------------")
    print("e-Contato: sua agenda de contatos Eletronica!")
    print("---------------------------------------------")

def menu_principal():
    print(" Menu do Sistema:")
    print("    1. Novo Contato")
    print("    2. Listar Contatos")
    print("    3. Remover Contato")
    print("    4. Atualizar Contato")
    print("    9. Sair")

def sair():
    print("Ate logo!")

def opcao_invalida():
    print("Opcao inválida!")    

def cadastro_contato(contatos_dict):
    print("Novo Contato")
    nome = input("Nome:")
    telefone = input("Telefone:")
    email = input("E-mail:")
    contatos_dict[nome] = [telefone, email]
    print(" >>> Cadastro armazenado com sucesso!")

def listar_contatos(contatos_dict):
    print("Lista de Contatos\n")

    print("-----------------")
    i = 0
    for (k,v) in contatos_dict.items():
        print("Nome:",k)
        print("Telefone:",v[0])
        print("E-mail:",v[1])
        print("-----------------")
        i = i+1
    print("Qtd de contatos:",i)
    

def remover_contato():
    print("Remover Contato")
    print("Em breve")

def atualizar_contato():
    print("Atualizar Contato")
    print("Em breve")    

# Programa Principal
opcao = 1
while (opcao!=9):
    cabecalho()
    menu_principal()
    opcao = int(input("Digite sua opção:"))
    if (opcao==1):
        cadastro_contato(contatos)
    elif(opcao==2):
        listar_contatos(contatos)
    elif(opcao==3):
        remover_contato()
    elif(opcao==4):
        atualizar_contato() 
    elif(opcao==9):
        sair()
    else:
        opcao_invalida() 