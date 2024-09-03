#Declara una lista de cadenas
aves=["loro gris","palma de diamante","Coctel"]
print("los valores de la lista antes de insertar:")
#itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave,end=" ")

print("\n")

#Agrega tres valores al final de la lista utilizando el metodo append()
aves.append("Mayna")
aves.append("periquitos")
aves.append("cacatua")
print("los valores de la lista despues de insertar:")
#itera sobre la lista para imprimir los valores
for ave in aves:
    print(ave,end=" ")
    print("\n")