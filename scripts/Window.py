from scripts.Canvas import *
from scripts.Plot import *
import sys
import random

class Window():

    def __init__(self, network, worker, graphics):
        self.root = tkinter.Tk(className=' Neural network')
        self.root.configure(background='white')
        self.root.resizable(False, False)
        self.canvases = []
        self.f_top = tkinter.Frame()
        self.f_bot = tkinter.Frame()
        self.f_top.pack()
        self.f_bot.pack()

        data = worker.load_arrays()

        self.root.bind("<Return>", lambda l: self.run(network, data, self.get_codes()[0]))
        self.root.bind("<c>", lambda l: network.get_response(self.get_codes()[1]))
        self.root.bind("<l>", lambda l: self.load_canvases(worker))
        self.root.bind("<Control-s>", lambda l: worker.save_arrays(self.get_codes()[0], data['outputs'], self.get_codes()[1]))

        self.root.bind("<i>", lambda l: self.run(network, data, None, graphics))
        self.root.bind("<m>", lambda l: network.get_response(self.get_image_codes(graphics)))
        self.root.bind("<Escape>", self.exit)

        for i in range(5):
            canvas = Canvas(self.f_top, width=125, height=170, background='blue')
            canvas.pack(side="left")
            self.canvases.append(canvas)
        self.plot = Plot(self.root, self.f_bot)

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.after(1000, lambda: self.root.focus_force())
        self.root.mainloop()
        return


    def load_canvases(self, worker):
        data = worker.load_arrays()
        for idx, canvas in enumerate(self.canvases[:-1]):
            canvas.color_from_code(data['inputs'][idx])
        self.canvases[-1].color_from_code(data['test'])


    def run(self, network, data, now, graphics=None):
        if graphics == None:
            network.train(now, data['outputs'], True)
        else:
            network.train(graphics.get_codes(), data['outputs'], True)
        self.plot.draw(network.mean_square_train_error, network.mean_square_test_error)


    def get_codes(self, event=None):
        inputs = []
        for canvas in self.canvases[:-1]:
            inputs.append(canvas.get_code())
        test = self.canvases[-1].get_code()
        return np.array(inputs), np.array(test)


    def get_image_codes(self, graphics, event=None):
        number = random.randint(1, 4)
        noise = bool(random.getrandbits(1))
        return graphics.get_image_code(number, noise)


    def exit(self, event=None):
        self.root.withdraw()
        sys.exit()
