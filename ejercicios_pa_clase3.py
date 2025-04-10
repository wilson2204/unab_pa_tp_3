# Ejercicio 2: Clase Punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)

    def distancia_al_origen(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# Ejercicio 3: Clase Linea
class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def mostrar(self):
        return f"A: {self._punto_a.impresion()}, B: {self._punto_b.impresion()}"


# Ejercicio 4: Clase Cancion
class Cancion:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self._autor = nuevo_autor


# Ejercicio 5: Clase Libro y Clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self.titulo = titulo
        self.autor = autor  # instancia de Persona
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha = fecha

    def mostrar_info(self):
        return (f"Título: {self.titulo} {self.edicion}\n"
                f"Autor: {self.autor.nombre}\n"
                f"ISBN: {self.isbn}\n"
                f"{self.editorial}, {self.ciudad} ({self.pais})\n"
                f"{self.fecha}\n"
                f"{self.paginas} páginas\n")
