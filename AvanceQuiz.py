from datetime import datetime

# Definición de las clases de implantes médicos
class ImplanteMedico:
    def __init__(self, material, tipo_fijacion, tamaño):
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño
    
    def obtener_material(self):
        return self.__material
    
    def obtener_tipo_fijacion(self):
        return self.__tipo_fijacion
    
    def obtener_tamaño(self):
        return self.__tamaño

    def modificar_material(self, nuevo_material):
        self.__material = nuevo_material
    
    def modificar_tipo_fijacion(self, nuevo_tipo_fijacion):
        self.__tipo_fijacion = nuevo_tipo_fijacion
    
    def modificar_tamaño(self, nuevo_tamaño):
        self.__tamaño = nuevo_tamaño

class Marcapasos(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño, num_electrodos, alambrico, frec_estimulacion):
        super().__init__(material, tipo_fijacion, tamaño)
        self.__num_electrodos = num_electrodos
        self.__alambrico = alambrico
        self.__frec_estimulacion = frec_estimulacion
    
    def obtener_num_electrodos(self):
        return self.__num_electrodos
    
    def es_alambrico(self):
        return self.__alambrico
    
    def obtener_frec_estimulacion(self):
        return self.__frec_estimulacion 
class StentCoronario(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño, longitud, diametro):
        super().__init__(material, tipo_fijacion, tamaño)
        self.__longitud = longitud
        self.__diametro = diametro

    def obtener_longitud(self):
        return self.__longitud

    def obtener_diametro(self):
        return self.__diametro

class ImplanteDental(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño, forma, sistema_fijacion):
        super().__init__(material, tipo_fijacion, tamaño)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion

    def obtener_forma(self):
        return self.__forma

    def obtener_sistema_fijacion(self):
        return self.__sistema_fijacion      
class ProtesisCadera(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño):
        super().__init__(material, tipo_fijacion, tamaño)

class ProtesisRodilla(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamaño):
        super().__init__(material, tipo_fijacion, tamaño)

# Definición de la clase Paciente
class Paciente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.implantes_asociados = []

    def asignar_implante(self, implante, fecha_implantacion, medico_responsable, estado):
        info_implante = {
            'implante': implante,
            'fecha_implantacion': fecha_implantacion,
            'medico_responsable': medico_responsable,
            'estado': estado
        }
        self.implantes_asociados.append(info_implante)

# Lista para almacenar pacientes
lista_pacientes = []
# lista para implantes
lista_implantes = [Marcapasos, StentCoronario, ImplanteDental, ProtesisCadera, ProtesisRodilla]

# Funciones auxiliares
def crear_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cedula = input("Ingrese la cédula del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    paciente = Paciente(nombre, cedula, edad)
    lista_pacientes.append(paciente)
    print("Paciente creado con éxito.")

def asignar_implante():
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return

    # Mostrar lista de pacientes
    print("Lista de pacientes:")
    for i, paciente in enumerate(lista_pacientes):
        print(f"{i + 1}. {paciente.nombre}")

    # Seleccionar paciente
    num_paciente = int(input("Seleccione el número de paciente al que desea asignar un implante: "))
    paciente_seleccionado = lista_pacientes[num_paciente - 1]
    # Mostrar tipos de implantes disponibles
    print("\nTipos de implantes disponibles: \n1. Marcapasos\n2. Stent Coronario\n3. Implante Dental\n4. Prótesis de Cadera\n5. Prótesis de Rodilla\n")
    
    opcion_implante = input("Seleccione el tipo de implante que desea asignar al paciente: ")

    # Crear implante según la opción seleccionada
    if opcion_implante == "1":
        implante = Marcapasos(material="Titanio", tipo_fijacion="Inalambrico", tamaño="Pequeño",
                            num_electrodos=2, alambrico=False, frec_estimulacion=60)
    elif opcion_implante == "2":
        implante = StentCoronario(material="Acero inoxidable", tipo_fijacion="Expandible", tamaño="Mediano",
                                longitud=30, diametro=3)
    elif opcion_implante == "3":
        implante = ImplanteDental(material="Porcelana", tipo_fijacion="Tornillo", tamaño="Pequeño",
                                forma="Molar", sistema_fijacion="Implante de hueso")
    elif opcion_implante == "4":
        implante = ProtesisCadera(material="Titanio", tipo_fijacion="Cementada", tamaño="Grande")
    elif opcion_implante == "5":
        implante = ProtesisRodilla(material="Polietileno", tipo_fijacion="No cementada", tamaño="Mediano")
    else:
        print("Opción no válida.")
        return
    
    # Registrar información del implante
    fecha_implantacion = input("Ingrese la fecha de implantación (YYYY-MM-DD): ")
    medico_responsable = input("Ingrese el nombre del médico responsable: ")
    estado = input("Ingrese el estado del implante: ")

    # Asignar implante al paciente
    paciente_seleccionado.asignar_implante(implante, fecha_implantacion, medico_responsable, estado)
    print("Implante asignado con éxito.")
def mostrar_inventario():
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return

    print("Inventario de pacientes y sus implantes:")
    for i, paciente in enumerate(lista_pacientes):
        print(f"{i + 1}. Nombre: {paciente.nombre}, Cédula: {paciente.cedula}, Edad: {paciente.edad}")
        if paciente.implantes_asociados:
            print("   Implantes:")
            for implante_info in paciente.implantes_asociados:
                print(f"   - Tipo: {type(implante_info['implante']).__name__}")
                print(f"     Material: {implante_info['implante'].obtener_material()}")
                print(f"     Tipo de Fijación: {implante_info['implante'].obtener_tipo_fijacion()}")
                print(f"     Tamaño: {implante_info['implante'].obtener_tamaño()}")
                print(f"     Fecha de implantación: {implante_info['fecha_implantacion']}")
                print(f"     Médico responsable: {implante_info['medico_responsable']}")
                print(f"     Estado: {implante_info['estado']}")
        else:
            print("   No hay implantes asociados.")
def editar_implantes():
    while True:
        print("\n--- Edición de Implantes: \n1. Agregar nuevo tipo de implante\n2. Eliminar tipo de implante\n3. Editar información de tipo de implante\n4. Visualizar inventario de tipos de implantes\n5. Regresar al menú principal\n---")
        
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            agregar_nuevo_implante()
        elif opcion == "2":
            eliminar_implante()
        elif opcion == "3":
            editar_info_implante()
        elif opcion == "4":
            visualizar_inventario_implantes()
        elif opcion == "5":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

def agregar_nuevo_implante():
    nombre_clase = input("Ingrese el nombre de la nueva clase de implante: ")
    nueva_clase = type(nombre_clase, (ImplanteMedico,), {})
    lista_implantes.append(nueva_clase)
    print(f"Clase de implante '{nombre_clase}' agregada con éxito.")

def eliminar_implante():
    if not lista_implantes:
        print("No hay tipos de implantes registrados.")
        return

    print("Tipos de implantes registrados:")
    for i, implante in enumerate(lista_implantes):
        print(f"{i + 1}. {implante.__name__}")

    num_implante = int(input("Seleccione el número del tipo de implante que desea eliminar: "))
    if num_implante <= len(lista_implantes):
        del lista_implantes[num_implante - 1]
        print("Tipo de implante eliminado correctamente.")
    else:
        print("Número de tipo de implante no válido.")
def editar_info_implante():
    if not lista_implantes:
        print("No hay tipos de implantes registrados.")
        return

    print("Tipos de implantes registrados:")
    for i, implante in enumerate(lista_implantes):
        print(f"{i + 1}. {implante.__name__}")

    num_implante = int(input("Seleccione el número del tipo de implante cuya información desea editar: "))
    if num_implante <= len(lista_implantes):
        nombre_clase = lista_implantes[num_implante - 1].__name__
        print(f"Editando información del tipo de implante '{nombre_clase}':")
        nueva_info_material = input("Ingrese el nuevo material: ")
        nueva_info_tipo_fijacion = input("Ingrese el nuevo tipo de fijación: ")
        nueva_info_tamaño = input("Ingrese el nuevo tamaño: ")  
        # Actualizar la información de la clase
        lista_implantes[num_implante - 1].__init__ = lambda self, material=nueva_info_material, tipo_fijacion=nueva_info_tipo_fijacion, tamaño=nueva_info_tamaño: ImplanteMedico.__init__(self, material, tipo_fijacion, tamaño)
        print("Información del tipo de implante actualizada correctamente.")
    else:
        print("Número de tipo de implante no válido.")

def visualizar_inventario_implantes():
    if not lista_implantes:
        print("No hay tipos de implantes registrados.")
        return

    print("Inventario de tipos de implantes:")
    for i, implante in enumerate(lista_implantes):
        print(f"{i + 1}. {implante.__name__}")   
        # Menú principal
while True:
    print("\n--- Menú Principal\n1. Crear paciente\n2. Asignar implante a paciente\n3. Mostrar inventario de pacientes y sus implantes\n4. Edición de Implantes\n5. Salir ---")
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    if opcion == "1":
        crear_paciente()
    elif opcion == "2":
        asignar_implante()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        editar_implantes()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")   