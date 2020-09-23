import xml.dom.minidom as dom
from .Process import Process

class AADLModel(object):
    def __init__(self,aadl_file,instance_file):
        self.aadl_file=aadl_file
        self.instance_file=instance_file
        return

    def parse(self):
        self.root = dom.parse(self.instance_file)
        node = self.root.firstChild
        process = Process()
        process.parse(node)

