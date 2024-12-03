import getpass

# Diccionarios para almacenar datos
citas = {
    "123456789": {
        "día": "01/12/2024",
        "hora": "10:30",
        "tipo": "General",
        "médico": "Dr. Pérez",
        "estado": "Pendiente"
    },
    "987654321": {
        "día": "02/12/2024",
        "hora": "14:00",
        "tipo": "Especialista",
        "médico": "Dra. Ramírez",
        "estado": "Confirmada"
    }
}

atenciones = [
    "Cita agregada para cédula 123456789.",
    "Cita confirmada para cédula 987654321."
]

# Contraseña del administrador
ADMIN_PASS = "rana123"

# Dibujos de ranas en ASCII
RANA_BIENVENIDA = r"""
        @..@
       (----)
      ( >__< )
      ^^ ~~ ^^
  Sana, sana, colita de rana
"""

RANA_DESPEDIDA = r"""
        @..@
       (----)
      ( >__< )
      ^^ ~~ ^^
 ¡Que tengas un día saltarín y feliz!
"""

RANA_MENU = r"""
        @..@
       (----)
      ( >__< )
      ^^ ~~ ^^
"""

# Funciones auxiliares para diseño
def imprimir_encabezado(titulo):
    #Imprime un encabezado con estilo y temática de ranas.
    print("\n" + "=" * 50)
    print(f"🐸 {titulo.center(46)} 🐸")
    print("=" * 50)

def imprimir_opciones(opciones):
    #Imprime un menú de opciones con estilo.
    for num, opcion in enumerate(opciones, 1):
        print(f"  {num}. {opcion}")

def imprimir_separador():
    #Imprime un separador visual.
    print("-" * 50)

def imprimir_rana_menu():
    #rana en ASCII para embellecer los menús.
    print(RANA_MENU)

######################################################################################################

#Funciones del programa

######################################################################################################
def agregar_cita():
    imprimir_encabezado("Agregar Cita 🐸")
    imprimir_rana_menu()
    cedula = input("Ingrese la cédula del paciente: ")
    if cedula in citas:
        print("⚠️ Ya existe una cita para esta cédula.")
        return

    # Recolectar datos de la cita
    dia = input("Ingrese el día de la cita (dd/mm/aaaa): ")
    hora = input("Ingrese la hora de la cita (hh:mm): ")
    tipo = input("Ingrese el tipo de cita (General/Especialista): ")
    medico = input("Ingrese el nombre del médico: ")

    # Registrar cita
    citas[cedula] = {
        "día": dia,
        "hora": hora,
        "tipo": tipo,
        "médico": medico,
        "estado": "Pendiente"
    }
    atenciones.append(f"Cita agregada para cédula {cedula}.")
    print("✅ Cita registrada exitosamente. ¡La rana está feliz!")

def consultar_cita():
    imprimir_encabezado("Consultar Cita 🐸")
    imprimir_rana_menu()
    cedula = input("Ingrese su cédula: ")
    if cedula in citas:
        print("\nDatos de su cita:")
        imprimir_separador()
        for clave, valor in citas[cedula].items():
            print(f"  {clave.capitalize()}: {valor}")
        imprimir_separador()
        print("🐸 ¡Que tengas un día feliz como una rana!")
    else:
        print("⚠️ No se encontró ninguna cita asociada a esta cédula.")

def confirmar_cancelar_cita():
    imprimir_encabezado("Confirmar/Cancelar Cita 🐸")
    imprimir_rana_menu()
    cedula = input("Ingrese la cédula del paciente: ")
    if cedula not in citas:
        print("⚠️ No se encontró ninguna cita asociada a esta cédula.")
        return

    imprimir_opciones(["Confirmar cita", "Cancelar cita"])
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        citas[cedula]["estado"] = "Confirmada"
        atenciones.append(f"Cita confirmada para cédula {cedula}.")
        print("✅ La cita ha sido confirmada. ¡La rana dice croac de felicidad!")
    elif opcion == "2":
        citas[cedula]["estado"] = "Cancelada"
        atenciones.append(f"Cita cancelada para cédula {cedula}.")
        print("✅ La cita ha sido cancelada. ¡La rana espera verte pronto!")
    else:
        print("⚠️ Opción inválida.")

def imprimir_reporte():
    imprimir_encabezado("Reporte de Citas 🐸")
    imprimir_rana_menu()
    if not citas:
        print("⚠️ No hay citas registradas.")
        return
    for cedula, datos in citas.items():
        print(f"\n📄 Cédula: {cedula}")
        imprimir_separador()
        for clave, valor in datos.items():
            print(f"  {clave.capitalize()}: {valor}")
        imprimir_separador()

    print("\n--- Historial de Atenciones ---")
    imprimir_separador()
    for registro in atenciones:
        print(f"  {registro}")
    print("🐸 ¡Croac! Reporte finalizado.")

def menu_administrador():
    imprimir_encabezado("Menú Administrador 🐸")
    password = getpass.getpass("Ingrese la contraseña del administrador: ")
    if password != ADMIN_PASS:
        print("❌ Contraseña incorrecta. 🐸")
        return

    while True:
        imprimir_encabezado("Opciones de Administrador 🐸")
        imprimir_opciones(["Agregar cita", "Confirmar/Cancelar cita", "Imprimir reporte", "Salir al menú principal"])
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cita()
        elif opcion == "2":
            confirmar_cancelar_cita()
        elif opcion == "3":
            imprimir_reporte()
        elif opcion == "4":
            print("🐸 Saliendo al menú principal... ¡Hasta luego, administrador rana!")
            break
        else:
            print("⚠️ Opción inválida.")

def menu_principal():
    while True:
        imprimir_encabezado("Menú Principal 🐸")
        imprimir_rana_menu()
        imprimir_opciones(["Consultar cita", "Menú administrador", "Salir"])
        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            consultar_cita()
        elif opcion == "2":
            menu_administrador()
        elif opcion == "3":
            print(RANA_DESPEDIDA)
            break
        else:
            print("⚠️ Opción inválida.")

# Ejecución del programa
if __name__ == "__main__":
    print(RANA_BIENVENIDA)
    print("¡Bienvenido a Sana, sana, colita de rana!")
    menu_principal()
