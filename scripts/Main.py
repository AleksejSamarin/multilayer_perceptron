from scripts.NeuralNetwork import *
from scripts.FileWorker import *
from scripts.Graphics import *
from scripts.Window import *

if __name__ == '__main__':
    network = NeuralNetwork(800, 0.5, [35, 6, 19, 4]) # set configuration / 2025 - images
    worker = FileWorker('resources/arrays.npz')
    graphics = Graphics('sources/image_1.png', 'sources/', 45, 4, 388, 13, 22) # set parts data
    window = Window(network, worker, graphics)