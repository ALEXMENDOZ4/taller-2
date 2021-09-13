def punto1 ():
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


            