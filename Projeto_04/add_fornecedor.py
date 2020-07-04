import time

menu = """
    ╔════════════════════════════════════╗
    ║       Cadastro de Fornecedor       ║
    ╚════════════════════════════════════╝
"""

lista = []
arq2 = open("DadosFor.csv", "r")
lista = arq2.readlines()
arq2.close()

def inserir(empresa, nome, telefone, email):
    dados = empresa+";"+nome+";"+telefone+";"+email+"\n"
    lista.append(dados)

    print("Fornecedor adicionado com sucesso!")
    time.sleep(2)

    arq = open("DadosFor.csv", "w")
    tam = len(lista)

    for i in range(tam):
        arq.write(lista[i])
    arq.close()


def add_fornecedor():
    print(menu)

    empresa = str(input("Empresa: "))
    nome = str(input("Nome: "))
    tel = str(input("Telefone: "))
    email = str(input("E-mail: "))

    inserir(empresa,nome,tel,email)
