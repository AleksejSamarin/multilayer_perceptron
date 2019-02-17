from scripts.Canvas import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import sys

class Window():

    def __init__(self, network, worker):
        self.root = tkinter.Tk(className=' Neural network')
        self.root.configure(background='white')
        self.root.resizable(False, False)
        self.canvases = []
        self.f_top = tkinter.Frame()
        self.f_bot = tkinter.Frame()
        self.f_top.pack()
        self.f_bot.pack()

        data = worker.load_arrays()

        self.root.bind("<Return>", lambda l: network.train(data['inputs'], data['outputs']))
        self.root.bind("<c>", lambda l: network.check(data['test']))
        self.root.bind("<l>", lambda l: self.load_canvases(worker))
        self.root.bind("<Control-s>", lambda l: worker.save_arrays(self.get_codes()[0], data['outputs'], self.get_codes()[1]))
        self.root.bind("<Escape>", self.exit)

        for i in range(5):
            canvas = Canvas(self.f_top, width=125, height=170, background='blue')
            canvas.pack(side="left")
            self.canvases.append(canvas)

        self.build_plot()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.mainloop()
        return


    def load_canvases(self, worker):
        data = worker.load_arrays()
        for idx, canvas in enumerate(self.canvases[:-1]):
            canvas.color_from_code(data['inputs'][idx])
        self.canvases[-1].color_from_code(data['test'])


    def build_plot(self):
        figure = plt.Figure(figsize=(6.4, 5), dpi=100)
        plot = figure.add_subplot(111)
        X = np.linspace(-5, 5, 100)
        plot.plot(X, 1 / (1 + np.exp(-X * 1)), 'b')
        plot.plot(X, 1 / (1 + np.exp(-X * 2)), 'r')
        plot.set_title('Mean square errors')
        plot.set_xlabel('Epoch number')
        plot.set_ylabel('Error value')
        plot.legend(["Train", "Test"], loc=1)
        plot.grid()
        chart_type = FigureCanvasTkAgg(figure, self.f_bot)
        chart_type.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(chart_type, self.root)
        toolbar.config(background='white')
        toolbar._message_label.config(background='white')
        toolbar.update()
        chart_type.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    def get_codes(self, event=None):
        inputs = []
        for canvas in self.canvases[:-1]:
            inputs.append(canvas.get_code())
        test = self.canvases[-1].get_code()
        return np.array(inputs), np.array(test)


    def exit(self, event=None):
        self.root.withdraw()
        sys.exit()
