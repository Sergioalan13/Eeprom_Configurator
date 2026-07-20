# -----------------------------------------------------------------------------
#                           IMPORTS
# -----------------------------------------------------------------------------
from dataclasses import dataclass, field

# -----------------------------------------------------------------------------
#                           DATA CLASSES
# -----------------------------------------------------------------------------
@dataclass
class Memory:
    name: str = ""
    size: int = 0
    used: int = 0
    free: int = 0 

@dataclass
class Variable:
    name: str = ""
    type: str = ""
    elements: int = 1
    size: int = 0
    address: str = ""
    initValue: str = ""
    comment: str = ""

@dataclass
class Project:
    name: str = ""
    memory: Memory = field(default_factory=Memory)
    variables: list[Variable] = field(default_factory=list)