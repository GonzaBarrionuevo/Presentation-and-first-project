
##Técnicas de Programación

##Gonzalo Barrionuevo


##1. Un proveedor de estéreos ofrece un descuento del 10% sobre el precio sin IVA, de algún aparato si esta cuesta
##$2000 o más. Además, independientemente de esto, ofrece un 5% de descuento adicional sobre el precio si la marca
##es “NOSY”.
##Determinar cuánto pagará, con IVA incluido, un cliente cualquiera por la compra de su aparato. IVA = 20%.


##precio = int(input("Ingrese el precio del producto: "))
##marca = input("Ingrese la marca del producto: ")
##iva = 0.2
##if precio>=2000 and marca=="NOSY":
##    cuenta = precio*0.1
##    cuenta2 = cuenta*0.05
##    print("Debera pagar: ", cuenta2*iva)
##elif precio>=2000 and marca!="NOSY":
##    print("Debera pagar: ", (precio*0.1)*iva )
##elif precio<2000 and marca=="NOSY":
##    cuenta3 = precio*0.05
##    print("Debera pagar: ", cuenta3*iva)
##else:
##    print("Debera pagar: ", precio*iva)






##2.. Ingresar por teclado 15 números enteros y calcular cuántos de ellos son pares y cuantos de ellos son impares. Se
##emprime el resultado la suma, cantidad y promedio en cada caso. Sin utilizar Lista.




##numpar=0
##numimp=0
##cantpar=0
##cantimp=0
##for n in range(15):
##    n = int(input("Ingrese un numero: "))
##    if n%2==0:
##        numpar = numpar + n
##        cantpar = cantpar + 1
##    else:
##        numimp = numimp + n
##        cantimp = cantimp + 1
##print(f"La cantidad de los par: {cantpar}, la suma de los pares es: {numpar}, Y el promedio es: {numpar/cantpar}")
##print(f"La cantida de los impar: {cantimp} , la suma de los impares da: {numimp}, y el promedio es: {numimp/cantimp}")

   


##2.. Bis) resolver el ejercicio anterior con lista.



##listapar = []
##listaimpar = []
##for n in range(15):
##    n = int(input("Ingrese un numero: "))
##    if n%2==0:
##        listapar.append(n)
##    else:
##        listaimpar.append(n)
##sumapar=sum(listapar)
##sumaimp=sum(listaimpar)
##print(f"La cantidad de los par: {len(listapar)}, la suma de los pares es: {sumapar}, Y el promedio es: {sumapar/len(listapar)}")
##print(f"La cantida de los impar: {len(listaimpar)} , la suma de los impares da: {sumaimp}, y el promedio es: {sumaimp/len(listaimpar)}")    


        





##3.. Función, Pide números y mételos en 2 listas (por separado positivos y negativos), cuando el usuario meta un 0 ya
##dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor y también la cantidad.


##def num_lista():
##    numpositivos=[]
##    numnegativos=[]
##    numero = int(input("Ingrese un numero: "))
##    while numero!=0:
##        numero = int(input("Ingrese otro numero: "))
##        if numero > 0:
##            numpositivos.append(numero)
##            numpositivos.sort()
##        else:
##            numnegativos.append(numero)
##            numnegativos.sort()             
##    print("Los numeros postivos son: ", numpositivos,",y la cantidad de los postivos es: ", len(numpositivos))
##    print("Los numeros negativos son: ", numnegativos,",y la cantidad de los negativos es: ", len(numnegativos))
##                  
##num_lista()
            


    


##4.. Tenemos 2 artículos con 4 precios diferente. Necesitamos saber el precio medio de cada artículo luego su
##promedio total. Utilizar for para resolver.

##articulos = []
##precios = []
##articulo1 = 0
##articulo2 = 0
##promedio = 0
##for a in range(2):
##    articulo = str(input("Ingrese el nombre del articulo: "))
##    articulos.append(articulo)
##    for p in range(4):
##        precio = int(input("Ingrese el precio de los precios: "))
##        precios.append(precio)
##articulo1 = sum(precios[0:4])/4
##articulo2 = sum(precios[4:8])/4
##promedio = sum(precios)/len(precios)
##print(f"El promedio de {articulos[0]} es: {articulo1}")
##print(f"El promedio de {articulos[1]} es: {articulo2}")
##print(f"El promedio general es: {promedio}")
        


##5.. Escribir un algoritmo que invierta los dígitos de un número positivo entero. Usar operadores módulo y división
##para ir obteniendo los dígitos uno a uno. Por ejemplo, si se ingresa 37368 debe retornar el numero 86373


##n = int(input("Ingrese un numero: "))
##numero = 0
##while n != 0:
##    numero = 10*numero+n % 10
##    n //= 10   
##print("El numero que ingreso invertido es:", numero)



#otra forma que encontre:


##numero = input("Ingrese un numero entero: ")
##cuenta = numero[::-1]
##print("El numero que ingreso invertido es: ", cuenta)





