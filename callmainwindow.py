'''
Created on Jun 24, 2013

@author: lrvillan
'''

import sys
import os
import datetime
import logging

from mainwindowui import Ui_MainWindow
from PyQt4.QtGui import QApplication, QPixmap, QMainWindow, QWidget
from PyQt4.QtCore import Qt
from PIL import Image

from minimum_distance import distance_norm_1, distance_norm_2, distance_norm_p
from descriptors import (calculate_descriptor_1, calculate_descriptor_2,
                        calculate_descriptor_3)
from helper import convert_image_to_array
import PyQt4

#default icon editor size


# initialize logging
def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

script_name = os.path.basename(os.path.splitext(os.path.sys.argv[0])[0])+".log"
# script_name = timeStamped(script_name)
logging.basicConfig(filename=script_name,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s'
                    )
log = logging
LOGI = log.info
LOGW = log.warning
LOGE = log.error
LOGD = log.debug
LOGI("Starting Pattern Recognition script")


class CallMainWindow(QMainWindow):

    CLASS_IMAGES = "alpha.gif beta.png delta.png".split()
    DISTANCE_NORMS = {
        "Norm 1": distance_norm_1,
        "Norm 2": distance_norm_2,
        "Norm P": distance_norm_p
        }

    DESCRIPTOR_CALCULATORS = {
        "Descriptor 1": calculate_descriptor_1,
        "Descriptor 2": calculate_descriptor_2,
        "Descriptor 3": calculate_descriptor_3
        }
    ICON_EDITOR_SIZE = (16, 16)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_all_tabs()

        #initialize icon editor widget
        self.ui.widget_iconeditor.newCleanImage(size=self.ICON_EDITOR_SIZE)
        self.initialize_radio_buttons_events()

    def initialize_radio_buttons_events(self):
        # trap events from descriptor radio buttons
        for rb in self.ui.groupBox_descriptor.children():
            rb.toggled.connect(self.calculate_classes)
        # trap events from distance radio buttons
        for rb in self.ui.groupBox_distance.children():
            rb.toggled.connect(self.calculate_classes)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_P:
            LOGD("hey you press the P key :D")

    def appendToLogWindow(self, text):
        logWindow = self.ui.plainTextEdit
        logWindow.setText(logWindow.getText() + "\n" + text)

    def process_image(self, img_array,
                      descriptor_func=None,
                      distance_func=None,
                      class_name=None):
        """
        process the image data and returns a tuple containing the descriptor
        and the distance

        @param img_array:   the image data
        @param descriptor:  function that computes how are we going to describe
                            our image data
        @param distance:    selects the distance calculator among many
        @param class_name:  a name to use for DEBUG purposes
        """
        LOGI("Computing %s data" % (class_name))
        calculate_descriptor = descriptor_func

        descriptor_data = calculate_descriptor(img_array)
        LOGD("Descriptor Data:\n%s" % (str(descriptor_data)))
        distance_data = distance_func(descriptor_data)
        LOGD("Distance Data:\n%s" % (str(distance_data)))
        return (descriptor_data, distance_data)

    def array_to_string(self, array):
        pass

    def get_selected_distance_method(self):
        for rb in self.ui.groupBox_distance.children():
            if rb.isChecked():
                LOGD("distance=%s" % rb.text())
                return self.DISTANCE_NORMS[str(rb.text())]

    def get_selected_descriptor_method(self):
        for rb in self.ui.groupBox_descriptor.children():
            if rb.isChecked():
                LOGD("descriptor=%s" % rb.text())
                return self.DESCRIPTOR_CALCULATORS[str(rb.text())]

    def find_closest_distance(self):
        css_clear = """QLineEdit {
            background:;
        } """

        # highlight the closes match
        css_highlighted_bg = """QLineEdit {
            background-color: yellow;
        }"""

        icon_distance = self.ui.lineEdit_icon.text().toFloat()[0]
        closest_distance = 10000000   # initialize this to a largest value
        closest_lineEdit = None

        for lned in self.ui.tabMinDistance.findChildren(PyQt4.QtGui.QLineEdit):
            lned.setStyleSheet(css_clear)
            cur_distance = lned.text().toFloat()[0]
            distance_diff = abs(icon_distance - cur_distance)

            if distance_diff < closest_distance:
                closest_distance = distance_diff
                closest_lineEdit = lned

        closest_lineEdit.setStyleSheet(css_highlighted_bg)

    def on_pbtn_calculate_clicked(self):
        self.calculate_classes()

    def on_groupBox_descriptor_clicked(self, event):
        print "hello"

    def calculate_classes(self):
        LOGD("Update options classifier and distance methods")
        descriptor_func = self.get_selected_descriptor_method()
        distance_func = self.get_selected_distance_method()

        # calculate the first class
        LOGD("class alpha")
        img_array = convert_image_to_array(self.class1img)
        descriptor, distance = self.process_image(img_array,
                                                  descriptor_func,
                                                  distance_func,
                                                  "alpha"
                                                  )

        self.ui.textEdit_info1.setText(str(descriptor))
        self.ui.lineEdit_class1.setText(str(distance))

        # calculate the second class
        LOGD("class beta")
        img_array = convert_image_to_array(self.class2img)
        descriptor, distance = self.process_image(img_array,
                                                  descriptor_func,
                                                  distance_func,
                                                  "beta"
                                                  )

        self.ui.textEdit_info2.setText(str(descriptor))
        self.ui.lineEdit_class2.setText(str(distance))

        # calculate the third class
        LOGD("class gamma")
        img_array = convert_image_to_array(self.class3img)
        descriptor, distance = self.process_image(img_array,
                                                  descriptor_func,
                                                  distance_func,
                                                  "gamma"
                                                  )

        self.ui.textEdit_info3.setText(str(descriptor))
        self.ui.lineEdit_class3.setText(str(distance))

        # calculate the Drew class
        LOGD("class drawing")
        img_array = self.ui.widget_iconeditor.getIconData()
        descriptor, distance = self.process_image(img_array,
                                                  descriptor_func,
                                                  distance_func,
                                                  "Drawing"
                                                  )

        self.ui.textEdit_info4.setText(str(descriptor))
        self.ui.lineEdit_icon.setText(str(distance))

        # find closest match
        self.find_closest_distance()

    def on_widget_iconeditor_updated(self):
        self.calculate_classes()

    def init_all_tabs(self):
        self.init_minimum_distance()

    def compute_descriptors(self, class_data, descriptor_type):
        pass

    def init_minimum_distance(self):
        self.ui.label_desc1.setText("class alpha")
        self.ui.label_img1.setPixmap(QPixmap("alpha.png"))
        self.ui.label_img1.setScaledContents(True)
        self.ui.label_desc2.setText("class beta")
        self.ui.label_img2.setPixmap(QPixmap("beta.png"))
        self.ui.label_img2.setScaledContents(True)
        self.ui.label_desc3.setText("class delta")
        self.ui.label_img3.setPixmap(QPixmap("delta.png"))
        self.ui.label_img3.setScaledContents(True)

        self.class1img = Image.open("alpha.png")
        self.class2img = Image.open("beta.png")
        self.class3img = Image.open("delta.png")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = CallMainWindow()
    myapp.show()
    sys.exit(app.exec_())
