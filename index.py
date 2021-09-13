"""def punto1 ():
   c = int(input("ingrese cantidad\n "))
   p = int(input("ingrese precio compra\n "))

   costo = c * p
   if(c >= 3 ):
    desc = costo * 0.30
   else:
    desc = costo * 0.10
   total = costo - desc
   print("costo $", costo)
   print("descuento $", desc)
   print("total $", total)    

punto1()   


def punto2():
    c = int(input("digite total de la compra\n"))
    n = int(input("escribe un numero\n"))
    if(n < 74):
     descuento = c * 0.15    
    else:
     descuento = c * 0.20
    total = c - descuento 
    print("el total a pagar con descuento es de: ",total)
    print("el descuento aplicado es de: ", descuento)      

punto2() 

def punto3():
    f = int(input("ingrese el valor de la fianza\n"))
    if(f < 50000):
        desc = f * 0.03
    else:
        desc = f * 0.02
    print("el valor que debe pagar es:", desc)

punto3()

def punto4():
    gananciasd = int(input("cual es el valor de ganancias diarias de su fabrica\n"))
    dia1 = int(input("cuantos puntos emite la fabrica en el dia 1\n"))
    dia2 = int(input("cuantos puntos emite la fabrica en el dia 2\n")) 
    dia3 = int(input("cuantos puntos emite la fabrica en el dia 3\n"))
    dia4 = int(input("cuantos puntos emite la fabrica en el dia 4\n"))
    dia5 = int(input("cuantos puntos emite la fabrica en el dia 5\n"))
    promedio = ((dia1 + dia2 + dia3 + dia4 + dia5) / 5)
    if (promedio > 170):
        print ("Su promedio es mayor a 170, usted debe parar su producción por una semana y tendra una multa del 50% de las ganancias diarias cuando no se detiene la producción, la cual es un total de:" ,gananciasd / 2)
    elif (promedio <= 170):
       print ("Su promedio es menor a 170, usted no tendrá ni sanción ni multa")


punto4()


def punto5():
    p = int(input("ingrese el precio del terreno y automovil\n"))
    a = int(input("ingrese el incremento anual del terreno\n"))
    d = int(input("ingresa la devaluacion anual del automovil\n"))
    incremento = (((p * a) / 100)* 3) / 2
    decremento = ((p * d) / 100) * 3
    print("la mitad del incremento del terreno en 3 años es: ", incremento )
    print("la devaluacion del automovil en 3 años es: ", decremento)

    if(decremento < incremento):
      print("señor usuario le conviene comprar el automovil")
    else:
      print("señor usuario le conviene comprar el terreno")

punto5()            


def punto6():
    print("cada computadora tiene el valor de 11000")
    c = int(input("ingrese el numero de computadoras compradas\n"))
    total = c * 11000
    if(c < 5):
        descuento = total * 0.10
    elif(c < 10):
        descuento = total * 0.20
    elif(c >= 10):
        descuento = total * 0.40

    print(f'el total a pagar por {c} computadoras compradas es: ',total - descuento)
    print("el descuento aplicado es: ",descuento)

punto6()


def punto7():
    p = int(input("ingresa el precio del aparato\n"))
    m = input("ingresa la marca del aparato\n")
    total = p
    iva = int(input("ingresa el porcentaje de iva en aplicar\n"))
    descuento = 0
    if(m == "NOSY" and p >= 2000):
      descuento = p * 0.15
    else:
        if(p >= 2000):
            descuento = p * 0.10
    total = p - descuento
    iva = (total * iva) / 100
    print("el total a pagar es: ",p )
    print("el descuento aplicado es: ",descuento)
    print("el IVA aplicado es: ",iva)
    print("el total a pagar ya con IVA incluido es: ",total + iva)

punto7()


def punto8():
    p = int(input("ingrese numero de piezas\n"))
    c = int(input("ingrese costo por pieza\n"))
    total = p * c
    if(total > 500000):
        invertir = total * 0.55
        prestamo = total * 0.30
        credito =  total * 0.15
    else:
        invertir = total * 0.70
        prestamo = 0
        credito = total * 0.30
    interes = credito * 0.20
    print("cantidad a invertir es de: ",invertir) 
    print("cantidad a prestamo es de: ",prestamo)
    print("cantidad a credito es de: ", credito)
    print("interes es de: ",interes) 

punto8()


def punto9():
    num1 = int(input("ingrese un numero\n"))
    num2 = int(input("ingrese otro numero\n"))
    if(num1 == num2):
        total = num1 * num2
        print("la multiplicacion es de: ",total)
    elif(num1 > num2):
        total = num1 - num2
        print("la resta es de: ",total)
    else:
        total = num1 + num2
        print("la suma es de: ",total)

punto9()
"""

def punto10():
    num1 = int(input("ingrese numero 1\n"))
    num2 = int(input("ingrese numero 2\n"))
    num3 = int(input("ingrese numero 3\n"))
    if(num1 > num2 and num1 > num3):
        print("el numero mayor es numero 1 y su valor es: ",num1)
    elif(num2 > num1 and num2 > num3):    
        print("el numero mayor es numero 2 y su valor es: ",num2)
    elif(num3 > num1 and num3 > num2):    
        print("el numero mayor es numero 3 y su valor es: ",num3)    

punto10()