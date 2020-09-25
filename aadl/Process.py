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
        self.name=''
        self.subcomponent = Subcomponent()
        self.connection = Connection()
        return

    def show(self):
        print('------------')
        print('process {}'.format(self.name))
        self.subcomponent.show()
        self.connection.show()
        return

    def parse(self, node):
        self.name = node.getAttribute('name')
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
        return

    def get_threads(self):
        threads=[]
        for i in self.subcomponent.components:
            if i[0]=='thread':
                threads.append(i[1])
        return threads

    def configure(self):
        ports = self.connection.configure()
        for port in ports:
            for component in self.subcomponent.components:
                if component[0]=='thread' and component[1].name==port[0]:
                    component[1].configure((port[1],port[2]))
        return

    def translate(self,uppaal):
        self.subcomponent.translate(uppaal)
        self.connection.translate(uppaal)
        return
