inventario={"Herramienta manual":{"Productos":[],"Cantidad":{},"Precio":{}},
            "Herramienta electrica":{"Productos":[],"Cantidad":{},"Precio":{}},
            "Pinturas":{"Color":[],"Cantidad":{},"Precio":{}}}
ferreteria=input("Ingrese el nombre de su ferreteria: ")
moneda=input("Ingrese el simbolo de la moneda de su negocio:")
print("¡Bienvenido a ",ferreteria,"!")
while True:
    opcion_menu_principal=int(input("\nPor favor seleccione una de las opciones dadas:\n\n(1) Agregar producto\n(2) Eliminar producto\n(3) Buscar producto\n(4) Actualizar producto\n(5) Mostrar inventario\n(6) Salir\n"))
    #AGREGAR PRODUCTOS
    if opcion_menu_principal==1:
        opcion_1=input("Ingrese una opcion:\n(a) Herramienta manual\n(b) Herramienta electrica\n(c) Pinturas\n").lower()
        if opcion_1=="a":
            producto=input("Añada el producto\n").upper()
            verificar_1=producto in inventario["Herramienta manual"]["Productos"]
            while verificar_1==True:
                producto=input("El producto ya existe por favor ingrese otro\n").upper()
                verificar_1=producto in inventario["Herramienta manual"]["Productos"]
            cantidad=int(input("Ingrese la cantidad del producto añadido: "))
            precio=int(input("Ingrese el precio:\n"))
            inventario["Herramienta manual"]["Productos"].append(producto)
            inventario["Herramienta manual"]["Cantidad"][producto]=cantidad
            inventario["Herramienta manual"]["Precio"][producto]=precio
            
        elif opcion_1=="b":
            producto=input("Añada el producto\n").upper()
            verificar_1=producto in inventario["Herramienta electrica"]["Productos"]
            while verificar_1==True:
                producto=input("El producto ya existe por favor ingrese otro\n").upper()
                verificar_1=producto in inventario["Herramienta electrica"]["Productos"]
            cantidad=int(input("Ingrese la cantidad del producto añadido: "))
            precio=int(input("Ingrese el precio:\n"))
            inventario["Herramienta electrica"]["Productos"].append(producto)
            inventario["Herramienta electrica"]["Cantidad"][producto]=cantidad
            inventario["Herramienta electrica"]["Precio"][producto]=precio
        elif opcion_1=="c":
            producto=input("Indique el color de la pintura\n").upper()
            verificar_1=producto in inventario["Pinturas"]["Color"]
            while verificar_1==True:
                producto=input("El producto ya existe por favor ingrese otro\n").upper()
                verificar_1=producto in inventario["Pinturas"]["Color"]
            cantidad=int(input("Ingrese la cantidad del producto añadido: "))
            precio=int(input("Ingrese el precio:\n"))
            inventario["Pinturas"]["Color"].append(producto)
            inventario["Pinturas"]["Cantidad"][producto]=cantidad
            inventario["Pinturas"]["Precio"][producto]=precio
    #ELIMINAR PRODUCTOS
    elif opcion_menu_principal==2:
        opcion_2=input("Ingrese una opcion:\n(a) Herramienta manual\n(b) Herramienta electrica\n(c) Pinturas\n(d) Eliminar todos los productos existentes en el inventario\n").lower()  
        if opcion_2=="a":
            eliminar=input("Ingrese el producto que desea eliminar del inventario:").upper()
            verificar_2=eliminar in inventario["Herramienta manual"]["Productos"]
            while verificar_2==False:
                eliminar=input("El producto no existe en el inventario, por favor ingrese otro:").upper()
                verificar_2=eliminar in inventario["Herramienta manual"]["Productos"]
            inventario["Herramienta manual"]["Productos"].remove(eliminar)
            inventario["Herramienta manual"]["Cantidad"].pop(eliminar)
            inventario["Herramienta manual"]["Precio"].pop(eliminar)
        elif opcion_2=="b":
            eliminar=input("Ingrese el producto que desea eliminar del inventario:").upper()
            verificar_2=eliminar in inventario["Herramienta electrica"]["Productos"]
            while verificar_2==False:
                eliminar=input("El producto no existe en el inventario, por favor ingrese otro:").upper()
                verificar_2=eliminar in inventario["Herramienta electrica"]["Productos"]
            inventario["Herramienta electrica"]["Productos"].remove(eliminar)
            inventario["Herramienta electrica"]["Cantidad"].pop(eliminar)
            inventario["Herramienta electrica"]["Precio"].pop(eliminar)
            
        elif opcion_2=="c":
            eliminar=input("Ingrese el color de pintura que desea eliminar del inventario:").upper()
            verificar_2=eliminar in inventario["Pinturas"]["Color"]
            while verificar_2==False:
                eliminar=input("El producto no existe en el inventario, por favor ingrese otro:").upper()
                verificar_2=eliminar in inventario["Pinturas"]["Color"]
            inventario["Pinturas"]["Color"].remove(eliminar)
            inventario["Pinturas"]["Cantidad"].pop(eliminar)
            inventario["Pinturas"]["Precio"].pop(eliminar)
            
        elif opcion_2=="d":
            inventario["Herramienta manual"]["Productos"].clear
            inventario["Herramienta manual"]["Cantidad"].clear
            inventario["Herramienta manual"]["Precio"].clear
            inventario["Herramienta electrica"]["Productos"].clear
            inventario["Herramienta electrica"]["Cantidad"].clear
            inventario["Herramienta electrica"]["Precio"].clear

    #BUSCAR PRODUCTOS
    elif opcion_menu_principal==3:
        buscar=input("Ingrese el producto que desea buscar: ").upper()
        verificar_3_manual=buscar in inventario["Herramienta manual"]["Productos"]   
        verificar_3_electrica=buscar in inventario["Herramienta electrica"]["Productos"]
        verificar_3_pintura=buscar in inventario["Pinturas"]["Color"]
        while verificar_3_manual==False and verificar_3_electrica==False and verificar_3_pintura==False:
                buscar=input("El producto no existe, por favor ingrese otro:").upper()
                verificar_3_manual=buscar in inventario["Herramienta manual"]["Productos"]   
                verificar_3_electrica=buscar in inventario["Herramienta electrica"]["Productos"]
                verificar_3_pintura=buscar in inventario["Pinturas"]["Color"]
        if buscar in inventario["Herramienta manual"]["Productos"] or buscar in inventario["Herramienta electrica"]["Productos"] or buscar in inventario["Pinturas"]["Color"]:
            if buscar in inventario["Herramienta manual"]["Productos"]:
                print(buscar,"--->","Precio:",inventario["Herramienta manual"]["Precio"][buscar],moneda, "Unidades disponibles:",inventario["Herramienta manual"]["Cantidad"][buscar])
            elif buscar in inventario["Herramienta electrica"]["Productos"]:
                print(buscar,"Precio:",inventario["Herramienta electrica"]["Precio"][buscar],moneda, "Unidades disponibles:",inventario["Herramienta electrica"]["Cantidad"][buscar])
            elif buscar in inventario["Pinturas"]["Color"]:
                print(buscar,"Precio:",inventario["Pinturas"]["Precio"][buscar],moneda, "Unidades disponibles:",inventario["Pinturas"]["Cantidad"][buscar])
                
    #ACTUALIZAR PRODUCTOS
    elif opcion_menu_principal==4:
        opcion_4=input("Ingrese una opcion:\n(a) Actualizar precio\n(b) Actualizar cantidad\n")
        if opcion_4=="a":
            opcion_4_tipo=input("Ingrese una opcion:\n(a) Herramienta manual\n(b) Herramienta electrica\n(c) Pinturas\n").lower()
            if opcion_4_tipo=="a":
                producto_act=input("Ingrese el producto\n").upper()
                verificar_4=producto_act in inventario["Herramienta manual"]["Productos"]
                while verificar_4==False:
                    producto_act=input("El producto no esta registrado, por favor ingrese otro:").upper()
                    verificar_4=producto_act in inventario["Herramienta manual"]["Productos"]
                precio=int(input("Ingrese el precio\n"))
                inventario["Herramienta manual"]["Precio"][producto_act]=precio
            elif opcion_4_tipo=="b":
                producto_act=input("Ingrese el producto\n").upper()
                verificar_4=producto_act in inventario["Herramienta electrica"]["Productos"]
                while verificar_4==False:
                    producto_act=input("El producto no esta registrado, por favor ingrese otro:").upper()
                    verificar_4=producto_act in inventario["Herramienta electrica"]["Productos"]
                precio=int(input("Ingrese el precio\n"))
                inventario["Herramienta electrica"]["Precio"][producto_act]=precio
                
            elif opcion_4_tipo=="c":
                    producto_act=input("Ingrese el color de la pintura\n").upper()
                    verificar_4=producto_act in inventario["Pinturas"]["Color"]
                    while verificar_4==False:
                        producto_act=input("El producto no esta registrado, por favor ingrese otro:").upper()
                        verificar_4=producto_act in inventario["Pinturas"]["Color"]
                    precio=int(input("Ingrese el precio\n"))
                    inventario["Pinturas"]["Precio"][producto_act]=precio
                
        elif opcion_4=="b":
            opcion_4_tipo=input("Ingrese una opcion:\n(a)Herramienta manual\n(b)Herramienta electrica\n(c)Pintura\n")
            if opcion_4_tipo=="a":
                añadir_retirar=input("Ingrese una opcion:\n(a) Añadir\n (b)Retirar\n")
                if añadir_retirar=="a":
                    producto=input("Ingrese el producto\n").upper()
                    verificar_4=producto in inventario["Herramienta manual"]["Productos"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Herramienta manual"]["Productos"]
                    cantidad=int(input("Ingrese la cantidad que desea añadir: "))
                    suma=inventario["Herramienta manual"]["Cantidad"][producto]+cantidad
                    inventario["Herramienta manual"]["Cantidad"][producto]=suma
                elif añadir_retirar=="b":
                    producto=input("Ingrese el producto\n").upper()
                    verificar_4=producto in inventario["Herramienta manual"]["Productos"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Herramienta manual"]["Productos"]
                    cantidad=int(input("Ingrese la cantidad que desea retirar: "))
                    resta=inventario["Herramienta manual"]["Cantidad"][producto]-cantidad
                    inventario["Herramienta manual"]["Cantidad"][producto]=resta
            elif opcion_4_tipo=="b":
                añadir_retirar=input("Ingrese una opcion:\n(a) Añadir\n (b) Retirar\n")
                if añadir_retirar=="a":
                    producto=input("Ingrese el producto\n").upper()
                    verificar_4=producto in inventario["Herramienta electrica"]["Productos"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Herramienta electrica"]["Productos"]
                    cantidad=int(input("Ingrese la cantidad que desea añadir: "))
                    suma=inventario["Herramienta electrica"]["Cantidad"][producto]+cantidad
                    inventario["Herramienta electrica"]["Cantidad"][producto]=suma
                elif añadir_retirar=="b":
                    producto=input("Ingrese el producto\n").upper()
                    verificar_4=producto in inventario["Herramienta electrica"]["Productos"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Herramienta electrica"]["Productos"]
                    cantidad=int(input("Ingrese la cantidad que desea retirar: "))
                    resta=inventario["Herramienta electrica"]["Cantidad"][producto]-cantidad
                    inventario["Herramienta electrica"]["Cantidad"][producto]=resta
            elif opcion_4_tipo=="c":
                añadir_retirar=input("Ingrese una opcion:\n(a) Añadir\n (b)Retirar\n")
                if añadir_retirar=="a":
                    producto=input("Ingrese el color de pintura\n").upper()
                    verificar_4=producto in inventario["Pinturas"]["Color"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Pinturas"]["Color"]
                    cantidad=int(input("Ingrese la cantidad que desea añadir: "))
                    suma=inventario["Pinturas"]["Cantidad"][producto]+cantidad
                    inventario["Pinturas"]["Cantidad"][producto]=suma
                elif añadir_retirar=="b":
                    producto=input("Ingrese el color de pintura\n").upper()
                    verificar_4=producto in inventario["Pinturas"]["Color"]
                    while verificar_4==False:
                        producto=input("El producto no esta registrado, por favor ingrese otro: ").upper()
                        verificar_4=producto in inventario["Pinturas"]["Color"]
                    cantidad=int(input("Ingrese la cantidad que desea retirar: "))
                    resta=inventario["Pinturas"]["Cantidad"][producto]-cantidad
                    inventario["Pinturas"]["Cantidad"][producto]=resta
                
        #MOSTRAR INVENTARIO
    elif opcion_menu_principal==5:
        print("HERRAMIENTAS MANUALES")
        print("El numero de herramientas de este tipo es:", len(inventario["Herramienta manual"]["Productos"]))
        print("Los precios de los productos existentes son:")
        for key in inventario["Herramienta manual"]["Precio"]:
            print(key,":",inventario["Herramienta manual"]["Precio"][key],moneda)
        print("La cantidad de productos existentes es:")
        for key in inventario["Herramienta manual"]["Cantidad"]:
            print(key,":",inventario["Herramienta manual"]["Cantidad"][key],"unidades")
        print("HERRAMIENTAS ELECTRICAS")
        print("El numero de herramientas de este tipo es:",len(inventario["Herramienta electrica"]["Productos"]))
        print("Los precios de los productos existentes son:")
        for key in inventario["Herramienta electrica"]["Precio"]:
            print(key,":",inventario["Herramienta electrica"]["Precio"][key],moneda)
        print("La cantidad de productos existentes es:")
        for key in inventario["Herramienta electrica"]["Cantidad"]:
            print(key,":",inventario["Herramienta electrica"]["Cantidad"][key],"unidades")
        print("PINTURAS")
        print("El numero de tipos de pintura es:",len(inventario["Pinturas"]["Color"]))
        print("Los precios de los productos existentes son:")
        for key in inventario["Pinturas"]["Precio"]:
            print(key,":",inventario["Pinturas"]["Precio"][key],moneda)
        print("La cantidad de productos existentes es:")
        for key in inventario["Pinturas"]["Cantidad"]:
             print(key,":",inventario["Pinturas"]["Cantidad"][key],"unidades")
    #SALIR
    elif opcion_menu_principal==6:
        break
    
print("¡Gracias por usar nuestro programa!")
    
            


