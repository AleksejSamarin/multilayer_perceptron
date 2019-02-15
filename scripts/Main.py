from scripts.NeuralNetwork import *

if __name__ == '__main__':
    inputs = np.array([[0, 0, 1], # 4 training sets (3 signals)
                       [0, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    outputs = np.array([[0, 1, 1, 0]]).T # 4 training sets (1 signal)

    network = NeuralNetwork(5000, 0.1, [3, 5, 6, 1]) # set configuration
    network.train(inputs, outputs)
    network.print_layer()