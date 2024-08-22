productos=["jugo de uva"]
print("lista inicial",productos)
productos.append ("papel higientico")
productos.append ("yogurt pera")
print("lista completa despues de usar append",productos)
productos.insert(0,"jabon en polvo")

print("despues de usar insert: ",productos)
productos[1]="rollo de cocina" #reemplazamos valor del elemento en la posicion 1 conejo por liebre
print("lista animales despues de reemplazar conejo por liebre:",productos)