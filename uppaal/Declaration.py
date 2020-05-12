from .DataType import DataType
import xml.dom.minidom as dom
from .Constant import *


class _VariableDec(object):
    def __init__(self, type: int, name: str, value: str == ''):
        '''
        :param type: the data type of the declaration
        :param name: the name of the variable
        :param value: the value of the variable if it exists
        '''
        self.type = type
        self.name = name

        # assign the variable 'is_assigned' and 'value' according to the param 'value'
        if value:
            self.is_assigned = True
            self.value = value
        else:
            self.is_assigned = False
            self.value = ''
        return

    def __str__(self):
        '''
        :return: the declaration string
        '''

        if self.is_assigned:
            return ASSIGNED_VARIABLE_DECLARATION.format(DataType.type2str(self.type), self.name, self.value)
        else:
            return UNASSIGNED_VARIABLE_DECLARATION.format(DataType.type2str(self.type), self.name)

    def set_type(self, type: int):
        self.type = type
        return

    def set_name(self, name: str):
        self.name = name
        return

    def set_value(self, value: str):
        self.value = value
        if value:
            if not self.is_assigned:
                self.is_assigned = True
        else:
            self.is_assigned = False
        return


class _FunctionDec(object):
    def __init__(self, type: int, name: str, param: str, code: str):
        self.type = type
        self.name = name
        self.param = param
        self.code = code
        return

    def __str__(self):
        return FUNCTION_DECLARATION.format(DataType.type2str(self.type), self.name, self.param, self.code)

    def set_type(self, type: int):
        self.type = type
        return

    def set_name(self, name: str):
        self.name = name
        return

    def set_param(self, param: str):
        self.param = param
        return

    def set_code(self, code: str):
        self.code = code
        return


class Declaration(object):
    def __init__(self):
        self.variable_declarations = []
        self.function_declarations = []
        return

    def add_variable(self, type: int, name: str, value: str):
        declaration = _VariableDec(type, name, value)
        self.variable_declarations.append(declaration)
        return declaration

    def add_function(self, type: int, name: str, param: str, code: str):
        declaration = _FunctionDec(type, name, param, code)
        self.function_declarations.append(declaration)
        return declaration

    def __str__(self):
        declaration = '\n'
        for variable_declaration in self.variable_declarations:
            declaration += variable_declaration.__str__() + '\n'

        declaration += '\n\n'
        for function_declaration in self.function_declarations:
            declaration += function_declaration.__str__() + '\n'

        return declaration

    def writer(self, doc: dom.Document):
        # doc=dom.Document()
        node = doc.createElement("declaration")
        node.appendChild(doc.createTextNode(str(self)))
        # doc.appendChild(node)
        return node


class SystemDeclaration(object):
    def __init__(self):
        self.processes = []
        return

    def add_process(self, name: str):
        '''
        add a process to the system declaration
        :param name: the process name
        :return:
        '''
        self.processes.append(name)
        return

    def __str__(self):
        system_declaration = '\n'
        system_composed = 'system '
        for i, process in enumerate(self.processes):
            system_declaration += SYSTEM_DECLARATION.format(str(i), process) + '\n'
            system_composed += 'Process' + str(i) + ','
        system_composed = system_composed[:-1] + ';'
        return system_declaration + '\n\n' + system_composed + '\n'

    def writer(self, doc: dom.Document):
        # doc=dom.Document()
        node = doc.createElement("system")
        node.appendChild(doc.createTextNode(str(self)))
        # doc.appendChild(node)
        return node
