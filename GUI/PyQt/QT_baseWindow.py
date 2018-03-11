import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setGeometry(50, 50, 600, 400) #x, y start ovre venstre hjorne, deretter bredde og hoyde
window.setWindowTitle("Test")

window.show()

