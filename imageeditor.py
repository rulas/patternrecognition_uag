# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageeditor.ui'
#
# Created: Mon Aug 19 13:19:15 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(480, 640)
        self.widget_iconeditor = IconWidget(Form)
        self.widget_iconeditor.setGeometry(QtCore.QRect(30, 40, 240, 240))
        self.widget_iconeditor.setMinimumSize(QtCore.QSize(240, 240))
        self.widget_iconeditor.setObjectName(_fromUtf8("widget_iconeditor"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(31, 311, 92, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 311, 211, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(31, 340, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(31, 369, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 340, 211, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 369, 211, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 470, 321, 71))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 420, 318, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Image Filename", None))
        self.label_2.setText(_translate("Form", "Current number", None))
        self.label_3.setText(_translate("Form", "Next Filename", None))
        self.pushButton_2.setText(_translate("Form", "Save", None))
        self.pushButton_4.setText(_translate("Form", "Restart Numbering", None))
        self.pushButton.setText(_translate("Form", "Clear", None))

from iconwidget import IconWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

