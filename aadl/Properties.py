
class Property(object):
    def __init__(self,name:str,type:str,value:str):
        self.name=name
        self.type=type
        self.value=value
        return

    def assign(self,value:str):
        self.value=value
        return


class Properties(object):
    def __init__(self):
        self.properties=[]

        self.self_defines=[]

        self.components=[]
        self.subcomponents=[]
        self.features=[]
        self.connections=[]
        self.flows=[]
        self.modes=[]
        self.subprogram_calls=[]
        return
