import time
import os

lista = []
arq2 = open("DadosClientes.csv", "r")
lista = arq2.readlines()
arq2.close()

def inserir(nome, telefone, email):
    dados = nome+";"+telefone+";"+email+"\n"
    lista.append(dados)

    print("Cliente adicionado com sucesso!")
    time.sleep(2)

    arq = open("DadosClientes.csv", "w")
    tam = len(lista)

    for i in range(tam):
        arq.write(lista[i])
    arq.close()


def menu():
    menuOPC = """
    ╔════════════════════════════════════╗
    ║  1° ➜ Cadastro cliente             ║
    ║  2° ➜ Excluir cliente              ║
    ║  3° ➜ Ver total de clientes        ║
    ╚════════════════════════════════════╝"""
    print(menuOPC)


    opcao = int(input("O que deseja fazer: "))

    if opcao == 1:
        cad = """
        ┌────────────────┐
         ❯  -CADASTRO-  ❮
        └────────────────┘"""
        print(cad)

        nome = str(input("Nome: "))
        tel = str(input("Telefone: "))
        email = str(input("E-mail: "))
        inserir(nome,tel,email)

    elif opcao == 2:
        rem = """
        ┌─────────────────┐
         ❯   -REMOVER-   ❮
        └─────────────────┘"""
        print(rem)
        print('{:^35}'.format(" ☢ IMPORTANTE ☢ "))
        print("Em hipótese alguma remova o indice zero.")

        tam = len(lista)
        for i in range(tam):
            print(i, "-", lista[i])
        excluir = int(input("Qual deseja excluir: "))
        lista.pop(excluir)
        print("Cliente removido com sucesso!")

        arq = open("DadosClientes.csv", "w")
        tam = len(lista)

        for i in range(tam):
            arq.write(lista[i])
        arq.close()
        time.sleep(7)

    elif opcao == 3:
        tam = len(lista)
        for i in range(tam):
            print(i, "-", lista[i])
        arq = open("DadosClientes.csv", "w")
        tam = len(lista)

        for i in range(tam):
            arq.write(lista[i])
        arq.close()
        sair = input("Aperte [E N T E R] para sair.")
