#Generar una agenda de contactos. 
#Se debe utilizar funciones, listas y diccionarios
#Se debe tener en cuenta los controles necesario ante errores del usuario o código
#Se asignará un área funcional a cada alumno
#La integración del código estará a cargo del grupo que quede conformado
#Se otorgará una nota grupal y una individual
#La nota final del parcial va a estar conformada por la relación de ambas notas


#-------------01- FUNCION  PARA AGREGAR CONTACTOS------------------------

def agregar_contacto(lista_contactos):
        dic_contacto = {}  
        dic_contacto["código"] = len(lista_contactos) + 1                          
        dic_contacto["Celular"] = input("Ingrese el número de celular: ").strip()
        dic_contacto["Nombre"] = input("Ingrese el nombre del contacto: ").strip()
        favorito = input("¿Favorito? (si/no): ").strip()
        dic_contacto["Favorito"] = favorito in ["SI", "Si", "si", "TRUE", "True", "true"]
        
        lista_contactos.append(dic_contacto)
        print("Contacto agregado correctamente.")
        print((dic_contacto))

#--------------02- FUNCION PARA MOSTRAR CONTACTOS--------------------------

def mostrar_contactos(lista_contactos):
        if len(lista_contactos) == 0: 
            print("La agenda está vacía.")
        else:
            print("\nListado de contactos:")
        
        for contacto in lista_contactos:
            print("-" * 30)
            print(f"Código: {contacto['código']}")
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Celular: {contacto['Celular']}")
            print(f"Favorito: {'Sí' if contacto['Favorito'] else 'No'}")
        print("-" * 30)


#--------------03- FUNCION PARA FILTRAR CONTACTO POR NOMBRE-----------------

def filtrar_contacto(lista_contactos):   
        nombre_busqueda = input("Ingrese el nombre del contacto a buscar: ").strip()
        encontrados = []
        for contacto in lista_contactos:
            if contacto["Nombre"] == nombre_busqueda:  
                encontrados.append(contacto)
                if len(encontrados) > 0:
                    print("\nContactos encontrados:")
                    for contacto in encontrados:
                        print("-" * 30)
                        print(f"Código: {contacto['código']}")
                        print(f"Nombre: {contacto['Nombre']}")
                        print(f"Celular: {contacto['Celular']}")
                        print(f"Favorito: {'Sí' if contacto['Favorito'] else 'No'}")
                        print("-" * 30)
                else:
                    print("No se encontró ningún contacto con ese nombre.")

#---------------04- FUNCION FILTRAR FAVORITO--------------------------------

def filtrar_favo(lista_contactos):
        print(" Contactos Favoritos:")
        favoritos = [c for c in lista_contactos if c.get("Favorito")]
        if not favoritos:
            print("No hay contactos favoritos.")
        else:
            for contacto in favoritos:
                print(f"Código: {contacto['código']}")
                print(f"Nombre: {contacto['Nombre']}")
                print(f"Celular: {contacto['Celular']}")
                print(f"Favorito: {'Sí' if contacto["Favorito"] else 'No'}")
                print("-" * 20)




#------------- 05- FUNCION PARA MOSTRAR CONTACTOS EVENTUALES -------------------

def mostrar_eventuales(lista_contactos):
    hay_eventuales = False

    for contacto in lista_contactos:
         if contacto["Favorito"] == False:
            print("Contactos eventuales: ")
            print(f"\nCódigo: {contacto['código']}")
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Celular: {contacto['Celular']}")
            print("Favorito: No")
            hay_eventuales = True

         else: 
            hay_eventuales
            print("No hay contactos eventuales.")

#-----------------06- FUNCION PARA AGREGAR FAVORITO ----------------------------

def agregar_favorito(lista_contactos):   
        codigo_favorito = int(input("Ingrese el código del contacto que quiera marcar como favorito: "))
        for contacto in lista_contactos:
            if contacto["código"] == codigo_favorito:
                contacto["Favorito"] = True
                print(f"Contacto {contacto['Nombre']} ahora es favorito.")
                break
        else:
                print("No se encontró un contacto con ese código.")


#--------------------07- MODIFICAR CONTACTO--------------------


def modificar_contacto(lista_contactos):
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        encontrado = False
        for contacto in lista_contactos:
            if contacto["Nombre"].lower() == nombre.lower():
                nuevo_cel = input("Ingrese el nuevo número de celular: ")
                contacto["Celular"] = nuevo_cel
                print(" Número de celular actualizado.")
                encontrado = True
                break
            if not encontrado:
                print("Contacto no encontrado.")


#-------------------08- FUNCION ELIMINAR CONTACTO------------------
def eliminar_contacto(lista_contactos):
    nombre_busqueda = input("Ingrese el nombre del contacto a buscar para eliminar: ").strip()
    encontrados = []

    for contacto in lista_contactos:
        if contacto["Nombre"].lower() == nombre_busqueda.lower():
            encontrados.append(contacto)

    if len(encontrados) > 0:
        print("\nContactos encontrados:")
        for contacto in encontrados:
            print("-" * 30)
            print(f"Código  : {contacto['código']}")
            print(f"Nombre  : {contacto['Nombre']}")
            print(f"Celular : {contacto['Celular']}")
            print(f"Favorito: {'Sí' if contacto['Favorito'] else 'No'}")
        print("-" * 30)

        try:
            codigo_a_eliminar = int(input("Ingrese el código del contacto que desea eliminar: "))
        except ValueError:
            print("Código inválido.")
            return

        for contacto in lista_contactos:
            if contacto["código"] == codigo_a_eliminar:
                confirmacion = input("¿Estás seguro que deseas eliminar este contacto? (s/n): ").strip().lower()
                if confirmacion == "s":
                    lista_contactos.remove(contacto)
                    print("Contacto eliminado correctamente.")
                else:
                    print("Eliminación cancelada.")
                return

        print("No se encontró ningún contacto con ese código.")
    else:
        print("No se encontró ningún contacto con ese nombre.")




# 
#           


lista_contactos=[  {"código": 1, "Nombre": "Juan Perez", "Celular": "123456789", "Favorito": True},
    {"código": 2, "Nombre": "Lucia Gomez", "Celular": "987654321", "Favorito": False}]



while True:
    print("""-----MENU------
    1- Agregar Contacto
    2- Mostrar Contactos
    3- Filtrar Contacto por nombre
    4- Filtrar Favoritos
    5- Filtrar eventuales
    6- Agregar a favoritos
    7- Modificar Contacto 
    8- Eliminar Contacto
    9- Salir""")
    opcion=int(input("Ingrese la opción deseada: "))
    if opcion==1:
        agregar_contacto(lista_contactos)
        #Alumno 1
        #Se debe permitir el ingreso de un contacto a través del diccionario a la lista señalada
   
    elif opcion==2:
        mostrar_contactos(lista_contactos)
        #Alumno 1
        #Se debe mostrar la lista completa de contactos. Se tendrá en cuenta la forma de mostrar
        #Se sugiere investigar alguna forma atractiva de mostrar los datos

    elif opcion==3:
        filtrar_contacto(lista_contactos)
    #TODOS 
           
    elif opcion==4:
         filtrar_favo(lista_contactos)
       




        #Alumno 2
        #Se debe mostrar sólo los contactos favoritos
        #Se sugiere investigar alguna forma atractiva de mostrar los datos


    elif opcion == 5:
        mostrar_eventuales(lista_contactos)

    elif opcion==6:
         agregar_favorito(lista_contactos)
    


    elif opcion==7:
        modificar_contacto(lista_contactos)


        
    elif opcion==8:
        eliminar_contacto(lista_contactos) 
        #Alumno 3
        #Se debe filtrar un contacto y luego permitir eliminarlo
        pass
    elif opcion==9:
        break
    else:
        print("Elija una opción correcta")


