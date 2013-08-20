import sys
from PyQt4.QtGui import (QWidget, QImage, QSizePolicy, QPainter, QApplication,
                         QPalette, QColor)
from PyQt4.QtCore import Qt, QRect, QPoint, pyqtProperty, QSize, pyqtSignal
from PIL import Image
import numpy as np


class IconWidget(QWidget):
    QT_BLACK = Qt.color1
    QT_WHITE = Qt.color0
    updated = pyqtSignal()

    def __init__(self, parent=None, size=(8, 8), zoom=8):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.curColor = Qt.color0
        self.zoom = zoom
        self.size = QSize(*size)
        self.newCleanImage()

    def penColor(self):
        return self.curColor

    def setPenColor(self, penColor):
        self.curColor = penColor

    def newCleanImage(self, size=None):
        if size:
            self.size = QSize(*size)
        self.image = QImage(self.size, QImage.Format_Mono)
        self.clearIconImage()

    def iconImage(self):
        return self.image

    def setIconImage(self, new_image):
        if new_image != self.image:
            self.image = new_image
            self.update()
            self.updateGeometry()

    def clearIconImage(self):
        self.image.fill(1)
        self.update()
        self.updateGeometry()

    def zoomFactor(self):
        return self.zoom

    def setZoomFactor(self, zoomFactor):
        self.zoom = zoomFactor

    # Qt Designer attributes
    penColor = pyqtProperty("QColor", penColor, setPenColor)
    iconImage = pyqtProperty("QImage", iconImage, setIconImage)
    zoomFactor = pyqtProperty("int", zoomFactor, setZoomFactor)

    def sizeHint(self):
        size = self.zoom * self.image.size()
        if self.zoom >= 3:
            size += QSize(1, 1)
        return size

    def getIconData(self):
        width = self.image.width()
        height = self.image.height()

        matrix = list()
        for y in range(height):
            row = list()
            for x in range(width):
                opaque = 1 if QColor.fromRgba(
                        self.image.pixel(QPoint(x, y))).red() != 255 else 0
                row.append(opaque)
            matrix.append(row)
        return np.array(matrix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setImagePixel(event.pos(), True)
        elif event.button() == Qt.RightButton:
            self.setImagePixel(event.pos(), False)
        elif event.button() == Qt.MiddleButton:
#             self.image.fill(0)
            self.clearIconImage()

    def mouseReleaseEvent(self, event):
        self.updated.emit()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.setImagePixel(event.pos(), True)
        elif event.buttons() == Qt.RightButton:
            self.setImagePixel(event.pos(), False)
        elif event.buttons() == Qt.MiddleButton:
            self.clearIconImage()

    def setImagePixel(self, pos, opaque):
        i = pos.x() / self.zoom
        j = pos.y() / self.zoom

        if self.image.rect().contains(i, j):
            self.image.setPixel(i, j, 0)
            self.update(self.pixelRect(i, j))

    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        if self.zoom >= 3:
            self.painter.setPen(QPalette().foreground().color())

            # draw horizontal lines
            for i in range(self.image.width() + 1):
                self.painter.drawLine(self.zoom * i,
                                      0,
                                      self.zoom * i,
                                      self.zoom * self.image.height())

            # draw vertical lines
            for j in range(self.image.height() + 1):
                self.painter.drawLine(0,
                                      self.zoom * j,
                                      self.zoom * self.image.width(),
                                      self.zoom * j)

            for i in range(self.image.width()):
                for j in range(self.image.height()):
                    rect = self.pixelRect(i, j)
                    if not event.region().intersected(rect).isEmpty():
                        color = QColor.fromRgba(self.image.pixel(QPoint(i, j)))
                        if color.red() < 255:
                            self.painter.fillRect(rect, self.QT_WHITE)
                        self.painter.fillRect(rect, color)
        self.painter.end()

    def pixelRect(self, i, j):
        if self.zoom >= 3:
            return QRect(self.zoom * i + 1, self.zoom * j + 1,
                         self.zoom - 1, self.zoom - 1)
        else:
            return QRect(self.zoom * i, self.zoom * j,
                         self.zoom, self.zoom)

    def saveToFile(self, path):
        # FIXTHIS: saveToFile not working
        img_data = self.getIconData()
        img_string = img_data.tostring()
        size = (16, 16)  #FIX THIS PLEASE
#         img_data = np.uint8(img_data)
        print img_data
        im = Image.fromstring(mode="P", size=size, data=img_string)
        im.save(path)


def main():
    app = QApplication(sys.argv)
    window = IconWidget(size=(30, 30))
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
