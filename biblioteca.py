from claseLibro import Libro
from claseUsuario import Usuario


#Crear un programa para una biblioteca en el cual se puedan cargar libros, los cuales cuentan con
# la siguiente informacion: título, autor, ISBN(numero identificador), páginas, edición, editorial,
# lugar (ciudad y país) y fecha de edición. La biblioteca cuenta ademas con usuarios, los cuales 
# tienen informacion como nombre y apellido, edad, numero de socio, y libros que pidieron prestados
# para la biblioteca. Al crear el programa, contemplar las siguientes reglas del negocio:
#Un libro solo puede prestarse a una persona
#Un usuario no puede tener mas de dos libros de la biblioteca al mismo tiempo



libros = []
l1 = Libro("hola", "autor1", "123", "d")
l2 = Libro("chau", "autor2", "321", "D")
libros.append(l1)
libros.append(l2)

usuarios = []
u1 = Usuario("asd", "qwe", "12", "1234", 0)
u2 = Usuario("lkj", "qwe", "23", "4321", 2)
usuarios.append(u1)
usuarios.append(u2)



def estado_de_libro(consulta_libro):
    for libro in libros:
        if consulta_libro == libro.ver_titulo():
            posicion = libros.index(libro)
            return libros[posicion].ver_estado(), posicion
        else:
            print ("Libro no encontrado")


def usuario_libros_prestados(usuario_registrado):
    for usuario in usuarios:
        if usuario_registrado == usuario.ver_nro_socio():
            posicion_usuario = usuarios.index(usuario)
            return usuario.ver_libros_prestados(), posicion_usuario
            
        else:
            print("usuario no registrado")



def nuevo_prestamo(posicion_usuario_prestamo):
    for usuario_registrado in usuarios:
        posicion_usuario = usuarios.index(usuario_registrado)
        return posicion_usuario
        #cargar_nuevo_prestamo = usuarios[posicion_usuario].append(titulo_libro_prestamo)

    

opciones = int(input("Ingrese 1 para registrar nuevo libro, 2 para registrar nuevo usuario, 3 para préstamo "))

if opciones == 1:
    cargar_titulo = input("Ingrese nombre del libro ")
    cargar_autor = input("Ingrese autor ")
    cargar_ISBN = input("Ingrese número identificador ")
    cargar_estado = input("Ingrese P si será prestado o D si está disponible ")
    cargar_libro = Libro(cargar_titulo, cargar_autor, cargar_ISBN,cargar_estado)

if opciones == 2:
    cargar_nombre = input("Ingrese nombre ")
    cargar_apellido = input("Ingrese apellido ")
    cargar_edad = input("Ingrese edad ")
    cargar_nro_socio = input("Ingrese nro de socio ")
    cargar_libros_prestados = input("Ingrese el número de libros a prestar ")
    cargar_usuario = Usuario(cargar_nombre, cargar_apellido, cargar_edad, cargar_nro_socio, cargar_libros_prestados)


if opciones == 3:
    consulta_libro = input("Ingrese el nombre para localizar el estado del libro ")
    disponibilidad, posicion_libro = estado_de_libro(consulta_libro)
    if disponibilidad == "p":
        print("El libro no se encuentra disponible en este momento")
    else:
        print("Préstamo disponible")

        usuario_registrado = input("Ingrese número de socio ")
        usuario_para_prestamo = nuevo_prestamo(usuario_registrado)

        libros_en_uso, posicion_usuario_prestamo = usuario_libros_prestados(usuario_registrado)
        if libros_en_uso >= 2:
            print("Ha superado la cantidad máxima de libros prestados")
        else:
            libros_para_prestamo = 2
            libros_disponibles = 0
            libros_disponibles = libros_para_prestamo - libros_en_uso
            print("El usuario tiene {} libros disponibles para préstamo".format(libros_disponibles))
        
    
            nuevo_libro = libros_disponibles
            usuarios[posicion_usuario_prestamo].modificar_alta_libro(nuevo_libro)
            
            print(usuarios[posicion_usuario_prestamo].ver_libros_prestados())

            estado_actual = input("El libro {} será prestado? Ingrese P para préstamo o D para devolución".format(libros[posicion_libro].ver_titulo()))
            
            libros[posicion_libro].modificar_estado(estado_actual)
            if estado_actual == "p":
                print("Préstamo exitoso")
                print(libros[posicion_libro].ver_estado())
            if estado_actual == "d":
                print("Libro devuelto a biblioteca")
                print(libros[posicion_libro].ver_estado())









