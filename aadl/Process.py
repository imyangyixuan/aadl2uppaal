import xml.dom.minidom as dom
from .Subcomponent import Subcomponent
from .Connection import Connection

NODES = {
    'subcomponent': 'componentInstance',
    'connection': 'connectionInstance'
}
TYPE = 'process'


class Process(object):
    def __init__(self):
        self.subcomponent = Subcomponent()
        self.connection = Connection()
        return

    def show(self):
        self.subcomponent.show()
        self.connection.show()
        return

    def parse(self, node):
        category = node.getAttribute('category')
        if category not in  TYPE:
            print("TYPE ERROR")
            exit(1)

        subcomponents = node.getElementsByTagName(NODES['subcomponent'])
        self.parse_subcomponent(subcomponents)

        connections = node.getElementsByTagName(NODES['connection'])
        self.parse_connection(connections)

    def parse_subcomponent(self, nodes):
        self.subcomponent.parse(nodes)

    def parse_connection(self, nodes):
        self.connection.parse(nodes)
