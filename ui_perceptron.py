# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perceptron.ui'
#
# Created: Thu Aug 22 00:53:26 2013
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

class Ui_Perceptron(object):
    def setupUi(self, Perceptron):
        Perceptron.setObjectName(_fromUtf8("Perceptron"))
        Perceptron.resize(661, 560)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Perceptron.sizePolicy().hasHeightForWidth())
        Perceptron.setSizePolicy(sizePolicy)
        Perceptron.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_alphaset = QtGui.QGroupBox(Perceptron)
        self.groupBox_alphaset.setGeometry(QtCore.QRect(20, 20, 621, 91))
        self.groupBox_alphaset.setObjectName(_fromUtf8("groupBox_alphaset"))
        self.label_img_alpha1 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha1.setGeometry(QtCore.QRect(11, 21, 60, 60))
        self.label_img_alpha1.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha1.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha1.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha1.setMargin(0)
        self.label_img_alpha1.setObjectName(_fromUtf8("label_img_alpha1"))
        self.label_img_alpha2 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha2.setGeometry(QtCore.QRect(78, 21, 60, 60))
        self.label_img_alpha2.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha2.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha2.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha2.setMargin(0)
        self.label_img_alpha2.setObjectName(_fromUtf8("label_img_alpha2"))
        self.label_img_alpha3 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha3.setGeometry(QtCore.QRect(145, 21, 60, 60))
        self.label_img_alpha3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha3.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha3.setMargin(0)
        self.label_img_alpha3.setObjectName(_fromUtf8("label_img_alpha3"))
        self.label_img_alpha4 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha4.setGeometry(QtCore.QRect(212, 21, 60, 60))
        self.label_img_alpha4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha4.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha4.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha4.setMargin(0)
        self.label_img_alpha4.setObjectName(_fromUtf8("label_img_alpha4"))
        self.label_img_alpha5 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha5.setGeometry(QtCore.QRect(279, 21, 60, 60))
        self.label_img_alpha5.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha5.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha5.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha5.setMargin(0)
        self.label_img_alpha5.setObjectName(_fromUtf8("label_img_alpha5"))
        self.label_img_alpha6 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha6.setGeometry(QtCore.QRect(346, 21, 60, 60))
        self.label_img_alpha6.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha6.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha6.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha6.setMargin(0)
        self.label_img_alpha6.setObjectName(_fromUtf8("label_img_alpha6"))
        self.label_img_alpha7 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha7.setGeometry(QtCore.QRect(413, 21, 60, 60))
        self.label_img_alpha7.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha7.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha7.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha7.setMargin(0)
        self.label_img_alpha7.setObjectName(_fromUtf8("label_img_alpha7"))
        self.label_img_alpha8 = QtGui.QLabel(self.groupBox_alphaset)
        self.label_img_alpha8.setGeometry(QtCore.QRect(480, 21, 60, 60))
        self.label_img_alpha8.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_alpha8.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_alpha8.setFrameShape(QtGui.QFrame.Box)
        self.label_img_alpha8.setMargin(0)
        self.label_img_alpha8.setObjectName(_fromUtf8("label_img_alpha8"))
        self.groupBox_deltaset = QtGui.QGroupBox(Perceptron)
        self.groupBox_deltaset.setGeometry(QtCore.QRect(20, 110, 621, 91))
        self.groupBox_deltaset.setObjectName(_fromUtf8("groupBox_deltaset"))
        self.label_img_delta2 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta2.setGeometry(QtCore.QRect(78, 21, 60, 60))
        self.label_img_delta2.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta2.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta2.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta2.setMargin(0)
        self.label_img_delta2.setObjectName(_fromUtf8("label_img_delta2"))
        self.label_img_delta1 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta1.setGeometry(QtCore.QRect(11, 21, 60, 60))
        self.label_img_delta1.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta1.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta1.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta1.setMargin(0)
        self.label_img_delta1.setObjectName(_fromUtf8("label_img_delta1"))
        self.label_img_delta3 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta3.setGeometry(QtCore.QRect(145, 21, 60, 60))
        self.label_img_delta3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta3.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta3.setMargin(0)
        self.label_img_delta3.setObjectName(_fromUtf8("label_img_delta3"))
        self.label_img_delta4 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta4.setGeometry(QtCore.QRect(212, 21, 60, 60))
        self.label_img_delta4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta4.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta4.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta4.setMargin(0)
        self.label_img_delta4.setObjectName(_fromUtf8("label_img_delta4"))
        self.label_img_delta5 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta5.setGeometry(QtCore.QRect(279, 21, 60, 60))
        self.label_img_delta5.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta5.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta5.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta5.setMargin(0)
        self.label_img_delta5.setObjectName(_fromUtf8("label_img_delta5"))
        self.label_img_delta6 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta6.setGeometry(QtCore.QRect(346, 21, 60, 60))
        self.label_img_delta6.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta6.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta6.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta6.setMargin(0)
        self.label_img_delta6.setObjectName(_fromUtf8("label_img_delta6"))
        self.label_img_delta7 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta7.setGeometry(QtCore.QRect(413, 21, 60, 60))
        self.label_img_delta7.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta7.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta7.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta7.setMargin(0)
        self.label_img_delta7.setObjectName(_fromUtf8("label_img_delta7"))
        self.label_img_delta8 = QtGui.QLabel(self.groupBox_deltaset)
        self.label_img_delta8.setGeometry(QtCore.QRect(480, 21, 60, 60))
        self.label_img_delta8.setMinimumSize(QtCore.QSize(60, 60))
        self.label_img_delta8.setMaximumSize(QtCore.QSize(60, 60))
        self.label_img_delta8.setFrameShape(QtGui.QFrame.Box)
        self.label_img_delta8.setMargin(0)
        self.label_img_delta8.setObjectName(_fromUtf8("label_img_delta8"))
        self.groupBox = QtGui.QGroupBox(Perceptron)
        self.groupBox.setGeometry(QtCore.QRect(20, 210, 261, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditLearningRate = QtGui.QLineEdit(self.groupBox)
        self.lineEditLearningRate.setGeometry(QtCore.QRect(110, 30, 113, 22))
        self.lineEditLearningRate.setObjectName(_fromUtf8("lineEditLearningRate"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditThreshold = QtGui.QLineEdit(self.groupBox)
        self.lineEditThreshold.setGeometry(QtCore.QRect(110, 60, 113, 22))
        self.lineEditThreshold.setObjectName(_fromUtf8("lineEditThreshold"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditMaxEpochs = QtGui.QLineEdit(self.groupBox)
        self.lineEditMaxEpochs.setGeometry(QtCore.QRect(110, 90, 113, 22))
        self.lineEditMaxEpochs.setObjectName(_fromUtf8("lineEditMaxEpochs"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEditClassification = QtGui.QLineEdit(self.groupBox)
        self.lineEditClassification.setGeometry(QtCore.QRect(110, 120, 113, 22))
        self.lineEditClassification.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.lineEditClassification.setReadOnly(True)
        self.lineEditClassification.setObjectName(_fromUtf8("lineEditClassification"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEditNumWeights = QtGui.QLineEdit(self.groupBox)
        self.lineEditNumWeights.setGeometry(QtCore.QRect(110, 150, 113, 22))
        self.lineEditNumWeights.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.lineEditNumWeights.setReadOnly(True)
        self.lineEditNumWeights.setObjectName(_fromUtf8("lineEditNumWeights"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEditNumCycles = QtGui.QLineEdit(self.groupBox)
        self.lineEditNumCycles.setGeometry(QtCore.QRect(110, 210, 113, 22))
        self.lineEditNumCycles.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.lineEditNumCycles.setReadOnly(True)
        self.lineEditNumCycles.setObjectName(_fromUtf8("lineEditNumCycles"))
        self.lineEditNumWeightedSum = QtGui.QLineEdit(self.groupBox)
        self.lineEditNumWeightedSum.setGeometry(QtCore.QRect(110, 180, 113, 22))
        self.lineEditNumWeightedSum.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.lineEditNumWeightedSum.setReadOnly(True)
        self.lineEditNumWeightedSum.setObjectName(_fromUtf8("lineEditNumWeightedSum"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pbtnStartTraining = QtGui.QPushButton(Perceptron)
        self.pbtnStartTraining.setGeometry(QtCore.QRect(310, 330, 101, 41))
        self.pbtnStartTraining.setObjectName(_fromUtf8("pbtnStartTraining"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Perceptron)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 460, 631, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.groupBox_descriptor = QtGui.QGroupBox(Perceptron)
        self.groupBox_descriptor.setGeometry(QtCore.QRect(290, 210, 151, 111))
        self.groupBox_descriptor.setFlat(False)
        self.groupBox_descriptor.setCheckable(False)
        self.groupBox_descriptor.setObjectName(_fromUtf8("groupBox_descriptor"))
        self.radioButton_desc1 = QtGui.QRadioButton(self.groupBox_descriptor)
        self.radioButton_desc1.setGeometry(QtCore.QRect(11, 21, 96, 20))
        self.radioButton_desc1.setChecked(True)
        self.radioButton_desc1.setObjectName(_fromUtf8("radioButton_desc1"))
        self.radioButton_desc2 = QtGui.QRadioButton(self.groupBox_descriptor)
        self.radioButton_desc2.setGeometry(QtCore.QRect(11, 48, 96, 20))
        self.radioButton_desc2.setObjectName(_fromUtf8("radioButton_desc2"))
        self.radioButton_desc3 = QtGui.QRadioButton(self.groupBox_descriptor)
        self.radioButton_desc3.setGeometry(QtCore.QRect(11, 75, 96, 20))
        self.radioButton_desc3.setObjectName(_fromUtf8("radioButton_desc3"))
        self.pbtnClassifyImage = QtGui.QPushButton(Perceptron)
        self.pbtnClassifyImage.setGeometry(QtCore.QRect(310, 380, 101, 41))
        self.pbtnClassifyImage.setObjectName(_fromUtf8("pbtnClassifyImage"))
        self.widget_iconeditor = IconWidget(Perceptron)
        self.widget_iconeditor.setGeometry(QtCore.QRect(450, 220, 180, 180))
        self.widget_iconeditor.setMinimumSize(QtCore.QSize(180, 180))
        self.widget_iconeditor.setObjectName(_fromUtf8("widget_iconeditor"))

        self.retranslateUi(Perceptron)
        QtCore.QMetaObject.connectSlotsByName(Perceptron)

    def retranslateUi(self, Perceptron):
        Perceptron.setWindowTitle(_translate("Perceptron", "Form", None))
        self.groupBox_alphaset.setTitle(_translate("Perceptron", "Alpha training set", None))
        self.label_img_alpha1.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha2.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha3.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha4.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha5.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha6.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha7.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_alpha8.setText(_translate("Perceptron", "TextLabel", None))
        self.groupBox_deltaset.setTitle(_translate("Perceptron", "Delta training set", None))
        self.label_img_delta2.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta1.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta3.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta4.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta5.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta6.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta7.setText(_translate("Perceptron", "TextLabel", None))
        self.label_img_delta8.setText(_translate("Perceptron", "TextLabel", None))
        self.groupBox.setTitle(_translate("Perceptron", "Configuration", None))
        self.label.setText(_translate("Perceptron", "Learning Rate", None))
        self.label_2.setText(_translate("Perceptron", "Threshold", None))
        self.label_3.setText(_translate("Perceptron", "Max Epochs", None))
        self.label_4.setText(_translate("Perceptron", "Classified as", None))
        self.label_5.setText(_translate("Perceptron", "Num Weights", None))
        self.label_6.setText(_translate("Perceptron", "Weighted Sum", None))
        self.label_7.setText(_translate("Perceptron", "Cycles", None))
        self.pbtnStartTraining.setText(_translate("Perceptron", "&Start Training", None))
        self.groupBox_descriptor.setTitle(_translate("Perceptron", "Descriptor", None))
        self.radioButton_desc1.setText(_translate("Perceptron", "Descriptor 1", None))
        self.radioButton_desc2.setText(_translate("Perceptron", "Descriptor 2", None))
        self.radioButton_desc3.setText(_translate("Perceptron", "Descriptor 3", None))
        self.pbtnClassifyImage.setText(_translate("Perceptron", "&Classify Image", None))

from iconwidget import IconWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Perceptron = QtGui.QWidget()
    ui = Ui_Perceptron()
    ui.setupUi(Perceptron)
    Perceptron.show()
    sys.exit(app.exec_())

