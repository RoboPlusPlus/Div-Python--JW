import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QLayoutItem, QHBoxLayout, QLayout)
from PyQt5.QtCore import pyqtSlot


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #Oppsett MainWindow

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('MGL Tool')

        # Laster inn objekter
        # Lables
        label_object_list_loaded = QLabel('Ingen Master objektliste lastet inn')
        label_mgl_loaded = QLabel('Ingen Master Genereringsliste lastet inn')
        label_objects_loaded = QLabel('<b>Innlastede objekter</b>')
        label_log = QLabel('<b>Log</b>')

        # Buttons
        btn_load_object_list = QPushButton("Load Object list", self)
        btn_load_object_list.clicked.connect(self.btn_load_object_list_clicked)
        btn_load_object_list.resize(btn_load_object_list.sizeHint())

        btn_load_mgl = QPushButton("Load MGL", self)
        btn_load_mgl.resize(btn_load_mgl.sizeHint())
        btn_load_mgl.clicked.connect(self.btn_load_mgl_clicked)

        btn_exit = QPushButton("Exit", self)
        btn_exit.resize(btn_exit.sizeHint())
        btn_exit.clicked.connect(self.close)

        # Textboxes
        textbox_loaded_objects = QTextEdit()
        textbox_loaded_objects.setReadOnly(1)
        textbox_log = QTextEdit()
        textbox_log.setReadOnly(1)


        # layout setup
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.SetFixedSize = 20

        grid.SizeConstraint(grid.SetFixedSize)
        grid.SetFixedSize = 3

        grid.addWidget(btn_load_object_list, 0, 0)
        grid.addWidget(label_object_list_loaded, 0, 1)

        grid.addWidget(btn_load_mgl, 1, 0)
        grid.addWidget(label_mgl_loaded, 1, 1)

        grid.addWidget(label_objects_loaded, 3,0)
        grid.addWidget(textbox_loaded_objects, 4, 0, 4, 3)
        grid.addWidget(label_log, 3, 3)
        grid.addWidget(textbox_log, 4, 3, 4,7)
        grid.addWidget(btn_exit, 8, 8)

        for c in range(9):
            grid.setColumnMinimumWidth(c, 50)

        for r in range(5):
            grid.setRowMinimumHeight(r, 10)
        self.setLayout(grid)
        self.show()


    # Events
    @pyqtSlot()
    def btn_load_object_list_clicked(self):
        print("btn_load_object_list_clicked")

    @pyqtSlot()
    def btn_load_mgl_clicked(self):
        sender = self.sender()
        print("btn_load_mgl_clicked")



def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
