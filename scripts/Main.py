from scripts.NeuralNetwork import *

if __name__ == '__main__':
    inputs = np.array([[0, 0, 1],
                       [0, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    outputs = np.array([[0, 1, 1, 0],
                        [0, 0, 1, 1],
                        [1, 1, 1, 1],
                        [1, 0, 1, 1]])

    tests = np.array([0, 1, 0])

    inputs_height, inputs_width = inputs.shape
    network = NeuralNetwork(5000, 0.1, [inputs_width, 6, 13, 4]) # set configuration
    network.train(inputs, outputs)
    network.print_layer()

    network.check(tests)
    network.print_layer()