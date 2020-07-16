class Usuario:
    def __init__(self, nombre, apellido, edad, nro_socio, libros_prestados):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nro_socio = nro_socio
        self.libros_prestados = libros_prestados

    def ver_nro_socio(self):
        return self.nro_socio

    def ver_libros_prestados(self):
        return self.libros_prestados

    def modificar_nombre(self, nuevo_nombre):
        nombre_actual = self.nombre
        nuevo_nombre = nombre_actual
        self.nombre = nuevo_nombre

    def modificar_alta_libro(self, nuevo_libro):
        libro_en_prestamo = self.libros_prestados
        nuevo_libro = libro_en_prestamo
        self.libros_prestados = nuevo_libro
    


    

    

    
