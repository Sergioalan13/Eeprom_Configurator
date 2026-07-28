# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtGui import QIntValidator
from PyCode.main_window import Ui_MainWindow
from PyCode.Project_data_classes import Project, Variable
from Generators.GenerateXmlFiles import xmlGenerator
from PyCode.Eeprom_parameters_dialog import Ui_Dialog as Eeprom_parameters_dialog
from PyCode.Variable_configuration_dialog import Ui_Dialog as Variable_configuration_dialog

# -----------------------------------------------------------------------------
#                                VARIABLES
# -----------------------------------------------------------------------------
#EEPROM_SIZES = {"Kbit": Bytes}
EEPROM_SIZES = {
    "1 kBit": 128,
    "2 kBit": 256,
    "4 kBit": 512,
    "8 kBit": 1024,
    "16 kBit": 2048,
    "32 kBit": 4096,
    "64 kBit": 8192,
    "128 kBit": 16384,
    "256 kBit": 32768,
    "512 kBit": 65536,
    "1024 kBit": 131072,
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
    "Id": 0,
    "Name": 1,
    "Type": 2,
    "Elements" : 3,
    "Size" : 4,
    "Address": 5,
    "Init Value": 6,
    "Comment": 7
}

DEFAULT_VARIABLE_INIT_VALUE = 0

ELEMENTS_OF_SIMPLE_VARIABLE = 1

INIT_MEMORY_USED = 0
INIT_MEMORY_FREE = 100

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

        self.currentProject = Project()
        self.projectVariable = Variable()
        self.projectGenerator = xmlGenerator()

        self.memoryUsed = 0

        # -----------------------------------------------------------------------------
        #                           TABLE COLUM SIZES CONFIGURATION
        # -----------------------------------------------------------------------------
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Id"], 50)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Name"], 160)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Type"], 80)
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Elements"], 60)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Size"], 50)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Address"], 100)  
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Init Value"], 80)   
        self.ui.VariablesTableWidget.setColumnWidth(TABLE_ELEMENTS_INDEX["Comment"], 390)  

        # -----------------------------------------------------------------------------
        #                              CONNECT BUTTONS
        # -----------------------------------------------------------------------------
        # Configure eeprom parameters button
        self.ui.actionEeprom.triggered.connect(self.configEepromParameters)

         # Configure add an element button
        self.ui.actionAdd_new_element.triggered.connect(self.configVariableParameters)
        self.ui.AddElementpushButton.clicked.connect(self.configVariableParameters)
        self.ui.actionGenerate_xml_file.triggered.connect(self.generateXmlProjectFile)
        self.ui.actionOpenFile.triggered.connect(self.loadXmlProjectFile)
        self.ui.actionDelete_an_element.triggered.connect(self.deleteAnElement)
        self.ui.actionDelete_all.triggered.connect(self.deleteAllVariables)
        self.ui.DeleteElementpushButton.clicked.connect(self.deleteAnElement)
        self.ui.DeleteAllpushButton.clicked.connect(self.deleteAllVariables)


    # -----------------------------------------------------------------------------
    #                    EEPROM PARAMETERS CONFIGURATION DIALOG
    # -----------------------------------------------------------------------------
    def configEepromParameters(self):
        dialog = EepromParametersDialog()

        if dialog.exec():
            self.currentProject.memory.name = dialog.ui.EepromNameLineTextEdit.text()
            self.currentProject.memory.size = dialog.ui.EepromSizeComboBox.currentText()
            self.currentProject.memory.startAddress = dialog.ui.EepromStartAddressLineTextEdit.text()
            self.currentProject.memory.noPages = dialog.ui.EepromNoPagesLineTextEdit.text()
            self.currentProject.memory.pageSize = dialog.ui.EepromPageSizeLineTextEdit.text()
            self.currentProject.memory.i2cAddress = dialog.ui.EepromI2cAddressLineTextEdit.text()
            self.currentProject.memory.used = INIT_MEMORY_USED
            self.currentProject.memory.free = INIT_MEMORY_FREE

            self.projectGenerator.configMemory(self.currentProject.memory)

            self.ui.EepromName.setText('[' + self.currentProject.memory.name + ']')
            self.ui.EepromSize.setText(self.currentProject.memory.size)
            self.ui.EepromSize_Used.setText(str(INIT_MEMORY_USED) + '%')
            self.ui.EepromSize_Free.setText(str(INIT_MEMORY_FREE) + '%')


    # -----------------------------------------------------------------------------
    #                       VARIABLES PARAMETERS CONFIGURATION DIALOG
    # -----------------------------------------------------------------------------
    def configVariableParameters(self):
        dialog = VariableParametersDialog()

        if dialog.exec():
            self.projectVariable = Variable()
            self.projectVariable.type = dialog.ui.VariableTypeComboBox.currentText()
            self.projectVariable.elements = ELEMENTS_OF_SIMPLE_VARIABLE
            self.projectVariable.size = VARIABLE_SIZES[self.projectVariable.type]
 
            self.writeInitValue = dialog.ui.WriteVariableCheckBox.isChecked()
            if (False == self.writeInitValue): 
                self.projectVariable.initValue = DEFAULT_VARIABLE_INIT_VALUE
            else: 
                self.projectVariable.initValue = dialog.ui.VariableInitValue.text()

            # -----------------------------------------------------------------------------
            #                   DISPLAY VARIABLES CONFIGURED IN THE TABLE
            # -----------------------------------------------------------------------------
            self.projectVariable.name = dialog.ui.VariableName.text()
            self.projectVariable.address = dialog.ui.VariableAddress.text()
            self.projectVariable.comment = dialog.ui.VariableComment.text()

            self.id = self.ui.VariablesTableWidget.rowCount()
            self.ui.VariablesTableWidget.insertRow(self.id)
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Id"], QTableWidgetItem(str(self.id)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Name"], QTableWidgetItem(self.projectVariable.name))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Type"], QTableWidgetItem(self.projectVariable.type))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Elements"], QTableWidgetItem(str(self.projectVariable.elements)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Size"], QTableWidgetItem(str(self.projectVariable.size)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Address"], QTableWidgetItem(self.projectVariable.address))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Init Value"], QTableWidgetItem(str(self.projectVariable.initValue)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Comment"], QTableWidgetItem(self.projectVariable.comment))

            self.memoryUsed += int(self.projectVariable.size)
            self.projectGenerator.addVariable(self.currentProject, self.projectVariable)

    # -----------------------------------------------------------------------------
    #                       DELETE A VARIABLE
    # -----------------------------------------------------------------------------
    def deleteAnElement(self):
        rowSelected = self.ui.VariablesTableWidget.currentRow()
        if rowSelected >= 0:
            self.ui.VariablesTableWidget.removeRow(rowSelected)
        self.projectGenerator.deteleAnElement(self.currentProject, rowSelected)

    # -----------------------------------------------------------------------------
    #                       DELETE ALL VARIABLES
    # -----------------------------------------------------------------------------
    def deleteAllVariables(self):
        self.projectGenerator.deteleAllVariables(self.currentProject)
        self.ui.VariablesTableWidget.clearContents()
        self.ui.VariablesTableWidget.setRowCount(0)

    # -----------------------------------------------------------------------------
    #                       GENERATE XML FILE PROJECT
    # -----------------------------------------------------------------------------
    def generateXmlProjectFile(self):
        self.memoryInBytes = EEPROM_SIZES[self.currentProject.memory.size]

        self.memoryUsed = 0
        for variable in self.currentProject.variables:
            self.memoryUsed += variable.size

        self.currentProject.memory.used = int((self.memoryUsed * 100) / self.memoryInBytes)
        self.currentProject.memory.free = 100 - self.currentProject.memory.used
        self.ui.MemoryUsage_progressBar.setValue(int(self.currentProject.memory.used))
        self.ui.EepromSize_Used.setText(str(self.currentProject.memory.used) + '%')
        self.ui.EepromSize_Free.setText(str(self.currentProject.memory.free) + '%')

        self.projectGenerator.updateMemory(self.currentProject.memory)

        self.projectGenerator.configVariables(self.currentProject.variables)

        self.projectGenerator.generateProject("Eeprom_Configurator.xml", "Eeprom_Configurator")

    # -----------------------------------------------------------------------------
    #                       LOAD XML FILE PROJECT
    # -----------------------------------------------------------------------------
    def loadXmlProjectFile(self):
        self.currentProject = self.projectGenerator.loadProject("Eeprom_Configurator.xml")
        self.memoryUsed = 0
        self.ui.VariablesTableWidget.setRowCount(0)

        self.ui.EepromName.setText('[' + self.currentProject.memory.name + ']')
        self.ui.EepromSize.setText(self.currentProject.memory.size)
        self.ui.EepromSize_Used.setText(str(self.currentProject.memory.used) + '%')
        self.ui.EepromSize_Free.setText(str(self.currentProject.memory.free) + '%')
        self.ui.MemoryUsage_progressBar.setValue(int(self.currentProject.memory.used))

        for variable in self.currentProject.variables:

            self.memoryUsed += variable.size

            self.id = self.ui.VariablesTableWidget.rowCount()
            self.ui.VariablesTableWidget.insertRow(self.id)
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Id"], QTableWidgetItem(str(self.id)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Name"], QTableWidgetItem(variable.name))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Type"], QTableWidgetItem(variable.type))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Elements"], QTableWidgetItem(str(variable.elements)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Size"], QTableWidgetItem(str(variable.size)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Address"], QTableWidgetItem(variable.address))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Init Value"], QTableWidgetItem(str(variable.initValue)))
            self.ui.VariablesTableWidget.setItem(self.id, TABLE_ELEMENTS_INDEX["Comment"], QTableWidgetItem(variable.comment))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

