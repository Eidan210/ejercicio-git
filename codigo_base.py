tareas = []
while True:
    print ("""
==============================
        BIENVENID@s
Que opcion desea realizar hoy:

1. agregar tarea
2. editar tarea
3. eliminar tarea
4. salir...
==============================""")

    opcion = int(input("que opcion desea elegir. "))
    if opcion <= 0 and opcion >= 5:
        print("opcion no valida, intente denuevo")
        continue
    elif opcion == 1:
        tarea = str(input("Agregue la tarea deseada. ")).capitalize()
        tareas.append(tarea)
        decision = input("¿desea añadir otra tarea? S/N: ").upper()
        if decision == "S":
            continue
        elif decision == "N":
            continue
    elif opcion == 2:
        print("Eligio editar una tarea")
        print(tareas)
        editar_tarea = input("Escriba la tarea que quiere editar: ").capitalize()
        print(tareas.index(editar_tarea))
        tarea_editada = input("ingrese la tarea ya editada: ").capitalize()
        posicion = int(input("ponga el indice de la tarea. "))
        tareas[posicion] = tarea_editada
        if not editar_tarea or not tarea_editada:
            print("no pusiste la tarea que quieres editar o la tarea ya editada,intentalo denuevo")
            continue
        else:
            print("error")
            continue
    elif opcion == 3:
        print("Eligió eliminar una tarea")
        print(f"Lista actual: {tareas}")
        
        eliminar_tarea = input("Escriba la tarea que quiere eliminar: ").capitalize()

        if not eliminar_tarea:
            print("No pusiste la tarea que quieres eliminar, inténtalo de nuevo.")
            continue

        if eliminar_tarea in tareas:
            tareas.remove(eliminar_tarea)
            print(f"Tarea '{eliminar_tarea}' eliminada correctamente.")
        else:
            print("Esa tarea no se encontró en la lista.")

    elif opcion == 4:
        print("saliendo...")
        break
    else:
        print("error")
        continue
                