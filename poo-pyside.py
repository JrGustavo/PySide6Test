import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication


class VentanaPySide(QMainWindow):
   def __init__(self):
       #Llamamos el metodo init de la clase padre
       super().__init__()
       self.setWindowTitle('POO con Pyside')
       #self.resize(600, 400)
       # Colocamos los valores de ancho y alto de manera fija
       self.setFixedSize(QSize(600, 400))
       #Creamos algunos componentes
       self._agregar_componentes()
   def _agregar_componentes(self):
       #Agregramos un menu
       menu = self.menuBar()
       menu_archivo = menu.addMenu('Archivo')
       # Agregamos algunas opciones al melnu
       accion_nuevo = QAction('Nuevo', self)
       menu_archivo.addAction(accion_nuevo)


if __name__ == '__main__':
    app = QApplication([])
    #Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    #Ejecutamos la ventana
    sys.exit(app.exec())