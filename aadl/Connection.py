from .Port import Port
from .DataAccess import DataAccess

NODES = {
    'level1': 'connectionReference',
    'level2': 'connection'
}

TYPE = {
    'port': 'portConnection',
    'data_access': 'accessConnection'
}

TYPE_REVERSE = dict([val, key] for key, val in TYPE.items())

class Connection(object):
    def __init__(self):
        self.connections = []
        return

    def show(self):
        for i in self.connections:
            print(i)
        return

    def parse(self, nodes):
        for node in nodes:
            kind = node.getAttribute('kind')
            name = node.getAttribute('name')
            if kind == TYPE['port']:
                self.parse_port(node,name)
                continue
            if kind ==TYPE['data_access']:
                self.parse_data_access(node,name)
                continue
        return

    def parse_port(self,node,name):
        port = Port()
        port.parse(node,name)
        self.connections.append(('port',port))
        return

    def parse_data_access(self,node,name):
        data_access = DataAccess()
        data_access.parse(node,name)
        self.connections.append(('data_access',data_access))
        return

