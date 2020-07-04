import time
import os
from add_fornecedor import *
from cad_clientes import *
from estoque import *

menu_tela = """
         SOMENTE O GERENTE PODE ACESSAR
    ╔══════════════════════════════════════╗
    ║  1 ➜ Cadastrar fornecedores          ║
    ║  2 ➜ Clientes                        ║
    ║  3 ➜ Estoque                         ║
    ║                                      ║
    ║  4 ➜          SAIR                   ║
    ╚══════════════════════════════════════╝ """

opcao = 0
while True:
    os.system("clear")
    print(menu_tela)

    opcao = int(input("O que deseja: "))

    if opcao == 1:
        add_fornecedor()
    elif opcao == 2:
        menu()
    elif opcao == 3:
        menu_estoque()
    elif opcao == 4:
        print("Saindo do sistema...")
        exit()
    else:
        print("Tente novamente em: ", end="")
        for c in range(5, -1, -1):
            time.sleep(1)
            print(c)
