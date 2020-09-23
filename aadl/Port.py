TYPE = ['event','data','event data']
DIRECTION = ['in','out']

class Port(object):
    def __init__(self):
        self.direction=''
        self.type=''
        self.p_from=''
        self.p_to=''
        self.source=''
        self.destination=''
        return

    def parse(self,node,name):
        tmp = name.split('->')
        self.p_from = tmp[0].replace(' ','')
        self.p_to = tmp[1].replace(' ','')
        self.source=node.getAttribute('source')
        self.destination=node.getAttribute('destination')
        self.type = 'event'
        return
