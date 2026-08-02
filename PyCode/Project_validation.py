import re

VARIABLE_TYPE_RANGES = {
    "uint8_t":  (0, 255),
    "uint16_t": (0, 65535),
    "uint32_t": (0, 4294967295),

    "int8_t":   (-128, 127),
    "int16_t":  (-32768, 32767),
    "int32_t":  (-2147483648, 2147483647),

    "float":  (-1000000.0, 1000000.0),
}

class VALIDATION_PROJECT_STATUS:
    VALIDATED = 0
    NO_VALIDATED = 1

class validation:
    def __init__(self):
        self.projectStatus = VALIDATION_PROJECT_STATUS.NO_VALIDATED
        self.variableNamesOk = True
        self.variableValuesOk = True
        self.variableMemRangesOk = True
        
    def validateVariableNames(self, project):
        for variable in project.variables:
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*$", variable.name):
                self.errors.append(f'[Error]: "{variable.name}" is not a valid name')
                self.variableNamesOk = False

        return self.variableNamesOk

    def validateVariableValues(self, project):
        for variable in project.variables:
            min_val, max_val = VARIABLE_TYPE_RANGES[variable.type]
            if("float" == variable.type):
                value = float(variable.initValue)
            else:
                value = int(variable.initValue)

            if not (min_val <= value <= max_val):
                self.errors.append(f'[Error]: "{variable.name}" is out of value range')
                self.variableValuesOk = False

        return self.variableValuesOk

    def validateMemoryRanges(self, project):
        for i in range(len(project.variables)):

            variable1 = project.variables[i]
            endVar1 = int(variable1.address,16) + int(variable1.size) - 1

            for j in range(i + 1, len(project.variables)):

                variable2 = project.variables[j]
                endVar2 = int(variable2.address, 16) + int(variable2.size) - 1

                if not (endVar1 < int(variable2.address,16) or endVar2 < int(variable1.address,16)):
                    self.errors.append(f'[Error]: "{variable1.name}" is a memory overlap with "{variable2.name}"')
                    self.variableMemRangesOk = False

        return self.variableMemRangesOk

    def validateProject(self, project):
        self.errors = []
        self.variableNamesOk = self.validateVariableNames(project)
        self.variableValuesOk = self.validateVariableValues(project)
        self.variableMemRangesOk = self.validateMemoryRanges(project)

        if(self.variableNamesOk and self.variableValuesOk and self.variableMemRangesOk):
            self.projectStatus = VALIDATION_PROJECT_STATUS.VALIDATED
        else:
            self.projectStatus = VALIDATION_PROJECT_STATUS.NO_VALIDATED

        self.variableNamesOk = True
        self.variableValuesOk = True
        self.variableMemRangesOk = True

        return self.projectStatus, self.errors
    
    def setProjectStatus(self, status):
        self.projectStatus = status

    def getProjectStatus(self):
        return self.projectStatus
