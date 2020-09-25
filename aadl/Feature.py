from .Port import Port
from .DataAccess import DataAccess
class Feature(object):
    def __init__(self):
        self.features=[]
        return

    def show(self):
        print('------')
        print('features')
        for i in self.features:
            i[1].show()
        return

    def parse(self,nodes):
        for node in nodes:
            category = node.getAttribute('category')
            #print(category)
            if category[-4:] == 'Port':
                self.parse_port(node)
                continue
            if category == 'dataAccess':
                self.parse_data_access(node)
                continue

        return

    def parse_port(self,node):
        port = Port()
        port.parse(node,'thread')
        self.features.append(('port',port))
        return

    def parse_data_access(self,node):
        data_access = DataAccess()
        data_access.parse(node,'thread')
        self.features.append(('data_access',data_access))
        return

    def translate(self,uppaal):
        pass