"""
Faça um programa que apresente o menu abaixo. Ao escolher a opção um o programa deve imprimir na tela Você escolheu a opção 1" e assim para todas as opções. Caso digitar zero, o programa deverá emitir um mnensagem de encerramento e terminar. Caso o usuário digite algo fora do escopo o programa deverá mostrar "opção inválida".
Opção 1
Opção 2
Opção 3
Sair
"""
print ("Escolha uma opção: \n")
print ("1.\tOpção 1\n2.\tOpção 2\n3.\tOpção 3\n0.\tEncerrar")

op = int(input("\n >"))

while op!=0:
    if op == 1:
        print ("opção", op)
    elif op == 2:
        print ("opção", op)
    elif op == 3:
        print ("opção", op)
    else:
        print ("Opção Inválida")
    print ('Desejar selecionar mais uma opção?')
    print ("1.\tOpção 1\n2.\tOpção 2\n3.\tOpção 3\n0.\tEncerrar")
    op = int(input("\n >"))
