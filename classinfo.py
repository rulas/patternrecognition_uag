# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classinfo.ui'
#
# Created: Fri Jun 28 01:42:53 2013
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

class Ui_ClassInfo(object):
    def setupUi(self, ClassInfo):
        ClassInfo.setObjectName(_fromUtf8("ClassInfo"))
        ClassInfo.resize(361, 156)
        self.label_name = QtGui.QLabel(ClassInfo)
        self.label_name.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_img = QtGui.QLabel(ClassInfo)
        self.label_img.setGeometry(QtCore.QRect(20, 50, 60, 60))
        self.label_img.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img.setFrameShape(QtGui.QFrame.Box)
        self.label_img.setMargin(0)
        self.label_img.setObjectName(_fromUtf8("label_img"))
        self.textEdit_descriptor = QtGui.QTextEdit(ClassInfo)
        self.textEdit_descriptor.setGeometry(QtCore.QRect(110, 50, 241, 87))
        self.textEdit_descriptor.setMinimumSize(QtCore.QSize(241, 87))
        self.textEdit_descriptor.setObjectName(_fromUtf8("textEdit_descriptor"))

        self.retranslateUi(ClassInfo)
        QtCore.QMetaObject.connectSlotsByName(ClassInfo)

    def retranslateUi(self, ClassInfo):
        ClassInfo.setWindowTitle(_translate("ClassInfo", "ClassInfo", None))
        self.label_name.setText(_translate("ClassInfo", "TextLabel", None))
        self.label_img.setText(_translate("ClassInfo", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ClassInfo = QtGui.QWidget()
    ui = Ui_ClassInfo()
    ui.setupUi(ClassInfo)
    ClassInfo.show()
    sys.exit(app.exec_())

