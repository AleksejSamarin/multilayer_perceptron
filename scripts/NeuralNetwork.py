import numpy as np

class NeuralNetwork:

    def __init__(self, epochs, rate, structure):
        self.epochs = epochs
        self.rate = rate
        self.structure = structure
        self.levels = len(structure)


    def change_inputs(self, to_change):
        result = np.concatenate((to_change, to_change))
        return self.noise(result, 0.2)


    def noise(self, value, probability):
        value[np.random.rand(*value.shape) < probability] ^= 1
        return value


    def train(self, inputs, outputs, test=False):
        if test:
            self.noise_inputs = self.change_inputs(inputs)
            self.outputs_for_test = np.concatenate((outputs, outputs))

        self.prepare(inputs)
        for j in range(self.epochs):
            for i in range(1, self.levels):
                self.layers[i] = self.count_function(np.dot(self.layers[i - 1], self.synapses[i - 1]), 0.1 * i**3)  # counting neuron weights

            self.errors[-1] = outputs - self.layers[-1]  # first error count
            self.deltas[-1] = self.errors[-1] * self.count_function(self.layers[-1], None, True)  # check direction of the target value

            for i in range(self.levels - 2, 0, -1):
                self.errors[i - 1] = self.deltas[i].dot(self.synapses[i].T)
                self.deltas[i - 1] = self.errors[i - 1] * self.count_function(self.layers[i], None, True)

            for i in range(self.levels - 1, 0, -1):
                self.synapses[i - 1] += self.layers[i - 1].T.dot(self.deltas[i - 1]) * self.rate

            self.mean_square_train_error.append(np.mean(self.errors[-1] ** 2))
            if test:
                self.check(self.noise_inputs) #self.change_inputs(inputs)
                error = self.outputs_for_test - self.layers[-1]
                self.mean_square_test_error.append(np.mean(error ** 2))
        # self.print_layer()


    def prepare(self, inputs):
        # np.random.seed(1)
        self.mean_square_train_error, self.mean_square_test_error = [], []
        self.synapses, self.layers, self.errors, self.deltas = [], [], [], []
        self.layers.append(inputs)  # layer initialization
        for i in range(1, self.levels):  # synaptic link weights initialization
            self.synapses.append(2 * np.random.random((self.structure[i - 1], self.structure[i])) - 1)
            self.layers.append([])
            self.errors.append([])
            self.deltas.append([])


    def check(self, inputs):
        prev = self.layers[0]
        self.layers[0] = inputs
        for i in range(1, self.levels):
            self.layers[i] = self.count_function(np.dot(self.layers[i - 1], self.synapses[i - 1]), 0.1 * i**3)
        self.layers[0] = prev


    def get_response(self, inputs):
        self.check(inputs)
        self.print_layer()
        print(f"Compatible picture: {self.layers[self.levels - 1].argmax(axis=0) + 1}")
        # print("Error test: ", np.mean(self.errors[self.levels - 2] ** 2))


    def count_function(self, x, a, derivative=False):
        if (derivative == True):
            return x * (1 - x)
        return 1 / (1 + np.exp(-x * a))


    def print_error(self, epoch):
        if (epoch % (self.epochs / 5)) == 0:
            print("Error: ", np.mean(self.errors[self.levels - 2]**2))  # mean square error


    def print_layer(self):
        print(np.array_str(self.layers[self.levels - 1], precision=5, suppress_small=True))