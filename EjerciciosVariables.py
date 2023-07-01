entero = 1
flotante = 4.16
booleano = True
caracteres = "Hola"

#I
resultado =  caracteres + str(booleano) + str(flotante) + str(entero) 

#II
investigacion = "Limite de enteros y  los flotantes\n" 
investigacion += "Enteros:\n" 
investigacion += "int\n"
investigacion += "- Memoria requerida 32 bits\n"
investigacion += "-Rango: 0 ~ 4.294.967.295\n"
investigacion += "Flotantes:\n"
investigacion += "float\n" 
investigacion += "Tenemos floats de 64 bits por lo que el numero mas grande seria 1.8 * 10 ^ 308.\n"
investigacion += "Pero tenemos Decimal ('1.8E+308')\n"
investigacion += "-32 bits\n"
investigacion += "-Rango: (-1,79769313486232^308) ~ (-4,94065645841247^-324)"

#III
""""
Formula de la suma de los primeros n numeros pares
n(n+1)
"""
n = int(input("Introduce un numero "))
resSum = n*(n+1)

#IV
print("----Resultados del punto 1----")
print(resultado)
print("----Resultados del punto 2----")
print(investigacion) 
print("----Resultados del punto 3----")
print(resSum)