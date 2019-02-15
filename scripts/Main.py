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

    network = NeuralNetwork(1000, 0.1, [3, 5, 11, 4]) # set configuration
    network.train(inputs, outputs)
    network.print_layer()

    network.check(tests)
    network.print_layer()