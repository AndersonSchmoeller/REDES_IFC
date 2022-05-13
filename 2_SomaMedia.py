"""
Faça um programa que leia número inteiros maiores que zero. Quando o usuário informar o número zero,
o programa deverá apresentar quantos números foram digitados e a média deles.
"""
soma = int(0)
qtd = int(0)

num = int(input("Digite um número: \n >"))

while (num > 0):
    qtd = qtd + 1
    soma = soma + num
    num = int(input("Digite um número: \n >"))

media = (soma/(qtd))

print ("Soma:", soma)

print ("Media:", media)
