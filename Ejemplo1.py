import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel,
                               QPushButton, QVBoxLayout, QWidget)

from PySide2.QtCore import Slot, Qt


class Aplicacion(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.saudo = ["Hola", "Ola", "Hello", "Alo", "Salut", "Arigatou", "Ciao"]
        boton = QPushButton("Púlsame")
        self.etiqueta = QLabel("Hola a todos")
        self.etiqueta.setAlignment(Qt.AlignCenter)
        caixaV = QVBoxLayout()
        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(boton)

        self.setLayout(caixaV)

        boton.clicked.connect(self.on_boton_clicked)

        self.resize(400, 300)
        self.show()

    def on_boton_clicked(self):
        self.etiqueta.setText(random.choice(self.saudo))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicacion = Aplicacion()
    # PODRÍAMOS PONER ESTAS FUNCIONES AQUÍ, AL ESTAR FUERA DE LA FUNCIÓN PRINCIPAL HABRÍA QUE LLAMARLA CON "aplicacion", NO CON "self" !!!
    # aplicacion.resize(400, 300)
    # aplicacion.show()
    sys.exit(app.exec_())
