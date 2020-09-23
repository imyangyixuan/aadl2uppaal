from uppaal.DataType import DataType
from uppaal.UppaalModel import UppaalModel

if __name__ == '__main__':
    model=UppaalModel()
    t=model.add_template('Trafficlight')
    model.add_global_variable_declaration(DataType.integer(),'time','0')
    model.add_global_variable_declaration(DataType.integer(),'count','0')
    # ......
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
    # ......
    y_e=t.add_transition(2,3)
    y_e.set_guard('time==100')


    fp = open('test.xml', 'w')
    model.writer().writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")











