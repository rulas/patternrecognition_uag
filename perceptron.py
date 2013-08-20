'''
Created on Aug 19, 2013

@author: lrvillan
'''
import numpy as np


class Perceptron(object):
    '''
        Percepton class 
    '''

    def __init__(self, vector_size, learning_rate=0.1, threshold=0):
        '''
        Constructor
        '''
        self.input_size = vector_size
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.unit_step = lambda x: 1 if x >= self.threshold else 0
        self.required_decades = 0

    def train(self, training_set, max_decades=1000):
        """
            train the perceptron using the given set and updates the weights
            accordingly.
            :param training_set:    a list containing a list of input vectors and the desired output.
                                    ie: training_set = [((1, 0, 0), 1),
                                                        ((1, 0, 1), 1),
                                                        ((1, 1, 0), 1),
                                                        ((1, 1, 1), 0)]
            :param num_decades:        indicates how many times the training
            algorithms should attempt to find the weight values
        """
        # initializes weights to random values
        self.weights = np.random.rand(self.input_size)
        learning_done = False
        cur_decade = 0

        while not learning_done and max_decades:
            learning_done = True
            cur_decade += 1
            max_decades -= 1
            for input_vector, desired_output in training_set:
                weighted_sum = np.dot(input_vector, self.weights)
                result = self.unit_step(weighted_sum)
                error = desired_output - result
                if error != 0:
                    learning_done = False
                    weights_update = self.learning_rate * error * np.array(input_vector)
                    self.weights = self.weights + weights_update

        self.required_decades = cur_decade

        self.dump()

    def dump(self):
        print "threshold = %0.2f" % self.threshold
        print "learning rate = %0.2f" % self.learning_rate
        print "weights = %s" % self.weights
        print "required decades = %d" % self.required_decades
        

    def classify_vector(self, input_vector):
        weighted_sum = np.dot(input_vector, self.weights)
        return (weighted_sum, self.unit_step(weighted_sum))

if __name__ == "__main__":
    p = Perceptron(vector_size=3, threshold=0.5)

    training_data = [([0, 0, 1], 0),
                     ([0, 1, 1], 1),
                     ([1, 0, 1], 1),
                     ([1, 1, 1], 1)]

    p.train(training_data, max_decades=1000)

    for input_vector, _ in training_data:
        print p.classify_vector(input_vector)
