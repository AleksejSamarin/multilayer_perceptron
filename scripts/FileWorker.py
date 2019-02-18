import numpy as np

class FileWorker:

    def __init__(self, path):
        self.path = path


    def load_arrays(self, default=False):
        if not default:
            for attempt in range(2):
                try:
                    data = np.load(self.path)
                except:
                    inputs = np.zeros((4, 3))
                    inputs_height, inputs_width = inputs.shape
                    outputs = np.diag(np.ones(inputs_height))
                    test = np.zeros(inputs_width)
                    self.save_arrays(inputs, outputs, test)
                    print("There is no data file. Default file created.")
                    continue
                return data
        else:
            inputs = np.array([[0, 0, 1],
                               [0, 1, 1],
                               [1, 0, 1],
                               [1, 1, 1]])

            outputs = np.array([[0, 1, 1, 0],
                                [0, 0, 1, 1],
                                [1, 1, 1, 1],
                                [1, 0, 1, 1]])

            test = np.array([1, 1, 0])
            data = {'inputs': inputs,
                    'outputs': outputs,
                    'test': test}
            return data


    def save_arrays(self, inputs, outputs, test):
        np.savez(self.path, inputs=inputs, outputs=outputs, test=test)
