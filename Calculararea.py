
print('''
[a] = Calcular área do triângulo\n[b] = Calcular área do quadrado\n[c] = Calcular área do círculo
''')

opc = str(input("Digite a opção escolhida: ")).lower()

if opc == 'a':
    print("-"*14,"Área Triângulo","-"*14,)
    b = int(input("Digite a base do triangulo: "))
    h = int(input("Digite a altura do triangulo: "))

    print("Área do Triângulo:",(b*h)/2)
elif opc == 'b':
    print("-"*14,"Área Quadrado","-"*14,)
    lado = int(input("Digite o lado do quadrado: "))

    prmt = lado * 4 
    area = lado * lado
    print("Área: %a"%(area))
    print("Perimetro: %a"%(prmt))

elif opc == 'c':
    print("-"*14,"Área do Círculo","-"*14,)


    r = float(input("Digite a área do Círculos em metros: "))
    a = 3.14 * (r * r)
    print("A área do círculo é %a m²"%(a))
