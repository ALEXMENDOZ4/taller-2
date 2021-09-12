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