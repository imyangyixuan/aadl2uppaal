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
        print('------')
        print('connections')
        for i in self.connections:
            i[1].show()
        return

    def parse(self, nodes):
        for node in nodes:
            kind = node.getAttribute('kind')
            name = node.getAttribute('name')
            if kind == TYPE['port']:
                self.parse_port(node)
                continue
            if kind ==TYPE['data_access']:
                self.parse_data_access(node)
                continue
        return

    def parse_port(self,node):
        port = Port()
        port.parse(node,'connection')
        self.connections.append(('port',port))
        return

    def parse_data_access(self,node):
        data_access = DataAccess()
        data_access.parse(node,'connection')
        self.connections.append(('data_access',data_access))
        return

    def configure(self):
        result = []
        j=0
        for i in self.connections:
            if i[0]=='port':
                result.extend(i[1].configure(j))
                j+=1
        return result

    def translate(self,uppaal):
        for i in self.connections:
            if i[0]=='port':
                uppaal.system_declarations.add_variable_declaration(i[1].declaration)
            if i[0]=='data_access':
                pass

