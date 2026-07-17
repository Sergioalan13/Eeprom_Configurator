# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtGui import QIntValidator
from main_window import Ui_MainWindow
from Eeprom_parameters_dialog import Ui_Dialog as Eeprom_parameters_dialog
from Variable_configuration_dialog import Ui_Dialog as Variable_configuration_dialog

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
#VARIABLE_SIZES = {VariableType : Size}
VARIABLE_SIZES = {
    "uint8_t": 1,
    "uint16_t": 2,
    "uint32_t": 4,
    "uint64_t": 8,
    "int8_t": 1,
    "int16_t": 2,
    "int32_t": 4,
    "int64_t": 8,
    "float": 4,
    "char": 1,
}

#TABLE_ELEMENTS_INDEX = {Column : Number}
TABLE_ELEMENTS_INDEX = {
    "Index": 0,
    "Name": 1,
    "Type": 2,
    "Elements" : 3,
    "Size" : 4,
    "Direction": 5,
    "Init Value": 6,
    "Comment": 7
}

DEFAULT_VARIABLE_INIT_VALUE = 0

ELEMENTS_OF_SIMPLE_VARIABLE = 1

# -----------------------------------------------------------------------------
#                           DIALOGS
# -----------------------------------------------------------------------------
class EepromParametersDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Eeprom_parameters_dialog()
        self.ui.setupUi(self)

class VariableParametersDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Variable_configuration_dialog()
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
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Index"], 50)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Name"], 160)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Type"], 80)
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Elements"], 60)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Size"], 55)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Direction"], 100)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Init Value"], 80)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Comment"], 400)  

        # -----------------------------------------------------------------------------
        #                              CONNECT BUTTONS
        # -----------------------------------------------------------------------------
        # Configure eeprom parameters button
        self.ui.actionEeprom.triggered.connect(self.configEepromParameters)

         # Configure add an element button
        self.ui.actionAdd_new_element.triggered.connect(self.configVariableParameters)
        self.ui.AddElementpushButton.clicked.connect(self.configVariableParameters)

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

    # -----------------------------------------------------------------------------
    #                       VARIABLES PARAMETERS CONFIGURATION DIALOG
    # -----------------------------------------------------------------------------
    def configVariableParameters(self):
        dialog = VariableParametersDialog()

        if dialog.exec():
            self.variableType = dialog.ui.VariableTypeComboBox.currentText()

            self.isArray = dialog.ui.ArrayCheckBox.isChecked()
            if (False == self.isArray): 
                self.VariableElements = ELEMENTS_OF_SIMPLE_VARIABLE
                self.VariableTotalSize = VARIABLE_SIZES[self.variableType]
            else: 
                self.VariableElements = int(dialog.ui.VariableElements.text())
                self.VariableTotalSize = VARIABLE_SIZES[self.variableType] * self.VariableElements
 
            self.isWriteVariable = dialog.ui.WriteVariableCheckBox.isChecked()
            if (False == self.isWriteVariable): 
                self.variableInitValue = DEFAULT_VARIABLE_INIT_VALUE
            else: 
                self.variableInitValue = dialog.ui.VariableInitValue.text()

            # -----------------------------------------------------------------------------
            #                   DISPLAY VARIABLES CONFIGURED IN THE TABLE
            # -----------------------------------------------------------------------------
            self.variableName = dialog.ui.VariableName.text()
            self.variableDirection = dialog.ui.VariableDirection.text()
            self.variableComment = dialog.ui.VariableComment.text()

            self.index = self.ui.VariablesTableWidget.rowCount()
            self.ui.VariablesTableWidget.insertRow(self.index)
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Index"], QTableWidgetItem(str(self.index)))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Name"], QTableWidgetItem(self.variableName))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Type"], QTableWidgetItem(self.variableType))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Elements"], QTableWidgetItem(str(self.VariableElements)))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Size"], QTableWidgetItem(str(self.VariableTotalSize)))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Direction"], QTableWidgetItem(self.variableDirection))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Init Value"], QTableWidgetItem(str(self.variableInitValue)))
            self.ui.VariablesTableWidget.setItem(self.index, TABLE_ELEMENTS_INDEX["Comment"], QTableWidgetItem(self.variableComment))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

