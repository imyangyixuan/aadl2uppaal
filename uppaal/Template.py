from .Declaration import Declaration

class Template(object):
    def __init__(self):
        self.name=''
        self.locations=[]
        self.transitions=[]
        self.declarations=Declaration()
        return

    def writer(self):

        return