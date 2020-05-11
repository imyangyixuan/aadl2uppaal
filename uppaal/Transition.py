import xml.dom.minidom as dom
class Transition(object):
    def __init__(self,source:int,target:int):
        self.source='id'+str(source)
        self.target='id'+str(target)
        self.select = ''
        self.guard = ''
        self.sync = ''
        self.update = ''
        self.comments = ''
        self.test_code = ''
        return

    def set_select(self,select:str):
        self.select=select
        return

    def set_guard(self,guard:str):
        self.guard=guard
        return

    def set_sync(self,sync:str):
        self.sync=sync
        return

    def set_update(self,update:str):
        self.update=update
        return

    def set_comments(self,comments:str):
        self.comments=comments
        return

    def set_test_code(self,test_code:str):
        self.test_code=test_code
        return


    def writer(self):
        doc=dom.Document()
        node=doc.createElement('transition')

        source=doc.createElement('source')
        source.setAttribute('ref',self.source)
        node.appendChild(source)
        target=doc.createElement('target')
        target.setAttribute('ref',self.target)
        node.appendChild(target)

        if self.select:
            select=doc.createElement('label')
            select.setAttribute('kind','select')
            select.appendChild(doc.createTextNode(self.select))
            node.appendChild(select)

        if self.guard:
            guard=doc.createElement('label')
            guard.setAttribute('kind','guard')
            guard.appendChild(doc.createTextNode(self.guard))
            node.appendChild(guard)

        if self.sync:
            sync=doc.createElement('label')
            sync.setAttribute('kind','synchronisation')
            sync.appendChild(doc.createTextNode(self.sync))
            node.appendChild(sync)

        if self.update:
            update=doc.createElement('label')
            update.setAttribute('kind','assignment')
            update.appendChild(doc.createTextNode(self.update))
            node.appendChild(update)

        if self.test_code:
            test_code=doc.createElement('label')
            test_code.setAttribute('kind','testcode')
            test_code.appendChild(doc.createTextNode(self.test_code))
            node.appendChild(test_code)

        if self.comments:
            comments=doc.createElement('label')
            comments.setAttribute('kind','comments')
            comments.appendChild(doc.createTextNode(self.comments))
            node.appendChild(comments)

        doc.appendChild(node)
        return doc
