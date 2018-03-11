import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy, QListWidget
#import MACVendorLookupSniffer
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random


#################
#    Globals    #
#################

#Oppretter tuple med x-y grid for vinduet
grid= []
grid_row_hight = 25
grid_col_width = 25
grid_left_border_offset = 20
grid_top_border_offset = 70

for col in range(100):
    for row in range(100):
        x_pos = col*grid_row_hight + grid_top_border_offset
        y_pos = row*grid_col_width + grid_left_border_offset
        gridentry = [y_pos, x_pos]
        grid.append(gridentry)


#################
#   Classes     #
#################
class BaseWindow(QtWidgets.QMainWindow):
    """
    Base-klasse for vinduer
    Generell initialisering av vindu

    Bruk inheritance fra denne classen for å opprette vinduer.
    Har Statusbar, en "File" meny med "Exit"
    Funksjon for "Close application"
    Aventi-logo

    """
    def __init__(self):
        super(BaseWindow, self).__init__()
        self.setGeometry(50, 50, 800, 450)
        self.setWindowTitle("Window Title")
        self.setWindowIcon(QtGui.QIcon("Logo-aventi_bare_logo.png"))
        # self.setFixedSize(800, 450)

        #Actions
        exitAction = QtWidgets.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Leave the app")
        exitAction.triggered.connect(self.close_application)

        #Enabler statusbar og meny på den, med "File" og "Exit"
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(exitAction)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, "Exit",
                                                "Quit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


class HomeWindow(BaseWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.setWindowTitle("HomeWindow")
        self.setGeometry(50, 50, 1200, 675)
        # self.setFixedSize(1200, 675) #Hvis vinduet ikke skal være resizable
        #self.setWindowOpacity(0.5)


        #Actions
        toolbarExitAction = QtWidgets.QAction(QtGui.QIcon("Logo-aventi_bare_logo.png"), "Exit Application", self)
        toolbarExitAction.triggered.connect(self.close_application)

        #Toolbar
        self.toolBar = self.addToolBar("Exit")
        self.toolBar.addAction(toolbarExitAction)

        #Matplotlib canvas
        #m = PlotCanvas(self, width=5, height=4)
        #m.move(*grid[200])

        #Knapper
        self.quit_btn()
        #self.new_plot_btn(m)

        #Checkbox
        checkBox = QtWidgets.QCheckBox("Enlarge window", self)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.move(*grid[25])

        #Label
        self.label_horse()

        self.lw = myListWidget()
        self.lw.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lw.setViewMode(QtWidgets.QListView.ListMode)
        self.lw.setObjectName("listView")
        #self.lw.move(50, 70)
        self.lw.setGeometry(70, 70, 100, 100)
        #self.lw.


        #Ferdig __init__
        self.show()




    def quit_btn(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        #btn.resize(100, 30)
        #btn.move(20, 100)
        btn.move(*grid[2200])

    def new_plot_btn(self, canvas):
        btn = QtWidgets.QPushButton("Nytt plot", self)
        btn.clicked.connect(canvas.plot)
        #btn.resize(100, 30)
        #btn.move(20, 100)
        btn.move(*grid[2205])

    def label_horse(self):
        label = QtWidgets.QLabel("horse", self)
        label.move(*grid[2305])


    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:

            self.setGeometry(50, 50, 1600, 900)
        else:
            self.setGeometry(50, 50, 1200, 675)


class myListWidget(QListWidget):
    def __init__(self):
        super(myListWidget, self).__init__()
        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")
        self.addItem("Item 4")

        self.setWindowTitle('PyQT QListwidget Demo')
        self.itemClicked.connect(self.Clicked)


    def Clicked(self,item):
        QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())



class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(data, 'r-')
        ax.set_title('Vilkårlig graf')
        self.draw()

    def clear_canvas(self):
        ax.clear()



############################
#   Globale funksjoner     #
############################
def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = HomeWindow()
    sys.exit(app.exec_())


##############
#   Main     #
##############
if __name__ == '__main__':
    run()
