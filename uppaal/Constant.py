
ASSIGNED_VARIABLE_DECLARATION='{} {}={};'

UNASSIGNED_VARIABLE_DECLARATION='{} {};'

FUNCTION_DECLARATION=('{} {}({}){{\n'
                      '{}\n'
                      '}}')

SYSTEM_DECLARATION='Process{}={}();'

if __name__ == '__main__':
    print(FUNCTION_DECLARATION.format('int','a','c','\tc=1;\n\treturn c'))