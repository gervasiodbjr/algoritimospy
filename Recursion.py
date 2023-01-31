# FACTORIAL
# internal function => num * factorial(num-1)
# Ex.: factorial(3) = 6
# Ex.: factorial(4) = 24
# Ex.: factorial(5) = 120
# 
# Casos base: f(0) = 1
#             f(1) = 1
# Recursividade: f(n) = n * f(n-1)
def factorial(num):
    if num <= 1:
        return 1;
    else:
        return num * factorial(num - 1);
    
# print(factorial(4))

# Defina a função expo que calcule 'n' elevado a 'e' positivo
# Ex.: 3^2 = 9
# Ex.: 3^3 = 27
# Ex.: 4^5 = 1024
# 
# Caso base: f(n, 0) = n^0 = 1
# Caso recursivo: f(n, 1) = n^1 * n^0 = n * f(n, 0) = n * f(n, e - 1)
def expo(n,e):
    if e == 0:
        return 1
    else:
        return n * expo(n, e - 1)

# print(expo(3,2))
# print(expo(3,3))
# print(expo(4,5))



# Defina a função digito_mais_relevante que recebe como argumento um número natural e devolve o dígito mais à esquerda.
# Ex.: digito_mais_relevante(345678039) = 3
# Ex.: digito_mais_relevante(45678039) = 4
# 
# Caso base: f(3) = n
# Recursividade: f(34) = n // 10
def digito_mais_relevante(n):
    if n // 10 < 1:
        return n
    else:
        return digito_mais_relevante(n // 10)
    
# print(digito_mais_relevante(345678039))
# print(digito_mais_relevante(45678039))



# Defina a função soma_digitos que recebe como argumento um número natural e devolve o somatório dos seus digitos.
# Ex.: soma_digitos(1234) = 10
# Ex.: soma_digitos(2345) = 14
# Ex.: soma_digitos(23456) = 20
# Ex.: soma_digitos(234567) = 27
# 
# Caso base: f(2) = 2
# recursivo: f(23) = 2 + 3 => (n // 10) + (n % 10)
def soma_digitos(n):
    if n // 10 <= 0:
        return n
    else:
        return soma_digitos(n // 10) + soma_digitos(n % 10)
    
print(soma_digitos(1234))
print(soma_digitos(2345))
print(soma_digitos(23456))
print(soma_digitos(234567))

