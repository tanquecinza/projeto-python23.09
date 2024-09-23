"""""
def area_circulo(raio, pi):
    area = pi*raio**2
    return area

raio = float(input("digite um raio"))
area = area_circulo(raio, 3.14)
print("a area do circulo e:", area)
"""
"""""
def soma(a,b):
    resultado = a + b
    return resultado

def subtracao(a,b):
    resultado = a - b
    return resultado
 
def multiplicaçao(a,b):
    resultado = a * b
    return resultado

def divisao(a,b):
   resultado = a / b
   return resultado

"""""
"""""
def eh_par(numero):
    if numero%2==0:
        return True
    else:
        return False

numero= eh_par(1)
print(numero)
"""""
"""""
def fharenheit_para_celsius(f):
    c = 5/9 * (f - 32)
    return c

graus = fharenheit_para_celsius (2)
print (graus)

"""""
"""""
def fibonacci(n):
    a = 0
    b = 1

    for i in range (n):
        auxiliar = a
        a = b
        b = auxiliar + b
    return b
print( fibonacci)
"""""
"""""
def fatorial(n):
    fat = 1
    for i in range(n):
        fat = fat * (i + 1)
    return fat

numero = int(input("digite um numero:"))
print(fatorial(numero))
"""""
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

a = int(input("digite um numero:"))
b = int(input("digite um numero:"))

print

def calculadora(a,b,  operacao):
    if operacao == "+":
        resultado = soma1
    elif operacao == "-":
        resultado = menos1
    elif operacao == "*":
        resultado = vezes1
    elif operacao == "/":
        resultado = divisao1

while True:
    print("calculadora")
    print("___________")
    numero1 = float(input("digite um numero"))
    operacao = input("digite uma operacao(+, -, *, /)")
    numero2 = float(input("digite outro numero:"))
"""""

























