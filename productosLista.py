rta="si"
while rta=="si" or rta=="si" or rta=="SI"
         opcion=input("1.agregar un producto a la lista\ n2.mostrar productos de la lista\n3.Salir")
if opcion=="1":
   productoAgregar=input("ingrese el producto a agregar:")
   prod.append (productoAgregar)
elif opcion=="2":
       for p in prod:
            print ("Los productos en la lista son:",p)
elif opcion=="3":
      rta=input("esta seguro de salir del sistema:(si/no)")
      if rta== "no" or rta=="no" or rta=="No"
         break  
else: 
       print ("opcion invalida")
