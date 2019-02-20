from scripts.NeuralNetwork import *
from scripts.FileWorker import *
from scripts.Graphics import *
from scripts.Window import *

if __name__ == '__main__':
    inputs_count = 35
    if len(sys.argv) > 1:
        inputs_count = int(sys.argv[1])
        print(f"Inputs count: {inputs_count}, press 'i' to start working with images.")

    network = NeuralNetwork(800, 0.5, [inputs_count, 6, 19, 4]) # set configuration: 35 / 2025 inputs
    worker = FileWorker('resources/arrays.npz')
    graphics = Graphics('sources/image_1.png', 'sources/', 45, 4, 388, 13, 22) # set parts data
    window = Window(network, worker, graphics)