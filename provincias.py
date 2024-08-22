Provincias={"Buenos Aires":"la plata","misiones":"posadas","rio negro":"Viedma","corrientes":"corrientes","parana":"entre rios","tierra del fuego":"ushuaia","chubut":"rawson","provincia del chaco":"resistencia","la pampa":"ciudad de santa rosa","formosa":"formosa","santa cruz":"rio gallegos","santa fe":"provincia de santa fe","salta":"salta","cordoba":"cordoba","jujuy":"san salvador de jujuy","santiago del Estero":"ciudad de santiago del estero","neuquen":"neuquen","san luis":"ciudad de san luis","la rioja":"la rioja","catamarca","san fernando valle catamarca"}

print (provincias)

for t, v in provincias.items():

    print (t,",",v)

    print (f"(c):(V)")

    if "mendoza" in v:

        print ("la provincia mendoza existe y tiene clave:",t)