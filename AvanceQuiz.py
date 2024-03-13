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
    

