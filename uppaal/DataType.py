DATA_TYPE={
    'int':1,
    'fun':2
}

DATA_TYPE_REVERSE={v:k for k,v in DATA_TYPE.items()}

class DataType(object):
    @staticmethod
    def integer():
        return DATA_TYPE['int']

    @staticmethod
    def function():
        return DATA_TYPE['fun']

    @staticmethod
    def type2str(type:int):
        return DATA_TYPE_REVERSE[type]

    @staticmethod
    def type2int(type:str):
        return DATA_TYPE[type]