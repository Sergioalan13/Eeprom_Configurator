# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
import xml.etree.ElementTree as ET
from PyCode.Project_data_classes import Variable, Memory, Project

# -----------------------------------------------------------------------------
#                           XML GENERATOR CLASS
# -----------------------------------------------------------------------------
class xmlGenerator:
    def __init__(self):
        self.treeName = "EepromConfigurator"
        self.root = ET.Element("EepromProject")
        self.projectName = ET.SubElement(self.root, "ProjectName")
        self.memory = ET.SubElement(self.root, "Memory")
        self.eepromVariables = ET.SubElement(self.root, "VariableStructures")

    def configMemory(self, memory):
        ET.SubElement(self.memory, "Name").text = str(memory.name)
        ET.SubElement(self.memory, "Size").text = str(memory.size)
        ET.SubElement(self.memory, "StartAddress").text = str(memory.startAddress)
        ET.SubElement(self.memory, "AddressSize").text = str(memory.addressSize)
        ET.SubElement(self.memory, "NoPages").text = str(memory.noPages)
        ET.SubElement(self.memory, "PageSize").text = str(memory.pageSize)
        ET.SubElement(self.memory, "I2cAddress").text = str(memory.i2cAddress)
        ET.SubElement(self.memory, "Used").text = str(memory.used)
        ET.SubElement(self.memory, "Free").text = str(memory.free)

    def updateMemory(self,memoryUpdated):
        memory = self.root.find("Memory")
        memory.find("Name").text = str(memoryUpdated.name)
        memory.find("Size").text = str(memoryUpdated.size)
        memory.find("StartAddress").text = str(memoryUpdated.startAddress)
        memory.find("AddressSize").text = str(memoryUpdated.addressSize)
        memory.find("NoPages").text = str(memoryUpdated.noPages)
        memory.find("PageSize").text = str(memoryUpdated.pageSize)
        memory.find("I2cAddress").text = str(memoryUpdated.i2cAddress)
        memory.find("Used").text = str(memoryUpdated.used)
        memory.find("Free").text = str(memoryUpdated.free)

    def addVariable(self, project, variable):
        project.variables.append(variable)

    def configVariables(self, listOfVariables):
        self.eepromVariables = self.root.find("VariableStructures")
        self.eepromVariables.clear()

        for variable in listOfVariables:
            self.variable = ET.SubElement(self.eepromVariables, "Variable")

            ET.SubElement(self.variable, "Id").text = str(variable.id)
            ET.SubElement(self.variable, "Name").text = str(variable.name)
            ET.SubElement(self.variable, "Type").text = str(variable.type)
            ET.SubElement(self.variable, "Elements").text = str(variable.elements)
            ET.SubElement(self.variable, "Size").text = str(variable.size)
            ET.SubElement(self.variable, "Address").text = str(variable.address)
            ET.SubElement(self.variable, "InitValue").text = str(variable.initValue)
            ET.SubElement(self.variable, "Comment").text = str(variable.comment)

    def deteleAllVariables(self, project):
        project.variables.clear()

    def deteleAnElement(self, project, indexElement):
        if indexElement >= 0:
            project.variables.pop(indexElement)

    def generateProject(self, fileName, projectName):
        self.projectName.text = projectName
        self.treeName = ET.ElementTree(self.root)
        ET.indent(self.treeName)
        self.treeName.write(fileName, encoding="utf-8", xml_declaration=True)
    
    def loadProject(self, file):
        self.treeName = ET.parse(file)
        self.root = self.treeName.getroot()
        variableDataClass = Variable()
        projectDataClass = Project()

        projectDataClass.name = self.root.find("ProjectName").text

        memory = self.root.find("Memory")
        projectDataClass.memory.name = memory.find("Name").text
        projectDataClass.memory.size = memory.find("Size").text
        projectDataClass.memory.startAddress = memory.find("StartAddress").text
        projectDataClass.memory.addressSize = memory.find("AddressSize").text
        projectDataClass.memory.noPages = memory.find("NoPages").text
        projectDataClass.memory.pageSize = memory.find("PageSize").text
        projectDataClass.memory.i2cAddress = memory.find("I2cAddress").text
        projectDataClass.memory.used = memory.find("Used").text
        projectDataClass.memory.free = memory.find("Free").text

        for VariableStructures in self.root.find("VariableStructures").findall("Variable"):
            variableDataClass = Variable()

            variableDataClass.id = VariableStructures.find("Id").text
            variableDataClass.name = VariableStructures.find("Name").text
            variableDataClass.type = VariableStructures.find("Type").text
            variableDataClass.elements = int(VariableStructures.find("Elements").text)
            variableDataClass.size = int(VariableStructures.find("Size").text)
            variableDataClass.address = VariableStructures.find("Address").text
            variableDataClass.initValue = VariableStructures.find("InitValue").text
            variableDataClass.comment = VariableStructures.find("Comment").text

            projectDataClass.variables.append(variableDataClass)

        return projectDataClass
