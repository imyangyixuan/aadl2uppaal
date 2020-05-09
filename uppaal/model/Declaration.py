class _VariableDec(object):
    def __init__(self, type: int, name: str, value: str == ''):
        '''
        :param type: the data type of the declaration
        :param name: the name of the variable
        :param value: the value of the variable if it exists
        '''
        self.type = type
        self.name = name

        # assign the variable 'is_assigned' and 'value' according to the param 'value'
        if value:
            self.is_assigned = True
            self.value = value
        else:
            self.is_assigned = False
            self.value = None
        return

    def __str__(self):
        '''
        :return: the declaration string
        '''
        declaration = DataType.type2str(self.type) + ' ' + self.name

        if self.is_assigned:
            return declaration + ' = ' + self.value + ';'
        else:
            return declaration + ';'


class _FunctionDec(object):
    def __init__(self, type: str, name: str, param: str, code: str):
        self.type = type
        self.name = name
        self.param = param
        self.code = code
        return

    def __str__(self):
        return self.type + ' ' + self.name + '(' + self.param + ')' + '{\n' + self.code + '\n}'


class Declaration(object):
    def __init__(self):
        self.variable_declarations = []
        self.function_declarations = []
        return

    def add_variable(self,type:str,name:str,value:str):
        declaration=_VariableDec(type,name,value)
        self.variable_declarations.append(declaration)
        return declaration

    def add_function(self,type: str, name: str, param: str, code: str):
        declaration=_FunctionDec(type,name,param,code)
        self.function_declarations.append(declaration)
        return declaration

