# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageeditor.ui'
#
# Created: Tue Aug 20 01:03:24 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImageEditor(object):
    def setupUi(self, ImageEditor):
        ImageEditor.setObjectName(_fromUtf8("ImageEditor"))
        ImageEditor.resize(480, 640)
        self.widget_iconeditor = IconWidget(ImageEditor)
        self.widget_iconeditor.setGeometry(QtCore.QRect(30, 40, 240, 240))
        self.widget_iconeditor.setMinimumSize(QtCore.QSize(240, 240))
        self.widget_iconeditor.setObjectName(_fromUtf8("widget_iconeditor"))
        self.label = QtGui.QLabel(ImageEditor)
        self.label.setGeometry(QtCore.QRect(31, 311, 92, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditFilename = QtGui.QLineEdit(ImageEditor)
        self.lineEditFilename.setGeometry(QtCore.QRect(130, 311, 211, 22))
        self.lineEditFilename.setObjectName(_fromUtf8("lineEditFilename"))
        self.label_2 = QtGui.QLabel(ImageEditor)
        self.label_2.setGeometry(QtCore.QRect(31, 340, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ImageEditor)
        self.label_3.setGeometry(QtCore.QRect(31, 369, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditCurrentNum = QtGui.QLineEdit(ImageEditor)
        self.lineEditCurrentNum.setGeometry(QtCore.QRect(130, 340, 211, 22))
        self.lineEditCurrentNum.setObjectName(_fromUtf8("lineEditCurrentNum"))
        self.lineEditNextFile = QtGui.QLineEdit(ImageEditor)
        self.lineEditNextFile.setGeometry(QtCore.QRect(130, 369, 211, 22))
        self.lineEditNextFile.setReadOnly(True)
        self.lineEditNextFile.setObjectName(_fromUtf8("lineEditNextFile"))
        self.plainTextEditLog = QtGui.QPlainTextEdit(ImageEditor)
        self.plainTextEditLog.setGeometry(QtCore.QRect(30, 470, 321, 71))
        self.plainTextEditLog.setObjectName(_fromUtf8("plainTextEditLog"))
        self.layoutWidget = QtGui.QWidget(ImageEditor)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 420, 318, 30))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbtnSave = QtGui.QPushButton(self.layoutWidget)
        self.pbtnSave.setObjectName(_fromUtf8("pbtnSave"))
        self.horizontalLayout.addWidget(self.pbtnSave)
        self.pbtnRestartNumbering = QtGui.QPushButton(self.layoutWidget)
        self.pbtnRestartNumbering.setObjectName(_fromUtf8("pbtnRestartNumbering"))
        self.horizontalLayout.addWidget(self.pbtnRestartNumbering)
        self.pbtnClear = QtGui.QPushButton(self.layoutWidget)
        self.pbtnClear.setObjectName(_fromUtf8("pbtnClear"))
        self.horizontalLayout.addWidget(self.pbtnClear)

        self.retranslateUi(ImageEditor)
        QtCore.QMetaObject.connectSlotsByName(ImageEditor)

    def retranslateUi(self, ImageEditor):
        ImageEditor.setWindowTitle(_translate("ImageEditor", "Form", None))
        self.label.setText(_translate("ImageEditor", "Image Filename", None))
        self.label_2.setText(_translate("ImageEditor", "Current number", None))
        self.label_3.setText(_translate("ImageEditor", "Next Filename", None))
        self.pbtnSave.setText(_translate("ImageEditor", "Save", None))
        self.pbtnRestartNumbering.setText(_translate("ImageEditor", "Restart Numbering", None))
        self.pbtnClear.setText(_translate("ImageEditor", "Clear", None))

from iconwidget import IconWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageEditor = QtGui.QWidget()
    ui = Ui_ImageEditor()
    ui.setupUi(ImageEditor)
    ImageEditor.show()
    sys.exit(app.exec_())

