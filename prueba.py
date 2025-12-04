#Esta linea de importación siempre debe ir primero
from manim import *

class Mover(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))


#CLASE PARA PRESENTAR LOS PUNTOS:

from manim import *

class Puntos(Scene):
    def construct(self):
        # Crear un plano cartesiano
        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-5, 5],
            background_line_style={"stroke_color": BLUE_E, "stroke_opacity": 0.5}
        )
        
        # Lista de puntos en coordenadas (x, y)
        points = [(-4, 3), (-2, 1), (0, -1), (2, -2), (4, 3)]

        # Se crea un arreglo o lista de objetos, en este caso es una lista de objetos -> punto
        dots = VGroup()  
        # Y otro grupo para las otras coordenadas.
        labels = VGroup()  

        # FOR EACH para recorrer los puntos por cada iteración.
        for x, y in points: #{
            # Crear el punto
            dot = Dot(plane.coords_to_point(x, y), color=RED)
            dots.add(dot)  # Agregar el punto al grupo de puntos
            
            # Crear la etiqueta
            label = MathTex(f"({x},{y})" , font_size = 18).next_to(dot, UP)
            
            labels.add(label)  # Agregar la etiqueta al grupo de etiquetas
        #  }

        # Mostrar el plano cartesiano, los puntos y las etiquetas
        self.play(Create(plane), run_time = 3)
        self.play(Create(dots), Write(labels), run_time  = 2.5)
        self.wait(2)
        self.play(FadeOut(labels))
        self.wait(2)


