import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Plot:

    def __init__(self, root, frame):
        figure = plt.Figure(figsize=(6.4, 5), dpi=100)
        self.plot = figure.add_subplot(111)
        self.plot.set_title('Mean square errors')
        self.plot.set_xlabel('Epoch number')
        self.plot.set_ylabel('Error value')

        self.plot.grid()
        self.chart_type = FigureCanvasTkAgg(figure, frame)
        self.chart_type.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(self.chart_type, root)
        toolbar.config(background='white')
        toolbar._message_label.config(background='white')
        toolbar.update()
        self.chart_type.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    def draw(self, data, extended=None):
        self.plot.lines = []
        self.plot.plot(data, 'b')
        if extended != None:
            self.plot.plot(extended, 'r')
        self.plot.legend(["Train", "Test"], loc=1)
        self.chart_type.draw()