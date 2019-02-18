from scripts.NeuralNetwork import *
from scripts.FileWorker import *
from scripts.Window import *

if __name__ == '__main__':
    network = NeuralNetwork(1000, 1, [35, 6, 13, 4]) # set configuration
    worker = FileWorker('resources/arrays.npz')
    ui = Window(network, worker)