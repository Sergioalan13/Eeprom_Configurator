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
        self.namesOk = True
        self.valuesOk = True
        self.memRangesOk = True
        self.noPageOverflow = True

        
    def validateVariableNames(self, project):
        nameStatus = True
        for variable in project.variables:
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*$", variable.name):
                self.errors.append(f'[Error]: "{variable.name}" is not a valid name')
                nameStatus = False

        return nameStatus

    def validateVariableValues(self, project):
        valuesStatus = True
        for variable in project.variables:
            min_val, max_val = VARIABLE_TYPE_RANGES[variable.type]
            if("float" == variable.type):
                value = float(variable.initValue)
            else:
                value = int(variable.initValue)

            if not (min_val <= value <= max_val):
                self.errors.append(f'[Error]: "{variable.name}" is out of value range')
                valuesStatus = False

        return valuesStatus

    def validateMemoryRanges(self, project):
        rangesStatus = True
        for i in range(len(project.variables)):

            variable1 = project.variables[i]
            endVar1 = int(variable1.address,16) + int(variable1.size) - 1

            for j in range(i + 1, len(project.variables)):

                variable2 = project.variables[j]
                endVar2 = int(variable2.address, 16) + int(variable2.size) - 1

                if not (endVar1 < int(variable2.address,16) or endVar2 < int(variable1.address,16)):
                    self.errors.append(f'[Error]: "{variable1.name}" is a memory overlap with "{variable2.name}"')
                    rangesStatus = False

        return rangesStatus

    def validatePageOverflow(self, project):
        pagesStatus = True
        pageSize = int(project.memory.pageSize)

        for variable in project.variables:

            varStartAddress = int(variable.address, 16)
            varEndAddress = varStartAddress + int(variable.size) - 1

            startPage = varStartAddress // pageSize
            endPage = varEndAddress // pageSize

            if startPage != endPage:

                self.errors.append(f'[Error]: "{variable.name}" crosses the page boundary (Page {startPage} -> Page {endPage})')
                pagesStatus = False

        return pagesStatus

    def validateProject(self, project):
        self.errors = []
        self.namesOk = self.validateVariableNames(project)
        self.valuesOk = self.validateVariableValues(project)
        self.memRangesOk = self.validateMemoryRanges(project)
        self.noPageOverflow = self.validatePageOverflow(project)

        if(self.namesOk and self.valuesOk and self.memRangesOk and self.noPageOverflow):
            self.projectStatus = VALIDATION_PROJECT_STATUS.VALIDATED
        else:
            self.projectStatus = VALIDATION_PROJECT_STATUS.NO_VALIDATED

        self.namesOk = True
        self.valuesOk = True
        self.memRangesOk = True
        self.noPageOverflow = True

        return self.projectStatus, self.errors
    
    def setProjectStatus(self, status):
        self.projectStatus = status

    def getProjectStatus(self):
        return self.projectStatus
