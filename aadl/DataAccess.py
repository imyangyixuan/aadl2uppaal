
class DataAccess(object):
    def __init__(self):
        self.name=''
        self.d_from=''
        self.d_to =''
        self.source=''
        self.destination=''
        return

    def parse(self,node,name):
        tmp = name.split('->')
        self.d_from = tmp[0].replace(' ', '')
        self.d_to = tmp[1].replace(' ', '')
        self.source = node.getAttribute('source')
        self.destination = node.getAttribute('destination')
        return 