"""
HACER UNA FUNCION QUE RECIBA UN PARAMETRO NUMERICO. CALCULE EL FACTORIAL Y DEVUELVA EL RESULTADO.

"""

def factorial(numero):
    i=1
    fact=1
    while numero <0:
        print("DEBE DIGITAR UN NUMERO MAYOR A 0")
        numero=int(input("DIGITE UN NUMERO: "))
    while i<=numero:
        fact*=i
        #print(fact)
        i+=1
    return fact

print(factorial(4))

"""
ESCRIBIR UNA FUNCION QUE RECIBA EL NOMBRE E IMPRIMA HOLA NOMBRE
"""

def saludo(name):
    return ("HOLA " + name)
nombre=str(input("INGRESE SU NOMBRE: "))
print(saludo(nombre))

"""
HACER UNA FUNCION QUE RECIBA UN NUMERO Y DEVUELVA EN UNA VARIABLE SI ES NUMERO PRIMO O NO
"""

def esprimo(num):
    if num >1:
      for i in range(2,num):
         if num%i==0:
            return (f"{num} NO ES UN NUMERO PRIMO")
      return (f"{num} ES UN NUMERO PRIMO")
    else:
        return ("DIGITA UN NUMERO MAYOR A 1")
    
print(esprimo(8))

"""
1.Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro 
usando la primera función.

"""
def area(r):
    area=3.14159*(r**2)
    return area

#area(3)

def volumen(r,h):
    volumen=area(r)*h
    return volumen

print(volumen(2,3))

"""
2.Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
def media(lista):
    acum=0
    for i in range(0,len(lista)):
        acum=acum+float(lista[i])
    return acum/len(lista)

lista=[]
while True:
    num=int(input("DIGITE UN NUMERO PARA AGREGAR A LA LISTA: "))
    lista.append(num)
    if str(input("DESEA AGREGAR OTRO NUMERO? ")).upper() == "N":
        break

print(media(lista))

"""
3.Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""
lista=[]
lista2=[]
lista3=[]
def mcd(num1,num2):
    for i in range(1,num1+1):
        if num1%i==0:
            lista.append(i)    
    for i in range(1,num2+1):
        if num2%i==0:
            lista2.append(i)
    if len(lista)>=len(lista2):
        for j in lista2:
            for i in range(1,len(lista2)):
                if lista[i]==j:
                    lista3.append(j)
    else:
        for j in lista:
            for i in range(1,len(lista)):
                if lista2[i]==j:
                    lista3.append(j)

    return (f"EL MAXIMO COMUN DIVISOR ENTRE {num1} Y {num2} ES {max(lista3)}")
print(mcd(63,49))
print(mcd(77,105))
#print(max(lista3))

#mcm
lista=[]
lista2=[]
lista3=[]

def mcm(num1,num2):
    for i in range(1,100):
        lista.append(num1*i)
        lista2.append(num2*i)
    for j in lista:
        for i in range(1,len(lista)):
            if lista2[i]==j:
                lista3.append(j)
    return (f"EL MINIMO COMUN MULTIPLO ENTRE {num1} Y {num2} ES {min(lista3)}")
print(mcm(12,8))
"""
4.Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def iva(valor,iva=0.21):
    valor_iva=int(valor*iva)
    total_fact=int(valor+valor_iva)
    return total_fact,valor_iva

total_fact,valor_iva=iva(10000)

print(f"EL VALOR TOTAL DEL IVA ES: {valor_iva}; TOTAL DE LA FACTURA: {total_fact}")

"""
5.Hacer dos funciones que se complementen entre las sí para hacer una tarea específica.
"""