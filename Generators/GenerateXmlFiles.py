# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
import xml.etree.ElementTree as ET
from PyCode.projectDataClasses import Variable, Project

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

    def configMemory(self, name, size):
        ET.SubElement(self.memory, "Name").text = name
        ET.SubElement(self.memory, "Size").text = size

    def configVariable(self, variable):
        self.variable = ET.SubElement(self.eepromVariables, "Variable")

        ET.SubElement(self.variable, "Name").text = variable.name
        ET.SubElement(self.variable, "Type").text = variable.type
        ET.SubElement(self.variable, "Elements").text = str(variable.elements)
        ET.SubElement(self.variable, "Size").text = str(variable.size)
        ET.SubElement(self.variable, "Address").text = variable.address
        ET.SubElement(self.variable, "InitValue").text = variable.initValue
        ET.SubElement(self.variable, "Comment").text = variable.comment

    def saveProject(self, fileName, projectName):
        self.projectName.text = projectName
        tree = ET.ElementTree(self.root)
        ET.indent(tree)
        tree.write(fileName, encoding="utf-8", xml_declaration=True)
    
    def loadProject(self, fileName):
        tree = ET.parse(fileName)
        root = tree.getroot()
        variableDataClass = Variable()
        projectDataClass = Project()

        projectDataClass.name = root.find("ProjectName").text

        memory = root.find("Memory")
        projectDataClass.memory.name = memory.find("Name").text
        projectDataClass.memory.size = memory.find("Size").text

        for VariableStructures in root.find("VariableStructures").findall("Variable"):
            variableDataClass.name = VariableStructures.find("Name").text
            variableDataClass.type = VariableStructures.find("Type").text
            variableDataClass.elements = int(VariableStructures.find("Elements").text)
            variableDataClass.size = int(VariableStructures.find("Size").text)
            variableDataClass.address = VariableStructures.find("Address").text
            variableDataClass.initValue = VariableStructures.find("InitValue").text
            variableDataClass.comment = VariableStructures.find("Comment").text

            projectDataClass.variables.append(variableDataClass)

        return projectDataClass
