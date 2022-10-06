total=0


print("Bienvenido al banco, elija una opción\n\
1.- Depositar dinero:\n\
2.- Retirar dinero:\n\
3.- Salir:\n")
opcion=int(input())

print("Bienvenido al banco, por favor digite el nombre del user 1")
user1 = str(input())
print("Bienvenido al banco, por favor digite el nombre del user 2")
user2 = str(input())
print("Bienvenido al banco, por favor digite el nombre del user 3")
user3 = str(input())

print("Ingreso exitoso, por favor digita tu nombre")
nombreoperar = str(input())

if opcion==1:

    ingreso=float(input("¿Cuánto dinero vas a depositar?:"))
    montodeposito = ingreso
    
    if nombreoperar == user1
   
    elif opcion==2:
    
        egreso=float(input("¿Cuanto dinero deseas retirar?:"))
    if total-egreso<0:
        print("Error, no tienes ese dinero en el banco tu dinero es:" + str(total))
    else:
        total-=egreso
        print("Tu saldo es de {total:}")

elif opcion==3:
    print("Saliste con éxito este es tu dinero en el banco:" + str(total))
    quit()