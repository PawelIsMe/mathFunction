import math
import numpy as np
import matplotlib.pyplot as plt

class QuadraticFunc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Calculating zero places with delta
    def f_kwadratowa(self):
        if self.b**2 >= 4*self.a*self.c and self.a != 0:
            x1 = (-self.b-math.sqrt(self.b**2-(4*self.a*self.c)))/(2*self.a)
            x2 = (-self.b+math.sqrt(self.b**2-(4*self.a*self.c)))/(2*self.a)
            self.draw()
            return f"F.Kwadratowa: x1 = {x1}; x2 = {x2}"
        elif self.a == 0 and self.b != 0:
            x = -self.c/self.b
            self.draw()
            return f"F.Liniowa: x = {x}"
        else:
            return "Nie ma rozwiazan!!"


    def draw(self):
        x = np.linspace(-10, 10, 400)

        # Setting a global font color on the chart
        plt.rcParams['text.color'] = 'white'
        plt.rcParams['axes.labelcolor'] = 'white'
        plt.rcParams['xtick.color'] = 'white'
        plt.rcParams['ytick.color'] = 'white'

        fig, ax = plt.subplots()

        # Calculating a value y for quadratic function
        y = self.a * x**2 + self.b * x + self.c
        ax.plot(x, y, color='red', label=f"f(x) = {self.a}x² {'+ ' if self.b >= 0 else '- '}{abs(self.b)}x {'+ ' if self.c >= 0 else '- '}{abs(self.c)}")

        # Setting for x-axis and y-axis
        ax.spines['left'].set_position('zero')   # Oś Y na 0
        ax.spines['bottom'].set_position('zero') # Oś X na 0
        ax.spines['left'].set_color('black')  # Oś Y
        ax.spines['bottom'].set_color('black')  # Oś X
        ax.spines['left'].set_linewidth(2)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.patch.set_facecolor('#85929E')
        fig.patch.set_facecolor('#85929E')

        # Adding a title
        ax.set_title('Wykres funkcji kwadratowej', color='black')

        # Adding grid and legend
        ax.grid(True, color='white')
        legend = ax.legend()

        for text in legend.get_texts():
            text.set_color('red')

        # Displaying a graph
        plt.savefig('static/graph.png')
        # plt.show()

