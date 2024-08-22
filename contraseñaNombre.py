usuario = ""
contraseña = ""
u=input("ingrese su nombre de usuario:")
c=input("ingrese su contraseña:")
contador +1
while u!=usuario and c!=contraseña and contador<4:

       u=input("ingrese su nombre de usuario:")
       c=input("ingrese su contraseña:")
       print("vuelta numero",contador)
       contador=contador+1

       if u=usuario and c=contraseña:
          print("elemento al sistema")
       else 
          print("usted no puede ingresar al sistema")