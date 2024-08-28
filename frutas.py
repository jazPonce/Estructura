frutas = {"cereza": ("precio":1000), "kiwi": ("precio":2000)}

#inicializar  el total 
total = 0

#solicitar al usuario que ingrese la fruta y la cantidad 
fruta = input ("ingrese la fruta que desea vender: ")
cant = float(input("ingrese la cantidad a vender: "))

#verificar que la fruta este en el diccionario 
if fruta in frutas:
    #calcular el total
    total = frutas[fruta]["precio"] * cant 
    print (f"el total a pagar por {cant} kilos de {fruta} es: {total})
    print ("el precio de",cant,"kg", "de ",fruta," es de:",total)

else :
    print ("la fruta ingresada no existe en el diccionario")