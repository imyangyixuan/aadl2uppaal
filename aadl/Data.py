NODES = {
    'type':'classifier',
    'value1':'ownedPropertyAssociation',
    'value2':'ownedValue',
    'value3':'ownedListElement'
}

TYPE = {
    "integer" : "platform:/plugin/org.osate.contribution.sei/resources/packages/Base_Types.aadl#Base_Types.Integer"
}

TYPE_REVERSE = dict([val, key] for key, val in TYPE.items())

class Data(object):
    def __init__(self):
        self.name=''
        self.type=''
        self.value=0
        return

    def parse(self,node):
        self.name = node.getAttribute('name')
        self.parse_type(node)
        self.parse_value(node)
        return

    def parse_type(self,node):
        one = node.getElementsByTagName(NODES['type'])[0]
        two = one.getAttribute('href')
        self.value = TYPE_REVERSE[two]
        return

    def parse_value(self,node):
        one = node.getElementsByTagName(NODES['value1'])[0]
        two = one.getElementsByTagName(NODES['value2'])[0]
        three = two.getElementsByTagName(NODES['value2'])[0]
        four = three.getElementsByTagName(NODES['value3'])[0]
        self.value = four.getAttribute('value')
        return