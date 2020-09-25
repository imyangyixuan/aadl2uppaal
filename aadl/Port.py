TYPE = ['event','data','event data']
DIRECTION = ['in','out']
DECLARATION = 'chan '

class Port(object):
    def __init__(self):
        self.name=''
        self.f_type=''
        self.direction=''
        self.type=''
        self.p_from=''
        self.p_to=''
        self.source=''
        self.destination=''
        self.declaration=''
        return

    def show(self):
        print('port : {} | {} | {} | {} | {} | {} | {}'.format(self.name,self.direction,self.type,self.p_from,self.p_to,self.source,self.destination))

    def parse(self,node,f_type):
        if f_type=='thread':
            self.thread_parse(node)

        if f_type=='connection':
            self.connection_parse(node)

    def thread_parse(self,node):
        self.name = node.getAttribute('name')
        direction = node.getAttribute('direction')
        if direction == None:
            self.direction='in'
        else:
            self.direction='out'
        self.type = node.getAttribute('category')


    def connection_parse(self,node):
        name = node.getAttribute('name')
        tmp = name.split('->')
        self.p_from = tmp[0].replace(' ', '')
        self.p_to = tmp[1].replace(' ', '')
        self.source = node.getAttribute('source')
        self.destination = node.getAttribute('destination')
        self.type = 'event'
        return

    def configure(self,num):
        variable = 'ch'+str(num)
        declaration = DECLARATION+variable
        self.declaration=declaration
        one = self.p_from.split('.')
        thread1 = (one[0],one[1],variable)
        two = self.p_to.split('.')
        thread2 = (two[0],two[1],variable)
        return [thread1,thread2]


    def translate(self,uppaal):
        pass