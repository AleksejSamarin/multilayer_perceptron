import numpy as np

class NeuralNetwork:

    def __init__(self, epochs, rate, structure):
        self.epochs = epochs
        self.rate = rate
        self.structure = structure
        self.levels = len(structure)
        self.layers, self.synapses, self.errors, self.deltas = [], [], [], []


    def train(self, inputs, outputs):
        self.prepare(inputs)
        for j in range(self.epochs):
            for i in range(1, self.levels):
                self.layers[i] = self.count_function(np.dot(self.layers[i - 1], self.synapses[i - 1]))  # counting neuron weights

            self.errors[self.levels - 2] = outputs - self.layers[self.levels - 1]  # first error count
            self.deltas[self.levels - 2] = self.errors[self.levels - 2] * self.count_function(self.layers[self.levels - 1], True) # check direction of the target value

            for i in range(self.levels - 2, 0, -1):
                self.errors[i - 1] = self.deltas[i].dot(self.synapses[i].T)
                self.deltas[i - 1] = self.errors[i - 1] * self.count_function(self.layers[i], True)

            for i in range(self.levels - 2, -1, -1):
                self.synapses[i] += self.layers[i].T.dot(self.deltas[i]) * self.rate

            self.print_error(j)
        self.print_layer()


    def prepare(self, inputs):
        self.layers, self.synapses, self.errors, self.deltas = [], [], [], []
        np.random.seed(1)
        for i in range(1, self.levels):  # synaptic link weights initialization
            self.synapses.append(2 * np.random.random((self.structure[i - 1], self.structure[i])) - 1)
        self.layers.append(inputs)  # layer initialization
        for i in range(self.levels - 1):
            self.layers.append([])
            self.errors.append([])
            self.deltas.append([])


    def check(self, inputs):
        self.layers[0] = inputs
        for i in range(1, self.levels):
            self.layers[i] = self.count_function(np.dot(self.layers[i - 1], self.synapses[i - 1]))
        self.print_layer()
        #print("Error test: ", np.mean(self.errors[self.levels - 2] ** 2))
        #print(self.layers[self.levels - 1] >= 0.5)


    def count_function(self, x, derivative=False):
        if (derivative == True):
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))


    def print_error(self, epoch):
        if (epoch % (self.epochs / 5)) == 0:
            print("Error: ", np.mean(self.errors[self.levels - 2]**2))  # mean square error


    def print_layer(self):
        print(self.layers[self.levels - 1])