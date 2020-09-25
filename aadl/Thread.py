from .Feature import Feature
from .Subcomponent import Subcomponent

NODES = {
    'feature':'featureInstance',
    'subcomponent': 'componentInstance'
}

UPPAAL_TYPE = {
    'integer':1
}

class Thread(object):
    def __init__(self):
        self.features=Feature()
        self.subcomponents=Subcomponent()
        self.param=[]
        self.argu=[]
        return

    def show(self):
        print('------')
        print('thread {}'.format(self.name))
        print(self.param)
        self.features.show()
        self.subcomponents.show()
        return

    def parse(self,node):
        self.name = node.getAttribute('name')
        subcomponents = node.getElementsByTagName(NODES['subcomponent'])
        self.parse_subcomponent(subcomponents)

        features = node.getElementsByTagName(NODES['feature'])
        self.parse_feature(features)
        return

    def reparse(self,node):
        subcomponents = node.getElementsByTagName(NODES['subcomponent'])
        self.parse_subcomponent(subcomponents)
        return

    def parse_subcomponent(self, nodes):
        self.subcomponents.parse(nodes)

    def parse_feature(self, nodes):
        self.features.parse(nodes)
        return

    def configure(self,argu):
        for i in self.features.features:
            if i[0]=='port' and i[1].name==argu[0]:
                self.argu.append(argu[1])
                self.param.append('chan &'+argu[0])

    def translate(self,uppaal):
        template = uppaal.add_template(self.name)
        argu=''
        for i in self.argu:
            argu+=i+','
        argu = argu[:-1]
        template.add_argu(argu)

        param = ''
        for i in self.param:
            param += i + ','
        param = param[:-1]
        template.add_param(param)

        for i in self.subcomponents.components:
            if i[0]=='data':
                template.add_variable_declaration(UPPAAL_TYPE[i[1].type],i[1].name,i[1].value)
