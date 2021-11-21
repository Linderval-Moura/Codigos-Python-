import pickle

def carregaDados():
    arquivo = open("arquivo.dat","wb")
    cad = pickle.load(arquivo)
    arquivo.close()
    return cad
    