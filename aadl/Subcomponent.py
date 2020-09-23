import xml.dom.minidom as dom
from .Data import Data
from .Thread import Thread

NODES = {

}

TYPE = ['data','thread']

class Subcomponent(object):
    def __init__(self):
        self.components = []
        return

    def show(self):
        for i in self.components:
            print(i)
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
        thread = Thread()
        thread.parse(node)
        self.components.append(('thread',thread))
        return