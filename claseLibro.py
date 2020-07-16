class Libro:
    def __init__(self, titulo, autor, ISBN, estado):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.estado = estado

    def ver_titulo(self):
        return self.titulo 

    def ver_ISBN(self):
        return self.ISBN

    def ver_estado(self):
        return self.estado

    def modificar_titulo(self, nuevo_titulo):
        antiguo_titulo = self.titulo
        nuevo_titulo = antiguo_titulo
        self.titulo = nuevo_titulo

    def modificar_estado(self, estado_actual):
        estado_previo = self.titulo
        estado_actual = estado_previo
        self.estado = estado_actual
        



