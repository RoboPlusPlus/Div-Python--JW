
from PyQt5.QtWidgets import QFileDialog


def openFileNameDialog(_self, title="QFileDialog.getOpenFileName()"):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(_self, title, "", "All Files (*);;Excel files (*.xlsx)", options=options)
    if fileName:
        return fileName
    else:
        return "No filename"