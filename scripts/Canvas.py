import tkinter
import numpy as np

class Canvas(tkinter.Canvas):
    WIDTH = 25
    HEIGHT = 25
    GRID_W = 5
    GRID_H = 7

    def __init__(self, *args, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)
        self.squares = []
        self.create_squares()
        self.bind("<Button-1>", self.change)


    def create_squares(self):
        for j in range(self.GRID_H):
            for i in range(self.GRID_W):
                x1 = i * self.WIDTH
                y1 = j * self.HEIGHT
                x2 = x1 + self.WIDTH
                y2 = y1 + self.HEIGHT
                s = self.create_rectangle(x1, y1, x2, y2, fill=self.get_hex(255, 255, 255), tag="{}{}".format(i, j))
                self.squares.append(s)
        return


    def change(self, event=None):
        overlapped = self.find_withtag("current")
        if self.type(overlapped) == 'rectangle':
            new_color = (0, 0, 0) if not self.is_square_marked(overlapped) else (255, 255, 255)
            self.itemconfig(overlapped, fill=self.get_hex(*new_color))
        return


    def get_code(self):
        return [1 if self.is_square_marked(square) else 0 for square in self.squares]


    def is_square_marked(self, index):
        return self.hex_to_rgb(self.itemcget(index, "fill")) == (0, 0, 0)


    def get_hex(self, x, y, z):
        return "#%02x%02x%02x" % (x, y, z)


    def hex_to_rgb(self, hex):
        code = hex.replace('#', '')
        return tuple(int(code[i:i + 2], 16) for i in (0, 2, 4))


    def color_from_code(self, code):
        for idx, square in enumerate(self.squares):
            new_color = (0, 0, 0) if not code[idx] == 0 else (255, 255, 255)
            self.itemconfig(square, fill=self.get_hex(*new_color))