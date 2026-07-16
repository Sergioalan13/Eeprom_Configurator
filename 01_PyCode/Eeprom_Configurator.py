from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Table colum sizes configuration
        self.ui.VariablesTableWidget.setColumnWidth(0, 50)   #Index
        self.ui.VariablesTableWidget.setColumnWidth(1, 200)  #Name
        self.ui.VariablesTableWidget.setColumnWidth(2, 80)   #Type
        self.ui.VariablesTableWidget.setColumnWidth(3, 100)  #Direction
        self.ui.VariablesTableWidget.setColumnWidth(4, 80)   #InitValue
        self.ui.VariablesTableWidget.setColumnWidth(5, 465)  #Comment

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

