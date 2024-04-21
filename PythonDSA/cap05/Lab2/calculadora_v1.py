# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Bem vindo a Calculadora em Python *******************")

num1 = float(input("Entre com o primeiro valor"))
num2 = float(input("Entre com o segundo valor"))
operacao = str(input("Agora, escolha entre as operações: +, -, / ou *"))

def soma(x,y):
 resultado = x+y
 return(resultado)

if operacao == "+":
    resultado = soma(num1, num2)
    print ("O resultado desta operação é: ", resultado)

 #autor: neste laboratório quis fazer a calculadora de uma maneira diferente. utilizei funções para chamar as operações 
 # e loops while para validar as entradas.





