import xml.dom.minidom as dom
from .Data import Data

NODES = {

}

TYPE = ['data','thread']

UPPAAL_TYPE = {
    'integer':1
}

class Subcomponent(object):
    def __init__(self):
        self.components = []
        return

    def show(self):
        print('------')
        print('components')
        for i in self.components:
            i[1].show()
        return

    def parse(self,nodes):
        for node in nodes:
            category = node.getAttribute('category')
            if category == 'data':
                self.parse_data(node)
                continue

            if category == 'thread':
                self.parse_thread(node)
                continue
        return

    def parse_data(self,node):
        data = Data()
        data.parse(node)
        self.components.append(('data',data))
        return

    def parse_thread(self,node):
        from .Thread import Thread
        thread = Thread()
        thread.parse(node)
        self.components.append(('thread',thread))
        return

    def translate(self,uppaal):
        for i in self.components:
            if i[0]=='thread':
                i[1].translate(uppaal)
            if i[0]=='data':
                uppaal.add_global_variable_declaration(UPPAAL_TYPE[i[1].type],i[1].name,i[1].value)
        return