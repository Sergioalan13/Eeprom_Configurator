# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QIntValidator
from main_window import Ui_MainWindow
from Eeprom_parameters_dialog import Ui_Dialog

# -----------------------------------------------------------------------------
#                                VARIABLES
# -----------------------------------------------------------------------------
#EEPROM_SIZES = {"Kbit": Bytes}
EEPROM_SIZES = {
    "1 Kbit": 128,
    "2 Kbit": 256,
    "4 Kbit": 512,
    "8 Kbit": 1024,
    "16 Kbit": 2048,
    "32 Kbit": 4096,
    "64 Kbit": 8192,
    "128 Kbit": 16384,
    "256 Kbit": 32768,
    "512 Kbit": 65536,
}

# -----------------------------------------------------------------------------
#                           DIALOGS
# -----------------------------------------------------------------------------
class EepromParametersDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


# -----------------------------------------------------------------------------
#                           MAIN WINDOW TOOL
# -----------------------------------------------------------------------------
class MainWindow(QMainWindow):
    # -----------------------------------------------------------------------------
    #                           TOOL FUNCTIONALITIES
    # -----------------------------------------------------------------------------    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # -----------------------------------------------------------------------------
        #                           TABLE COLUM SIZES CONFIGURATION
        # -----------------------------------------------------------------------------
        self.ui.VariablesTableWidget.setColumnWidth(0, 50)   #Index
        self.ui.VariablesTableWidget.setColumnWidth(1, 200)  #Name
        self.ui.VariablesTableWidget.setColumnWidth(2, 80)   #Type
        self.ui.VariablesTableWidget.setColumnWidth(3, 100)  #Direction
        self.ui.VariablesTableWidget.setColumnWidth(4, 80)   #InitValue
        self.ui.VariablesTableWidget.setColumnWidth(5, 465)  #Comment

        # -----------------------------------------------------------------------------
        #                              CONNECT BUTTONS
        # -----------------------------------------------------------------------------
        # Configure eeprom parameters button
        self.ui.actionEeprom.triggered.connect(self.configEepromParameters)

    # -----------------------------------------------------------------------------
    #                    EEPROM PARAMETERS CONFIGURATION DIALOG
    # -----------------------------------------------------------------------------
    def configEepromParameters(self):
        self.initMemoryUsed = 0
        self.initMemoryFree = 100

        dialog = EepromParametersDialog()

        if dialog.exec():
            self.EepromName = dialog.ui.EepromNameLineTextEdit.text()
            self.EepromSize = dialog.ui.EepromSizeComboBox.currentText()

            self.ui.EepromName.setText('[' + self.EepromName + ']')
            self.ui.EepromSize.setText(self.EepromSize)
            self.ui.EepromSize_Used.setText(str(self.initMemoryUsed) + '%')
            self.ui.EepromSize_Free.setText(str(self.initMemoryFree) + '%')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

