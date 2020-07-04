import time
import os
import matplotlib.pyplot as plt
import pandas as pd

lista = []
arq2 = open("DadosProd.csv", "r")
lista = arq2.readlines()
arq2.close()

def inserir(fornecedor,nome,quantidade,tipo,validade):
    dados = fornecedor+","+nome+","+quantidade+","+tipo+","+validade+"\n"
    lista.append(dados)

    print("Produto adicionado ao estoque!")
    time.sleep(2)

    arq = open("DadosProd.csv", "w")
    tam = len(lista)

    for i in range(tam):
        arq.write(lista[i])
    arq.close()

def menu_estoque():
    menu = """
    ╔════════════════════════════════════╗
    ║  1° ➜ Adicionar produtos           ║
    ║  2° ➜ Ver produtos                 ║
    ║  3° ➜ Gráfico do Estoque           ║
    ║  4° ➜       REMOVER                ║
    ╚════════════════════════════════════╝"""

    print(menu)

    opcao = int(input("O que deseja fazer: "))
    os.system("clear")

    if opcao == 1:
        card = """
        ┌─────────────────┐
         ❯  -Adicionar-  ❮
        └─────────────────┘"""
        print(card)

        fornecedor = str(input("Fornecedor: "))
        nome = str(input("Nome: "))
        quant = str(input("Quantidade em UN: "))
        tipo = str(input("Tipo: "))
        validade = str(input("Validade: "))
        inserir(fornecedor,nome,quant,tipo,validade)

    elif opcao == 2:

        df = pd.read_csv('DadosProd.csv')
        df.head()
        print(df)
        print("")
        sair = input("Aperte [E N T E R] para sair.")

    elif opcao == 3:

        df = pd.read_csv ('DadosProd.csv')
        product_data = df["Nome"]
        bug_data = df["Quantidade"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]


        df = pd.read_csv("DadosProd.csv",sep=",").set_index('Nome')


        for i in range(bug_data[1]):
            print(df)
            print("\nPara sair basta fechar o GRÁFICO")
            break

        plt.pie(bug_data , labels=product_data , autopct='%0.1f%%', startangle=140)
        plt.title("Produto em estoque")
        plt.show()

    elif opcao == 4:
        rem = """
        ┌─────────────────┐
         ❯   -REMOVER-   ❮
        └─────────────────┘"""
        print(rem)
        print('{:^35}'.format(" ☢ IMPORTANTE ☢ "))
        print("Em hipótese alguma remova o indice zero.")

        tam = len(lista)
        for i in range(tam):
            print(i, "➜", lista[i])
        excluir = int(input("Qual produto excluir: "))
        lista.pop(excluir)
        print("Produto removido com sucesso!")

        arq = open("DadosProd.py", "w")
        tam = len(lista)

        for i in range(tam):
            arq.write(lista[i])
        arq.close()
        time.sleep(7)
    else:
        print("Valor inválido, tente novamente!")
        for c in range(5, -1, -1):
            time.sleep(1)
            print(c)
