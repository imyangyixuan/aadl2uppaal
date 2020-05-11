from .Template import Template
from .Declaration import Declaration
from .Declaration import SystemDeclaration
from .Location import Location
from .Transition import Transition
from .Query import Query
import xml.dom.minidom as dom


class UppaalModel(object):
    def __init__(self):
        self.global_declarations = Declaration()
        self.templates = []
        self.system_declarations = SystemDeclaration()
        self.queries=Query()
        return

    def add_global_variable_declaration(self,type:int,name:str,value:str):
        return self.global_declarations.add_variable(type,name,value)

    def add_global_function_declaration(self,type:int,name:str,param:str,code:str):
        return self.global_declarations.add_function(type,name,param,code)

    def add_template(self,name:str):
        template=Template(name)
        self.templates.append(template)
        self.system_declarations.add_process(name)
        return template

    def add_query(self,formual:str,comment:str):
        self.queries.add(formual,comment)
        return

    def writer(self):
        doc=dom.Document()
        node=doc.createElement('nta')

        node.appendChild(self.global_declarations.writer(doc))

        for template in self.templates:
            node.appendChild(template.writer(doc))

        node.appendChild(self.system_declarations.writer(doc))

        node.appendChild(self.queries.writer(doc))

        doc.appendChild(node)
        return doc





