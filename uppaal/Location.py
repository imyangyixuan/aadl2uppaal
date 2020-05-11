import xml.dom.minidom as dom


class Location(object):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = 'id' + str(id)
        self.invariant = ''
        self.exponentialrate = ''
        self.is_urgent = False
        self.is_committed = False
        self.comments = ''
        self.testcodeEnter = ''
        self.testcodeExit = ''
        return

    def set_invariant(self, invariant: str):
        self.invariant = invariant
        return

    def set_exponentialrate(self, rate_of_exponential: str):
        self.exponentialrate = rate_of_exponential
        return

    def set_urgent(self, urgent: bool = False):
        self.is_urgent = urgent
        if urgent:
            self.is_committed = False
        return

    def set_committed(self, commited: bool = False):
        self.is_committed = commited
        if commited:
            self.is_urgent = False

    def set_comments(self, comments: str):
        self.comments = comments
        return

    def set_test_code(self, on_enter: str = '', on_exit: str = ''):
        if on_enter:
            self.testcodeEnter = on_enter
        if on_exit:
            self.testcodeExit = on_exit
        return

    def writer(self):
        doc = dom.Document()
        node = doc.createElement('location')
        node.setAttribute('id', self.id)

        name = doc.createElement('name')
        name.appendChild(doc.createTextNode(self.name))
        node.appendChild(name)

        if self.invariant:
            invariant = doc.createElement('label')
            invariant.setAttribute('kind','invariant')
            invariant.appendChild(doc.createTextNode(self.invariant))
            node.appendChild(invariant)

        if self.exponentialrate:
            exponentialrate = doc.createElement('label')
            exponentialrate.setAttribute('kind','exponentialrate')
            exponentialrate.appendChild(doc.createTextNode(self.exponentialrate))
            node.appendChild(exponentialrate)

        if self.testcodeEnter:
            testcodeEnter = doc.createElement('label')
            testcodeEnter.setAttribute('kind','testcodeEnter')
            testcodeEnter.appendChild(doc.createTextNode(self.testcodeEnter))
            node.appendChild(testcodeEnter)

        if self.testcodeExit:
            testcodeExit = doc.createElement('label')
            testcodeExit.setAttribute('kind','testcodeExit')
            testcodeExit.appendChild(doc.createTextNode(self.testcodeExit))
            node.appendChild(testcodeExit)

        if self.comments:
            comments = doc.createElement('label')
            comments.setAttribute('kind','comments')
            comments.appendChild(doc.createTextNode(self.comments))
            node.appendChild(comments)

        if self.is_urgent:
            urgent = doc.createElement('urgent')
            node.appendChild(urgent)
        elif self.is_committed:
            committed = doc.createElement('committed')
            node.appendChild(committed)

        doc.appendChild(node)
        return doc
