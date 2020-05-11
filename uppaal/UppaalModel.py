from .Template import Template
from .Declaration import Declaration
from .Declaration import SystemDeclaration


class UppaalModel(object):
    def __init__(self):
        self.global_declarations = Declaration()
        self.templates = []
        self.system_declarations = SystemDeclaration()
        return
