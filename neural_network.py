'''
Created on Aug 19, 2013

@author: lrvillan
'''
import math
import cPickle
import time

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(value):
    return 1.0 / (1 + math.exp(-value))


class PerceptronAlg(object):
    '''
        Percepton class
    '''

    def __init__(self, learning_rate=0.1, threshold=0):
        '''
        Constructor
        '''
#         self.input_size = vector_size
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.required_cycles = 0

    def calculate_net(self, input_vector):
        """
            calculates the weighted sum (or net) of input vector
            and returns the result.
        """
        net = np.dot(input_vector, self.weights)

        return net 

    def calculate_output(self, weighted_sum):
        output = 1 if weighted_sum >= self.threshold else 0
        return output

    def train(self, training_set, vector_size, max_cycles=1000):
        """
            train the perceptron using the given set and updates the weights
            accordingly.
            :param training_set(list): a list containing a list of input vectors and the desired output.
                                    ie: training_set = [((1, 0, 0), 1),
                                                        ((1, 0, 1), 1),
                                                        ((1, 1, 0), 1),
                                                        ((1, 1, 1), 0)]
            :param num_epochs:        indicates how many times the training
            algorithms should attempt to find the weight values
        """
        self.input_size = vector_size

        # initializes weights to random values
#         self.weights = np.random.rand(self.input_size)
        self.weights = np.zeros(self.input_size)
        learning_done = False
        cur_cycle = 0
        errors = []

        while not learning_done and max_cycles:
            learning_done = True
            cur_cycle += 1
            max_cycles -= 1
            for input_vector, desired_output in training_set:
                weighted_sum = self.calculate_net(input_vector)
                output = self.calculate_output(weighted_sum)
                error = desired_output - output
                errors.append(error)
                if error != 0:
                    learning_done = False
                    weights_update = self.learning_rate * error * np.array(input_vector)
                    self.weights = self.weights + weights_update

        self.required_cycles = cur_cycle
#         plt.plot(errors)
#         plt.ion()
#         plt.draw()

        self.dump()

    def dump(self):
        print "threshold = %0.2f" % self.threshold
        print "learning rate = %0.2f" % self.learning_rate
        print "weights = %s" % self.weights
        print "required cycles = %d" % self.required_cycles

    def classify_vector(self, input_vector):
        weighted_sum = self.calculate_net(input_vector)
        output = self.calculate_output(weighted_sum)
        return output

    def get_num_weights(self):
        return self.input_size

    def get_num_cycles(self):
        return self.required_cycles


class AdalineAlg(PerceptronAlg):
    """
        Adaline algorithm class
    """
    def calculate_net(self, input_vector):
        return PerceptronAlg.calculate_net(self, input_vector)

    def calculate_output(self, weighted_sum):
        return weighted_sum

    def train(self, training_set, vector_size, desired_error, max_cycles=1000):
        self.input_size = vector_size

        # initializes weights to random values
        self.weights = np.zeros(self.input_size)
        cur_cycle = 0
        error_acc = 0
        errors = []

        while error_acc <= desired_error and cur_cycle < max_cycles:
            cur_cycle += 1
            error_acc = 0
            for input_vector, desired_output in training_set:
                net = self.calculate_net(input_vector)
                output = self.calculate_output(net)
                error = desired_output - output
                if error != 0:
                    weights_delta = self.learning_rate * error * \
                        sigmoid(output) * (1 - sigmoid(output)) * \
                        np.array(input_vector)
                    self.weights = self.weights + weights_delta
                error_acc += error ** 2
            error_acc /= len(training_set)
            errors.append(error_acc)
#             print "error_acc = {0}".format(error_acc)

        self.required_cycles = cur_cycle
        plt.plot(errors)

        plt.draw()
#         plt.show()
        self.dump()


class MLN_BackpropAlg(PerceptronAlg):
    pass


class NN:

#     def sigmoid(self,x):
#         return tanh(x)

    # derivative of our sigmoid function
    def dsigmoid(self, y):
        return 1.0 - y * y

    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1  # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = np.ones((self.ni), np.float)
        self.ah = np.ones((self.nh), np.float)
        self.ao = np.ones((self.no), np.float)

        # create weights
        self.wi = np.random.uniform(-2.0, 2.0, (self.ni, self.nh))
        self.wo = np.random.uniform(-2.0, 2.0, (self.nh, self.no))

        # last change in weights for momentum
        self.ci = np.zeros((self.ni, self.nh), np.float)
        self.co = np.zeros((self.nh, self.no), np.float)

    def SaveW(self, filename):
        W = [self.wi, self.wo]
        cPickle.dump(W, open(filename, 'w'))

    def LoadW(self, filename):
        W = cPickle.load(open(filename, 'r'))
        self.wi = W[0]
        self.wo = W[1]

    def classify_vector(self, input_vector):
        return self.update(input_vector)

    def update(self, inputs):
        if len(inputs) != self.ni - 1:
            raise ValueError('wrong number of inputs')

        # input activations
        self.ai[0:self.ni - 1] = inputs

        # hidden activations
        _sum = np.dot(np.transpose(self.wi), self.ai)
        self.ah = np.tanh(_sum)

        # output activations
        _sum = np.dot(np.transpose(self.wo), self.ah)
        self.ao = np.tanh(_sum)

        return self.ao

    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = self.dsigmoid(self.ao) * (targets - self.ao)

        # calculate error terms for hidden
        error = np.dot(self.wo, output_deltas)
        hidden_deltas = self.dsigmoid(self.ah) * error

        # update output weights
        change = output_deltas * np.reshape(self.ah, (self.ah.shape[0], 1))
        self.wo = self.wo + N * change + M * self.co
        self.co = change

        # update input weights
        change = hidden_deltas * np.reshape(self.ai, (self.ai.shape[0], 1))
        self.wi = self.wi + N * change + M * self.ci
        self.ci = change

        # calculate error
        error = sum(0.5 * (targets - self.ao) ** 2)

        return error

    def test(self, patterns):
        for p in patterns:
            print p[0], '->', self.update(p[0])

    def singletrain(self, inputs, targets):
        self.update(inputs)
        return self.backPropagate(targets, 0.5, 0.1)

    def train(self, patterns, iterations=100, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in xrange(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0 and i != 0:
                print 'error ' + str(error)


def demo():
    # Teach network XOR function
    pat = [
        [[0, 0], [-1]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [-1]]
    ]

    # create a network with two input, two hidden, and one output nodes
    a = time.clock()
    n = NN(2, 3, 1)
    #train it with some patterns
    print "Starting bath training"
    n.train(pat, 1000)  # Train is with Back Propagation Algorithm
    # test it
    n.test(pat)
    b = time.clock()
    print "Total time for Back Propagation Trainning ", b - a
    print
    print "Writing Network to file NN.dat"
    n.SaveW("NN.dat")  # Save Weigths to file
    del n
    n = NN(2, 3, 1)
    print "Load network from file NN.dat"
    n.LoadW("NN.dat")  # Load Weigths from file
    n.test(pat)
    del n

    # create a network with two input, two hidden, and one output nodes
    a = time.clock()
    n = NN(2, 3, 1)
    #train it with some patterns
    print "Starting single step training"
    for i in xrange(1000):
            error = 0.0
            for p in pat:
                inputs = p[0]
                targets = p[1]
                error = error + n.singletrain(inputs, targets)
            if i % 100 == 0 and i != 0:
                print 'error ' + str(error)
    # test it
    n.test(pat)
    b = time.clock()
    print "Total time for Back Propagation Trainning ", b - a
    print
    print "Writing Network to file NN.dat"
    n.SaveW("NN.dat")  # Save Weigths to file
    del n
    n = NN(2, 3, 1)
    print "Load network from file NN.dat"
    n.LoadW("NN.dat")  # Load Weigths from file
    n.test(pat)
    del n

if __name__ == "__main__":
#     p = PerceptronAlg(threshold=0.5)
# 
#     training_data = [([0, 0, 1], 0),
#                      ([0, 1, 1], 1),
#                      ([1, 0, 1], 1),
#                      ([1, 1, 1], 1)]
# 
#     input_size = len(training_data[0][0])
# 
#     p.train(training_data, input_size, max_cycles=1000)
# 
#     for input_vector, _ in training_data:
#         print p.classify_vector(input_vector)
# 
#     # test the adaline algorithm
#     p = AdalineAlg(threshold=0.5)
#  
#     training_data = [([-1, 0, 0], -.5),
#                      ([-1, 0, 1], -.5),
#                      ([-1, 1, 0], -.5),
#                      ([-1, 1, 1], .5)]
#  
#     input_size = len(training_data[0][0])
#  
#     p.train(training_data, input_size, desired_error=0.9, max_cycles=1000)
#  
#     for input_vector, _ in training_data:
#         print p.classify_vector(input_vector)
#     plt.show()
#     print "end of script"


    demo()