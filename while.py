while true: #condicion a evaluar 
    opcion=input("menu de elementos n1\agregar producto n2\eliminar producto n3\modificar producto n4\mostrar producto")
    if opcion=="1":
       elementoAgregar=input("ingrese el elemento a agregar:") # entra el elemento a agregar 
       l.append(elementoAgregar) # agrega 1 elemento 
    elif opcion=="2": #evalua condiciones guardadas en 2
       elementoAeliminar=input("ingrese el nombre del elemento a eliminar:")# entra el elemento a eliminar
       if elementoAeliminar in l: # si el elemento esta en la lista
          l.remove(elementoAeliminar) # remueve el elemento
           print("elemento eliminado exitosamente") # muestra 
        else: # si no
             print("el elemento que desea eliminar no se encuentra en la lista") # muestra
    elif opcion=="3": # evalua condiciones guardadas en 3
     elementoAmodificar=input("ingrese el nombre del elemento a modificar:") # entra el elemento a modificar
     if elementoAmodificar in l: # si el elemento esta en la lista
       elementoAmodificar=input("ingrese el nombre por el que quiere modificar") # entra elemento a modificar
       # Find the index of the element modify
       index = l.index(elementoAmodificar) # indice
       l[index] = elementoModificacion # use the index to modify the element
     else: # si no
         print("el elemento que desea modificar no se encuentra en la lista") # muestra 
       
    elif opcion=="4": # evalua condiciones guardadas en 4 
       print("elementos en la lista: \n",l) # muestra elemento en la lista
    elif opcion==5 # evalua condiciones guardadas en 5 
       print("saliendo del sistema") # muestra 
     break # cambio de linea
    else : # evalua multiples condiciones
      print ("la opcion ingresada es invalida") # muestra 