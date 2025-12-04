from manim import *
import numpy as np
from scipy.interpolate import CubicSpline

class Normal(Scene):
    def construct(self):
        # Notas del alumno de un parcial
        
        #notas = [4, 14, 33, 34, 35, 38, 43, 47, 49, 51, 52, 53, 60, 61, 66, 68, 76, 82]
        notas = [0, 10, 20, 30, 40, 50, 60, 70, 80]
        

        #Frecuencia/ocurrencia de cada nota

        #frec = [0.043, 0.043, 0.13, 0.13, 0.13, 0.13, 0.13, 0.304, 0.304, 0.304, 0.304, 0.304, 0.173, 0.173, 0.13, 0.13, 0.086, 0.086]
        frec = [0.043, 0.043, 0.0, 0.13, 0.13, 0.304, 0.173, 0.13, 0.086]

        # Crear el plano cartesiano
        axes = Axes(
            x_range=[0, 85, 5],   # Ajustado al rango de tus datos (min=4, max=82)
            y_range=[0, 0.35, 0.05],  # Ajustado al rango de frecuencias (max≈0.304)
            axis_config={"color": BLUE},
        )

        # Crear el spline cúbico
        cs = CubicSpline(notas, frec)

        # Crear un rango de puntuaciones para graficar el spline
        x_new = np.linspace(min(notas), max(notas), 100)
        y_new = cs(x_new)

        # Graficar la función interpolada
        graph = axes.plot(cs, color=YELLOW)

        # Crear y mostrar los puntos
        dots = VGroup()  # Crear un grupo vacío para los puntos
        for i in range(len(notas)):
            # Crear cada punto
            dot = Dot(axes.c2p(notas[i], frec[i]), color=RED)
            dots.add(dot)  # Añadir el punto al grupo

        # Mostrar elementos
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Create(dots))
        self.wait(2)
