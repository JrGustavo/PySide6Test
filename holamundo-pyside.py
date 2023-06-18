import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de QT (PySide)
# SE encarga de procesar los eventos (event  loop)
app = QApplication()
# Crear un objeto ventana
# Cualquier componente puede ser una ventana en PySide
#ventana = QPushButton('boton PySide')
ventana = QMainWindow()
# Cambiar  el titulo
ventana.setWindowTitle('Hola Mundo con PySide')
#Modificiamos el tamaño de la ventana
ventana.resize(600, 600)
#Mostrar ventana
ventana.show()
# Se ejecuta la aplicacion
sys.exit(app.exec())