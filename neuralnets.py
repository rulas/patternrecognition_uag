'''
Created on Aug 20, 2013

@author: lrvillan
'''
import os
import sys
import glob

from PyQt4.QtGui import QWidget, QApplication, QPixmap
from PIL import Image
import numpy as np

from ui_perceptron import Ui_Perceptron
from neural_network import PerceptronAlg, AdalineAlg
from helper import convert_image_to_array
from descriptors import (flat_descriptor_1,
                         flat_descriptor_2,
                         flat_descriptor_3)


class Perceptron(QWidget):

    descriptors_methods = {
            "Descriptor 1": flat_descriptor_1,
            "Descriptor 2": flat_descriptor_2,
            "Descriptor 3": flat_descriptor_3}
    
    neuron_algorithms = {
            "Perceptron": PerceptronAlg,
            "Adaline": AdalineAlg}

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Perceptron()
        self.neuron = None
        self.ui.setupUi(self)
        self.initialize_widget()

    def set_neuron(self, neuron):
        self.NeuronAlg = neuron

    def initialize_group_boxes(self):

        # initialize neuron type radio buttons
        for child in self.ui.groupBox_neuron_type.children():
            child.pressed.connect(self.handle_neurontype_change)

        # initialize descriptor radio buttons
        for child in self.ui.groupBox_descriptor.children():
            child.pressed.connect(self.handle_descriptor_change)

    def handle_neurontype_change(self):
        """
            handles a change into the neuron type radio buttons
            and set the neuron class to the desired one
        """
        neuron_type = str(self.sender().text())
        print "neuron_type = %s" % neuron_type
        self.set_neuron(self.neuron_algorithms[neuron_type])
    
    def handle_descriptor_change(self):
        """
            handles a change into the descriptors radio buttons and
            set the descriptormethod to the one selected.
        """
        method = str(self.sender().text())
        print "descriptor method = %s" % method
        self.descriptor_method = self.descriptors_methods[method]
        self.ui.pbtnStartTraining.setEnabled(True)
        self.ui.pbtnClassifyImage.setEnabled(False)

    def initialize_widget(self):
        """
            initialize widgets to default values
        """

        ##########################################################
        # Initialize images data
        ##########################################################
        alpha_paths = glob.glob("./images/alpha[0-9].png")
        alpha_groupbox = self.ui.groupBox_alphaset
        self.alpha_data = self.initialize_images(alpha_paths, alpha_groupbox)

        delta_paths = glob.glob("./images/delta[0-9].png")
        delta_groupbox = self.ui.groupBox_deltaset
        self.delta_data = self.initialize_images(delta_paths, delta_groupbox)

        # default neuron configuration
        self.set_learning_rate(0.1)
        self.set_max_epochs(1000)
        self.set_threshold(0.0)

        # the image editor
        self.ICON_EDITOR_SIZE = (16, 16)
        self.ui.widget_iconeditor.newCleanImage(size=self.ICON_EDITOR_SIZE)

        # disable classify image button until neuron has been trained
        self.ui.pbtnClassifyImage.setEnabled(False)

        # connect descriptor radio buttons to appropiate slot 
        self.initialize_group_boxes()

        # force a click on these to handle events
        self.ui.radioButton_desc1.click()
        self.ui.radioButtonPerceptron.click()

    def initialize_images(self, paths, groupbox=None):
        """
            Load images into the GUI and returns a tuple containing
            paths, images and widgets associated to images.
            :param paths(list): list of paths to images
            :param groupbox(QGroupBox): the groupbox that contains image placeholders
            :return: list of tuples containing paths, images, widgets
        """
        # open images
        images = []
        for path in paths:
            images.append(Image.open(path))

        # Find all image placeholders
        widgets = []
        for lbl in groupbox.children():
            widgets.append(lbl)

        img_data = zip(paths, images, widgets)

        for path, _, widget in img_data:
            widget.setPixmap(QPixmap(path))
            widget.setScaledContents(True)
        return img_data

    def get_learning_rate(self):
        return self.ui.lineEditLearningRate.text().toFloat()[0]

    def set_learning_rate(self, learning_rate):
        self.learning_rate = learning_rate
        self.ui.lineEditLearningRate.setText(str(self.learning_rate))

    def get_threshold(self):
        return self.ui.lineEditThreshold.text().toFloat()[0]

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.ui.lineEditThreshold.setText(str(self.threshold))

    def get_max_epochs(self):
        return self.ui.lineEditMaxEpochs.text().toInt()[0]

    def set_max_epochs(self, max_epochs):
        self.max_epochs = max_epochs
        self.ui.lineEditMaxEpochs.setText(str(self.max_epochs))

    def train(self):
        threshold = self.get_threshold()
        learning_rate = self.get_learning_rate()
        max_cycles = self.get_max_epochs()

        self.neuron = self.NeuronAlg(learning_rate, threshold)

        training_set = []
        vector_size = 0
        for _, image, _ in self.alpha_data:
            descriptor = self.descriptor_method(convert_image_to_array(image))
            descriptor = np.insert(descriptor, 0, 1)
            vector_size = len(descriptor)
            training_set.append((descriptor, 0))

        for _, image, _ in self.delta_data:
            descriptor = self.descriptor_method(convert_image_to_array(image))
            descriptor = np.insert(descriptor, 0, 1)
            training_set.append((descriptor, 1))

        self.neuron.train(training_set, vector_size, max_cycles)

    def obtain_draw_image_descriptor(self):
        """
            obtains the image from the image editor and 
            returns the descriptor of that image based
            on the selected descriptor.
        """
        img_array = self.ui.widget_iconeditor.getIconData()
        descriptor = self.descriptor_method(img_array)
        descriptor = np.insert(descriptor, 0, 1)
        return descriptor

    def classify_image(self):
        # obtain draw image data
        descriptor = self.obtain_draw_image_descriptor()
        print descriptor
        weighted_sum, classification = self.neuron.classify_vector(descriptor)
        self.ui.lineEditNumCycles.setText(str(self.neuron.get_num_cycles()))
        self.ui.lineEditNumWeights.setText(str(self.neuron.get_num_weights()))
        self.ui.lineEditNumWeightedSum.setText(str(weighted_sum))

        classification = "alpha" if classification == 0 else "delta"
        self.ui.lineEditClassification.setText(classification)

    def on_pbtnStartTraining_pressed(self):
        self.train()
        self.ui.pbtnStartTraining.setEnabled(False)
        self.ui.pbtnClassifyImage.setEnabled(True)

    def on_pbtnClassifyImage_pressed(self):
        self.classify_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Perceptron()
    myapp.show()
    sys.exit(app.exec_())