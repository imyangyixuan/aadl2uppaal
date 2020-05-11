from uppaal.Declaration import Declaration,SystemDeclaration
from uppaal.Location import Location
from uppaal.Transition import Transition
from uppaal.Template import Template
from uppaal.DataType import DataType
from uppaal.UppaalModel import UppaalModel
import xml.dom.minidom as dom

if __name__ == '__main__':
    model=UppaalModel()
    t=model.add_template('trafficlight')
    t.add_variable_declaration(DataType.integer(),'red','1')
    t.add_variable_declaration(DataType.integer(),'green','0')
    t.add_function_declaration(DataType.integer(),'turn','int red,int green','\treturn red&green;')

    t.add_location('Red',0)
    t.add_location('Green',1)
    t.set_initial_location(0)

    t.add_transition(0,1)
    t.add_transition(1,0)
    '''
    doc=dom.Document()
    t=Declaration()
    t.add_variable(1,'a','3')
    print(type(t.writer(doc)))
    doc.appendChild(t.writer(doc))
    '''
    fp = open('test.xml', 'w')
    model.writer().writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
