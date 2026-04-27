#for i in range(0,5,1): #(inicia la vx control, hasta donde llega, incremento)
#    print(i)
    
  #4.  #ingrese un numero y mostrar la tabla de multiplicar de ese numero. Por jemplo, si se ingresa el numero 5:
    #5 x 0 = 0
    #5 x 1 = 5
    #5 x 2 = 10
    #5 x 3 = 15

#tabla = int(input("ingrese que tabla: "))
#for i in range(0,11,1): 
#    resultado = que_tabla * i
#    print(f"{que_tabla} x {i} = {resultado}")

#5. Imprimir los numeros multiplos de 3 entre el 1 y el 10.

#for i in range(3,10,3):
#    print(i)

#for i in range(1,11,1):
#    if i % 3 == 0:
#        print(i)

#for i in range(1, 11, 1):
#    if (i % 3 != 0):
#        continue
#    print(i)

# se ingresa un maximo de 10 numeros o hasta que el usuario ingrese el numero 0.
# mostrar la suma y el promedio a todos los numeros.

#suma = 0
#contador = 0
#for i in range(10):
#    numero = int(input("ingrese un numero: "))
    
#    if numero == 0:
#        break

#    suma += numero
#contador += 1
#    # suma = suma + numero
#promedio = suma / contador
#print (promedio)  


# ingresar 10 numeros, solo sumar los que esten fuera del rango 50-100. 

#suma = 0
#for i in range(10):
#    numero = int(input("ingrese un numero: "))
#    if numero < 50 or numero > 100:
#        suma += numero

#print(suma) 

#11. ingresar un numero. Mostrar todos los divisores que hay desde el 1 hasta el numero ingresado.
# Mostrar la cantidad de divisores encontrados.

#numero = int(input("ingrese un numero: "))
#contador_divisores = 0
#for i in range(1, numero + 1, 1):
#    if numero % i == 0:
#       contador_divisores += 1
#       print(i)

#print(f"cantidad de divisores: {contador_divisores}")

#12. Ingresar un numero. Determinar si el numero es primo o no.

#numero = int(input("Ingrese un numero: "))
#contador_divisores = 0
#for i in range(1, numero +1, 1):
#    if numero % i == 0:
#       contador_divisores += 1 

#if contador_divisores == 2:
#    print("es primo")
#else:
#    print("no es primo")
# 
# FOR ANIDADO (EJEMPLO RELOJ)
#for i in range(13):
#    print(f"{i}: ")
#    for j in range(13):
#        print(f"\t{j}")

# INGRESAR UN NUMERO. MOSTRAR CADA NUMERO PRIMO QUE HAY ENTRE EL 1 Y EL NUMERO INGRESADO.
# INFORMAS CUANTOS NUMEROS PRIMOS SE ENCONTRARON.

numero = int(input("Ingrese un numero: "))
for i in range(1, numero + 1, 1):

    for i in range(1, i, 1):
        if i % j == 0:
            es_primo = False
            break