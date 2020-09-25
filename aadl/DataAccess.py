
class DataAccess(object):
    def __init__(self):
        self.name=''
        self.type=''
        self.d_from=''
        self.d_to =''
        self.source=''
        self.destination=''
        return

    def show(self):
        print('data_access : {} | {} | {} | {} | {} | {}'.format(self.name,self.type,self.d_from,self.d_to,self.source,self.destination))
        return

    def parse(self,node,f_type):
        if f_type=='thread':
            self.thread_parse(node)

        if f_type=='connection':
            self.connection_parse(node)

    def thread_parse(self,node):
        self.name = node.getAttribute('name')
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

    def translate(self,uppaal):
        pass