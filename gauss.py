from manim import *
import numpy as np
from scipy.interpolate import CubicSpline

class Campana (Scene):
    def construct(self):

        # Títulos
        title = Text("Distribución de Gauss").scale(0.9).shift(UP*3.5)
        # Fórmulas
        u = MathTex(
            r"\mu = E(X) = \sum_{i=1}^{n} x_i \cdot P(X = x_i)"
        ).scale(1).shift(UP*0.4)

        formula = MathTex(
            r"f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}"
        ).scale(1).shift(UP*2.3)

    
        res = MathTex(r"\mu = 1450").shift(UP * 0.4)

        res_desv = MathTex(r"\sigma = 400").shift(DOWN*1.4)
        

        desv = MathTex(
            r"\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}"
        ).scale(1).shift(DOWN*1.4)
        
        # Agrupar y mostrar
        self.play(Write(title))
        self.wait(2)
        self.play(Write(formula))
        self.play(Write(u))
        self.play(Write(desv))

        #self.play(FadeOut(expected_value))
        #Pongo el valor calculado de u
        self.play(Transform(u, res), run_time = 2)
        #self.play(FadeOut(variance))
        #Pongo el valor calculado de sigma
        self.play(Transform(desv, res_desv))

        self.play(formula.animate.scale(0.8), run_time = 1.5)
        self.play(formula.animate.shift(RIGHT * 3.4), run_time = 1.2)


        #Mover los resultados a la derecha
        self.play(u.animate.shift(DOWN * 0.3 + RIGHT * 3), run_time = 0.4)
        self.wait(0.5)
        self.play(desv.animate.shift(DOWN * 0.3 + RIGHT * 3),  run_time = 0.4)
        self.wait(0.5)
        # Esperar para ver
        self.wait(1)



class Graf(Scene):
    def construct(self):

        #ENCABEZADO
        encabez = MathTex(r"P(", r"x_1", r"<", r"X", r"<", r"x_2", r")", r"=", r"?")
        encabez.scale(1.2).to_edge(UP) 

        #INTEGRAL
        integral = MathTex(r"\int_{x_1}^{x_2} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}} \, dx")
        integral.scale(1).to_edge(UP)

        # Creación de ejes
        axes = Axes(
            x_range=(350, 2450, 100),  # Ajustar rango x
            y_range=(0, 0.0015, 0.0001),  # Ajustar rango y,
        #configuro parámetros como flechas del eje:
            axis_config={"color": WHITE},
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
        )
        # Agregar ticks personalizados
        
       #---------------------------------  DEFINICIÓN DE FUNCIÓN NORMAL ----------------------------------------

        def normal(x):
            # Parámetros de la distribución normal
            mu = 1450
            sigma = 400
            return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # Graficar la función de densidad de probabilidad
        graf = axes.plot(normal, color=BLUE)

        #FUNCIONES
        # ----------------------------------- VER EL ÁREA DE LA GRÁFICA --------------------------------------
        # Con esto propongo el intervalo en el cual queremos ver el área (alrededor de mu)
        #x0, x1 = mu - sigma, mu + sigma  # Intervalo de una desviación estándar
        x0, x1 = 1000, 1900
        area = axes.get_area(
            graf,
            x_range=(x0, x1),
            color=BLUE_E,
            opacity=0.4,
        )

        # Etiquetas para el área y los puntos
        label_x0 = MathTex(f"x_1 = {x0}").scale(0.7).next_to(axes.c2p(x0, 0), DOWN + RIGHT*0.3)
        label_x1 = MathTex(f"x_2 = {x1}").scale(0.7).next_to(axes.c2p(x1, 0), DOWN + RIGHT *0.3)




        # ----------------------------------------------------------------------------------------------------
        #  ------------------------------- DIBUJAR 9 PUNTOS -------------------------------------------------
        # Definir 9 puntos x
        x_values = [1000,1150,1300,1450,1600,1750,1900]
        points = VGroup()  # Agrupar los puntos

        # Crear los puntos y añadirlos al grupo
        for x in x_values:
            y = normal(x)
            point = Dot(axes.c2p(x, y), color=WHITE).scale(0.8) # Crear un punto en (x, f(x))
            points.add(point)  # Añadir el punto al grupo


        
        # Agrupar ejes y gráfica para moverlos juntos 
        graf_ejes = VGroup(axes, graf, area, points)
        graf_ejes.shift(RIGHT * 0.4)



        # -------------------------------------- DIBUJAR A LAS PARÁBOLAS  -------------------------------------------#
        def graficar_area(self, axes, abcisas, ordenadas):
            # Crear un spline cúbico para interpolar una función.
            cs = CubicSpline(abcisas, ordenadas)

            # Graficar la función interpolada
            parab = axes.plot(cs, color=BLUE, stroke_width=2)
            # Calcular los límites para el área
            x_min = min(abcisas)
            x_max = max(abcisas)
            # Crear el área bajo la curva entre los puntos más lejanos
            area = axes.get_area(parab, x_range=[x_min, x_max], color=GREEN, opacity=0.5)
            # Mostrar elementos
            self.play(Create(axes))
            self.play(Create(parab))
            self.play(FadeIn(area))
            self.wait(2)

        ## INSTANCIAS DEL MÉTODO DE PARÁBOLAS:
        self.graficar_area(axes, [1000, 1150, 1300], [normal(1000), normal(1150), normal(1300)])
        self.graficar_area(axes, [1300, 1450, 1600], [normal(1300), normal(1450), normal(1600)])
        self.graficar_area(axes, [1600, 1750, 1900], [normal(1600), normal(1750), normal(1900)])

        #------------------------------------------  ANIMACION ------------------------------------------------------#
        
        # Mostrar primero los ejes y luego la gráfica
        self.play(Create(axes), run_time=2)
        self.wait(1)  # Espera para resaltar el momento en que aparecen los ejes
        self.play(Create(graf), run_time=3)
        self.play(Write(label_x0), Write(label_x1))
        #hago la pregunta:
        self.play(Write(encabez))
        self.wait(2)
        self.play(Transform(encabez, integral), run_time = 1.5)
        self.wait(1)
        #Dibujo el área:
        
    
        self.play(DrawBorderThenFill(area), run_time = 2)
        self.wait(2)
        self.play(FadeOut(area))


        #---------------------------------
        self.play(Create(points), run_time = 2)  # Dibujar los puntos

        #---------------------------------
        #lineas de punto:
        
        def seg_punteado(x_0):
            y_0 = normal(x_0)  # Obtener el valor de f(x_0)
            linea_punteada = DashedLine(start=axes.c2p(x_0, 0), end=axes.c2p(x_0, y_0), color=GREEN)

            # Muestro la línea punteada
            self.play(Create(linea_punteada), run_time=2)

        # Lleno los valores de x_0
        puntos_x = [1000, 1300, 1600, 1900]

        # Usaré un bucle para hacer las llamadas
        for x_0 in puntos_x:
            seg_punteado(x_0)  # Crear línea punteada en x_0

        # Esperar para ver
        self.wait(1)



class Todo(Scene):
    def construct(self):
        Campana.construct(self)
        Graf.construct(self)

        



