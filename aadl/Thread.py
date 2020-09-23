from .Feature import Feature
from .Subcomponent import Subcomponent

NODES = {
    'feature':'featureInstance',
    'subcomponent': 'componentInstance'
}

class Thread(object):
    def __init__(self,node):
        self.name = node.getAttribute('name')
        self.features=Feature()
        self.subcomponents=Subcomponent()
        return

    def parse(self,node):
        subcomponents = node.getElementsByTagName(NODES['subcomponent'])
        self.parse_subcomponent(subcomponents)

        features = node.getElementsByTagName(NODES['feature'])
        self.parse_feature(features)
        return

    def parse_subcomponent(self, nodes):
        self.subcomponent.parse(nodes)

    def parse_feature(self, nodes):
        self.features.parse(nodes)