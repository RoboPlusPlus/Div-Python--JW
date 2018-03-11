from PyQt5.QtWidgets import QPushButton

def select_mg_list_button(_self):
    btn = QPushButton('Velg Master genereringsliste', _self)
    btn.setToolTip('Trykk på denne for å velge MGL')
    btn.move(_self.width - 400, 50)
    btn.clicked.connect(_self.select_mg_file)

def select_object_list_button(_self):
    btn = QPushButton('Velg objektliste', _self)
    btn.setToolTip('Trykk på denne for å velge objektliste')
    btn.move(_self.width -100, 50)
    btn.clicked.connect(_self.select_object_file)
