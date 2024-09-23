"""""
def soma1(a,b):
    resultado = a + b
    return resultado
def menos1(a,b):
    resultado = a - b
    return resultado
def vezes1(a,b):
    resultado = a * b
    return resultado
def divisao1(a,b):
   resultado = a / b
   return resultado

def calculadora(a,b, operacao):
    if operacao == "+":
        resultado = soma1(a,b)
    elif operacao == "-":
        resultado = menos1(a,b)
    elif operacao == "*":
        resultado = vezes1(a,b)
    elif operacao == "/":
        resultado = divisao1(a,b)
    return resultado

while True:
    print("calculadora")
    print("___________")
    numero1 = float(input("digite um numero:"))
    operacao = input("digite uma operacao:(+, -, *, /)")
    numero2 = float(input("digite outro numero: "))
    soma = calculadora(numero1, numero2, operacao)
    print ("")
    print ("resultado =",soma)
    print ("_________")
    print ("")
"""""

"""""
minha_lista = [1,2,3,4,5]
minha_lista.append(6)
minha_lista.append(7)
print(minha_lista)
"""""
"""""
tupla_mista = (1,"achou",3.14)
segundo_elemento = tupla_mista[1]
print(tupla_mista)
print ("o segundo elemento da tupla é:",segundo_elemento)

"""""
"""""
minha_lista = [37, 35.015592, "x6Fhj", False, 17, 47.292571, "jrwbl", True, 98, 1,864]
print ("lista com o true:",minha_lista)
minha_lista.remove(True)
print("lista atualizada sem true:",minha_lista)
"""""
"""""
numero1 = int(input("digite um numero"))
numero2 = int(input("digite um numero"))

if(numero1 == numero2):
    print("numeros iguais")
elif(numero1>numero2):
    print(numero1, "maior que", numero2)
else:
    print(numero2, "maior que", numero1)
"""""