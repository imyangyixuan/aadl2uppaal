
class Property(object):
    def __init__(self,name:str,type:str,value:str,unit:str):
        self.name=name
        self.type=type
        self.value=value
        self.unit=unit
        return

    def assign(self,value:str,unit:str):
        self.value=value
        self.unit=unit
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
