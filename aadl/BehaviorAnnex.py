import re

variable_re = "[a-Z|A-Z|0-9|_]"

class BehaviorAnnex(object):
    def __init__(self):
        self.variables = []
        self.states = []
        self.transitions = []
        self.pattern1 = "annex behavior_specification\s\{\*\*[\s|\S|\n]*\*\*\};"
        self.pattern2 = "\{\*\*[\s|\S|\n]*\*\*\};"
        return

    def parse(self, code):
        get1 = re.search(self.pattern1,code).group()
        get2 = re.search(self.pattern2,get1).group()[3:-4]
        tmp = get2.split('transitions')
        self.parse_state(tmp[0].replace('states',''))
        self.parse_transition(tmp[1])
        return

    def parse_state(self,code):
        pattern = ".*:.*;"
        states = re.findall(pattern,re.sub(' +', ' ', code))
        for state in states:
            tmp = state.split(':')
            self.add_state(tmp[0],tmp[1])
        return

    def parse_transition(self,code):
        code = re.sub(' +',' ',code)
        pattern1 = ".*-\[.*\]->[\s|\w]*?;"
        transitions = re.findall(pattern1,code)
        code = re.sub(pattern1,'',code)
        transitions.extend(re.findall(".*?\};",re.sub('\s+',' ',code)))
        for transition in transitions:
            t_from = re.search('.*-\[',transition).group().replace('-[','').replace(' ','')
            t_to = re.search(']->.*',transition).group().replace(']->','').replace(' ','')
            condition = re.search('\[.*\]',transition).group().replace('[','').replace(']','')
            tmp = re.search('\{.*\}',t_to)
            t_to=re.sub('\{.*\}','',t_to).replace(';','')
            if tmp ==None:
                action = ''
            else:
                action = tmp.group().replace('{','').replace('}','')
            self.add_transition(t_from,t_to,condition,action)

    def add_variable(self, data_type, data_value):
        variable = Variable(data_type, data_value)
        self.variables.append(variable)
        return

    def add_state(self, name, param):
        state = State(name, param)
        self.states.append(state)
        return

    def add_transition(self, t_from, t_to, condition,action):
        transition = Transition(t_from, t_to, condition,action)
        self.transitions.append(transition)
        return


class Variable(object):
    def __init__(self, data_type, data_value):
        self.data_type = data_type
        self.data_value = data_value
        return

    def set_type(self, data_type):
        self.data_type = data_type
        return

    def set_value(self, data_value):
        self.data_value = data_value
        return


class State(object):
    def __init__(self, name, param):
        self.name=''
        self.params=[]
        self.set_name(name)
        self.set_params(param)
        return

    def set_name(self, name):
        self.name = name.replace(' ','')
        return

    def set_params(self, param):
        params = param.replace(';','').split(' ')
        for param in params:
            param = re.sub('[\s]*','',param)
            if param!='' and param!='state':
                self.params.append(param)
        return


class Transition(object):
    def __init__(self, t_from, t_to, condition,action):
        self.t_from = ''
        self.t_to = ''
        self.condition = ''
        self.action = ''

        self.set_from(t_from)
        self.set_to(t_to)
        self.set_condition(condition)
        self.set_action(action)
        return

    def set_from(self, t_from):
        self.t_from = t_from
        return

    def set_to(self, t_to):
        self.t_to = t_to
        return

    def set_condition(self, condition):
        self.condition = condition
        return

    def set_action(self,action):
        return


test_str = \
    """
    thread implementation rwr1.impl
        subcomponents
            b: data Base_Types::Integer
            {
                Data_Model::Initial_Value => ("-1");
            };
            counts: data Base_Types::Integer
            {
                Data_Model::Initial_Value => ("0");
            };
        annex behavior_specification {**
        states
            rwr1_start: initial complete state;
            rwr1_1: state;
            rwr1_2: state;
            rwr1_3: state;
            rwr1_4: state;
            rwr1_end: final state;
        transitions
            rwr1_start -[on dispatch]-> rwr1_1;
            rwr1_1 -[rwr = 1]-> rwr1_2;
            rwr1_1 -[not(rwr = 1)]-> rwr1_end;
            rwr1_2 -[counts < 2]-> rwr1_3{
                b := rwr;
                message1!};
            rwr1_3 -[]-> rwr1_4{
                message2?;
                counts := counts + 1};
            rwr1_2 -[not(counts < 2)]-> rwr1_end{
                message1!};
            rwr1_4 -[]-> rwr1_2;
        **};
    end rwr1.impl;
    """

if __name__ == '__main__':

    behavior_annex = BehaviorAnnex()
    behavior_annex.parse(test_str)
