from io import open
# Retorna una lista de productos,cada uno con nombre, precio, y un atributo s o n
# si el atributo es "s" se le va aplicar un descuento de lo contrario un aumento
def devuelveLista():
    global productos
    productos = []
    nombre = input("ingrese nombre del producto: ")
    
    while(nombre != "ultimo"):
        if(nombre != "" and nombre.isalpha()):
            precio_de_lista = input("1 Precio del producto: ")
            if(precio_de_lista.isdigit()):
                pcuidados = input("\nPertenece a precios cuidados: ")
                if(pcuidados == "s" or pcuidados == "n"):
                    producto = [nombre,precio_de_lista,pcuidados]
                    productos.append(producto)
                    print("\n Ingrese nombre del producto o ultimo para salir ")

                    nombre = input("nombre del producto: ")
                else:
                    print ("\nnombre del producto ingresado: ",nombre)
                    print ("\nOpcion incorrecta,elija(s/n)")
            else:
                print ("no introdujo un precio ")          
        else:   

            print("No es un nombre aceptable")
            nombre=input("ingrese un nombre: ")
    return productos

# retorna la lista de productos con la aplicacion de los descuentos o aumentos
def deveuelvePrecio(lista,valorS,valorN):
    productos = lista
    productosr=[]
    valorS=valorS
    valorN=valorN
    for producto in productos:
        if producto[2] == "s":
            descuento = (int(producto[1])*(100 - valorS)) / 100
            remarcado=[producto[0],descuento,"s"]
            productosr.append(remarcado)
        if producto[2] == "n":
            aumento = (int(producto[1])*(100 + valorN)) / 100
            remarcado=[producto[0],aumento,"n"]
            productosr.append(remarcado)

    return productosr

def menu():
    print ("-----programa supermercado-----")
    print ("opcion 1: carga de productos.")
    print ("opcion 2: lista de precios.")
    print ("opcion n: salir")
    opcion = input("Elija una opcion:")
    while(True):
        if (opcion == "1"):
            lista=devuelveLista()
            listaProductos=open("archivo.txt","a")
            for prod in lista:
                agregar=prod[0]+","+prod[1]+","+prod[2]+"/"
                listaProductos.write(agregar)
            listaProductos.close()
            opcion=input("\nver lista de productos:(2/n) ")
            
        elif opcion == "2":
            listaProductos=open("archivo.txt","r")
            texto=listaProductos.read()
            listaProductos.close()
            lista1=texto.split("/")
            lista=[]
            cont=0
            while cont < len(lista1)-1:
                producto=lista1[cont].split(",")
                lista.append(producto)
                cont+=1
            # se le aplica un 30% de descuento si la opcion es "s" de lo contrario 25% de aumento
            precios=deveuelvePrecio(lista,30,25)
            contador=0
            for precio in precios:
                if precio[2] == "s":
                    print (contador+1,")",precio[0].capitalize()," precio: ",precio[1],"$", "precio cuidado" )
                else:
                    print(contador+1,")",precio[0].capitalize()," precio: ",precio[1],"$")
                contador+=1
                
                if contador == len(precios):
                    opcion = input("\n volver a cargar producto:(1/n)")
                    
        elif opcion == "n":
            print ("\nPrograma terminado.")
            break            
        else:
            print ("opcion incorrecta!!")
            opcion= input("ingrese opcion,(1/2/n)!!")

menu()


