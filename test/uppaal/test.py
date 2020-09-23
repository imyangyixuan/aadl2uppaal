from uppaal.Declaration import Declaration,SystemDeclaration
from uppaal.Location import Location
from uppaal.Transition import Transition
from uppaal.Template import Template
from uppaal.DataType import DataType
from uppaal.UppaalModel import UppaalModel
import xml.dom.minidom as dom

if __name__ == '__main__':
    model=UppaalModel()
    t=model.add_template('Trafficlight')
    model.add_global_variable_declaration(DataType.integer(),'time','0')
    model.add_global_variable_declaration(DataType.integer(),'count','0')
    model.add_global_variable_declaration(DataType.integer(), 'red', '1')
    model.add_global_variable_declaration(DataType.integer(), 'red_time', '30')
    model.add_global_variable_declaration(DataType.integer(), 'yellow', '0')
    model.add_global_variable_declaration(DataType.integer(), 'yellow_time', '3')
    model.add_global_variable_declaration(DataType.integer(), 'green', '0')
    model.add_global_variable_declaration(DataType.integer(), 'green_time', '20')
    model.add_global_variable_declaration(DataType.integer(), 'passenger', '0')
    model.add_global_variable_declaration(DataType.integer(), 'passed', '0')

    red=t.add_location('Red',0)
    green=t.add_location('Green',1)
    yellow=t.add_location('Yellow', 2)
    end=t.add_location('End', 3)
    t.set_initial_location(0)

    r_r=t.add_transition(0,0)
    r_r.set_guard('count<red_time')
    r_r.set_update('time+=1,\ncount+=1')
    r_g=t.add_transition(0,1)
    r_g.set_guard('count==red_time')
    r_g.set_update('count=0,\nred=0,\ngreen=0')
    g_g=t.add_transition(1,1)
    g_g.set_guard('count<green_time')
    g_g.set_update('time+=1,\ncount+=1')
    g_y=t.add_transition(1,2)
    g_y.set_guard('count==green_time')
    g_y.set_update('count=0,\ngreen=0,\nyellow=1')
    y_y=t.add_transition(2,2)
    y_y.set_guard('count<yellow_time')
    y_y.set_update('count+=1,\ntime+=1')
    y_r=t.add_transition(2,0)
    y_r.set_guard('count==yellow_time')
    y_r.set_update('count=0,\nyellow=0,\nred=1')
    r_e=t.add_transition(0,3)
    r_e.set_guard('time==100')
    g_e=t.add_transition(1,3)
    g_e.set_guard('time==100')
    y_e=t.add_transition(2,3)
    y_e.set_guard('time==100')


    fp = open('test.xml', 'w')
    model.writer().writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
