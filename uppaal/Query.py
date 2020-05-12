import xml.dom.minidom as dom


class Query(object):
    def __init__(self):
        self.queries = []
        return

    def add(self, formual: str, comment: str):
        new_query = (formual, comment)
        self.queries.append(new_query)
        return

    def writer(self, doc: dom.Document):
        node = doc.createElement('queries')

        for query in self.queries:
            qnode = doc.createElement('query')
            formual = doc.createElement('formual')
            comment = doc.createElement('comment')
            formual.appendChild(doc.createTextNode(query[0]))
            comment.appendChild(doc.createTextNode(query[1]))
            qnode.appendChild(formual)
            qnode.appendChild(comment)
            node.appendChild(qnode)

        return node
