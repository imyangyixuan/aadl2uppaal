from uppaal.Declaration import Declaration,SystemDeclaration
from uppaal.Location import Location
from uppaal.Transition import Transition
from uppaal.DataType import DataType
import xml.dom.minidom as dom
if __name__ == '__main__':

    t=Transition(0,1)
    t.set_select('test select')
    t.set_guard('a==1')
    t.set_sync('sync test')
    t.set_update('update test')
    t.set_test_code('test code')
    t.set_comments('comments test')

    fp = open('test.xml', 'w')
    t.writer().writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
