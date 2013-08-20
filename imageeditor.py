'''
Created on Aug 19, 2013

@author: lrvillan
'''
import os
import sys
from PyQt4.QtGui import QWidget, QApplication
from ui_imageeditor import Ui_ImageEditor


class ImageEditor(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_ImageEditor()
        self.ui.setupUi(self)
        self.clear_all()

    def clear_all(self):
        self.ui.widget_iconeditor.newCleanImage(size=(16, 16))
        self.ui.lineEditFilename.setText("image")
        self.update_counter(0)

    def update_counter(self, value):
        self.counter = value
        self.ui.lineEditCurrentNum.setText(str(value))

    def on_pbtnSave_pressed(self):
        # get file options
        filename = str(self.ui.lineEditFilename.text())
        number, _ = self.ui.lineEditCurrentNum.text().toInt()
        filename = "%s-%d.png" % (filename, number)

        # current path
        cur_path = os.path.dirname(os.path.abspath(__file__))

        # build the file name
        filename = os.path.join(cur_path, filename)

        # takes the image data and save to file
        self.ui.widget_iconeditor.saveToFile(filename)
        output_text = "Imaged saves as %s" % filename
        self.ui.plainTextEditLog.appendPlainText(output_text)

        self.update_counter(self.counter + 1)

    def on_pbtnClear_pressed(self):
        self.clear_all()
    
    def on_pbtnRestartNumbering_pressed(self):
        self.update_counter(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = ImageEditor()
    myapp.show()
    sys.exit(app.exec_())
