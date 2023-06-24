# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400,200)
        #DEfinimos la etiqueta y la linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #Conectar el widget de entrada_texto con la etiqueta
        # La señal es textChanged, el slot es setTExt
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        #Crear un contendor
        contenedor  = QWidget()
        contenedor.setLayout(disposicion)
        #Publicamosd el contenedor, el cual incluye los demas elementos
        self.setCentralWidget(contenedor)



if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
