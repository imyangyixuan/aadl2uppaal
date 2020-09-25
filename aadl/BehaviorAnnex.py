import re

variable_re = "[a-Z|A-Z|0-9|_]"


class BehaviorAnnex(object):
    def __init__(self):
        self.thread = ''
        self.variables = []
        self.states = []
        self.transitions = []
        self.pattern0 = "thread implementation.*"
        self.pattern1 = "annex behavior_specification\s\{\*\*[\s|\S|\n]*\*\*\};"
        self.pattern2 = "\{\*\*[\s|\S|\n]*\*\*\};"
        return

    def parse(self, code):
        self.thread = re.search(self.pattern0,code).group().split(' ')[-1].split('.')[0]

        get1 = re.search(self.pattern1, code).group()
        get2 = re.search(self.pattern2, get1).group()[3:-4]
        tmp = get2.split('transitions')
        self.parse_state(tmp[0].replace('states', ''))
        self.parse_transition(tmp[1])
        return

    def judge(self, code):
        get1 = re.search(self.pattern1, code).group()
        if get1 == None:
            return None

    def show(self):
        print('------------')
        print('annex behavior_specification')
        print('thread {}'.format(self.thread))
        for i in self.states:
            i.show()
        for i in self.transitions:
            i.show()
        return

    def parse_state(self, code):
        pattern = ".*:.*;"
        states = re.findall(pattern, re.sub(' +', ' ', code))
        for state in states:
            tmp = state.split(':')
            self.add_state(re.sub('\s+','',tmp[0]), tmp[1])
        return

    def parse_transition(self, code):
        code = re.sub(' +', ' ', code)
        pattern1 = ".*-\[.*\]->[\s|\w]*?;"
        transitions = re.findall(pattern1, code)
        code = re.sub(pattern1, '', code)
        transitions.extend(re.findall(".*?\};", re.sub('\s+', ' ', code)))
        for transition in transitions:
            t_from = re.sub('\s+','',re.search('.*-\[', transition).group().replace('-[', ''))
            t_to = re.sub('\s+','',re.search(']->.*', transition).group().replace(']->', ''))
            condition = re.search('\[.*\]', transition).group().replace('[', '').replace(']', '')
            tmp = re.search('\{.*\}', t_to)
            t_to = re.sub('\{.*\}', '', t_to).replace(';', '')
            if tmp == None:
                action = ''
            else:
                action = tmp.group().replace('{', '').replace('}', '')
            self.add_transition(t_from, t_to, condition, action)

    def add_variable(self, data_type, data_value):
        variable = Variable(data_type, data_value)
        self.variables.append(variable)
        return

    def add_state(self, name, param):
        state = State(name, param)
        self.states.append(state)
        return

    def add_transition(self, t_from, t_to, condition, action):
        transition = Transition(t_from, t_to, condition, action)
        self.transitions.append(transition)
        return

    def translate(self, uppaal):
        for template in uppaal.templates:
            if template.name == self.thread:
                self.translate_detail(template)

    def translate_detail(self, template):
        state_id ={}
        for i,state in enumerate(self.states):
            template.add_location(state.name,i)
            state_id[state.name]=i
            if 'initial' in state.params:
                template.set_initial_location(i)

        for  transition in self.transitions:
            t = template.add_transition(state_id[transition.t_from],state_id[transition.t_to])
            t.set_guard(transition.condition.replace('on dispatch',''))
            t.set_update(transition.action)

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
        self.name = ''
        self.params = []
        self.set_name(name)
        self.set_params(param)
        return

    def set_name(self, name):
        self.name = name.replace(' ', '')
        return

    def set_params(self, param):
        params = param.replace(';', '').split(' ')
        for param in params:
            param = re.sub('[\s]*', '', param)
            if param != '' and param != 'state':
                self.params.append(param)
        return

    def show(self):
        print('------')
        print('state {}'.format(self.name))
        print(self.params)


class Transition(object):
    def __init__(self, t_from, t_to, condition, action):
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
        self.condition = self.cond_process(condition)
        return

    def cond_process(self,condition):
        condition = condition.replace('=','==')
        return condition

    def set_action(self, action):
        return

    def show(self):
        print('------')
        print('transition')
        print('{} | {} | {} | {}'.format(self.t_from,self.t_to,self.condition,self.action))
        return