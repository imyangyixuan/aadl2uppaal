from .Declaration import Declaration
from .Location import Location
from .Transition import Transition
import xml.dom.minidom as dom


class Template(object):
    def __init__(self, name: str):
        self.name = name
        self.param = ''
        self.argu=''
        self.initial_location = ''
        self.locations = []
        self.transitions = []
        self.declarations = Declaration()
        return

    def set_initial_location(self, id: int):
        self.initial_location = 'id' + str(id)
        return

    def add_location(self, name: str, id: int):
        location = Location(name, id)
        self.locations.append(location)
        return location

    def add_transition(self, source: int, target: int):
        transition = Transition(source, target)
        self.transitions.append(transition)
        return transition

    def add_variable_declaration(self, type: int, name: str, value: str):
        return self.declarations.add_variable(type, name, value)

    def add_function_declaration(self, type: int, name: str, param: str, code: str):
        return self.declarations.add_function(type, name, param, code)

    def add_param(self,param):
        self.param=param
        return

    def add_argu(self,argu):
        self.argu=argu
        return

    def writer(self, doc: dom.Document):
        node = doc.createElement('template')
        name = doc.createElement('name')
        name.appendChild(doc.createTextNode(self.name))
        node.appendChild(name)

        param = doc.createElement('parameter')
        param.appendChild(doc.createTextNode(self.param))
        node.appendChild(param)

        node.appendChild(self.declarations.writer(doc))

        for location in self.locations:
            node.appendChild(location.writer(doc))

        init = doc.createElement('init')
        init.setAttribute('ref', self.initial_location)
        node.appendChild(init)

        for transition in self.transitions:
            node.appendChild(transition.writer(doc))
        doc.appendChild(node)
        return node
