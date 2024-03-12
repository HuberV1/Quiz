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


