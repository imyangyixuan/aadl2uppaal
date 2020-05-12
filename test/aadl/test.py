import xml.dom.minidom as dom

if __name__ == '__main__':
    tree= dom.parse('Ball_AADL.xml')
    doc=tree.documentElement
    node=doc.getElementsByTagName('ownedPublicSection')[0]
    for i in node.childNodes:
        print(i)

