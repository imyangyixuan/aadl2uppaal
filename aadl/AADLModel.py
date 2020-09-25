import xml.dom.minidom as dom
import re
from .Process import Process
from .BehaviorAnnex import BehaviorAnnex



class AADLModel(object):
    def __init__(self, aadl_file, instance_process_file, instance_thread_file):
        self.aadl_file = aadl_file
        self.instance_process_file = instance_process_file
        self.instance_thread_file = instance_thread_file
        self.process = None
        self.behavior_annex = []
        return

    def parse(self):
        self.root = dom.parse(self.instance_process_file)
        node = self.root.firstChild
        self.process = Process()
        self.process.parse(node)

        threads = self.process.get_threads()

        for file in self.instance_thread_file:
            node = dom.parse(file).firstChild
            for thread in threads:
                node_name = node.getAttribute('name').split('_')[0]
                if thread.name ==node_name:
                    thread.reparse(node)


        content = open(self.aadl_file).read()
        self.thread_behavior_annex(content)
        self.process.configure()
        return

    def show(self):
        self.process.show()
        for i in self.behavior_annex:
            i.show()

    def thread_behavior_annex(self,code):
        pattern0 = "thread implementation\s[\s|\S|\n]*?end\s.*;"
        pattern1 = "annex behavior_specification"
        threads = re.findall(pattern0, code)
        for thread in threads:
            result = re.search(pattern1,thread)
            if result ==None:
                continue
            else:
                behavior = BehaviorAnnex()
                behavior.parse(thread)
                self.behavior_annex.append(behavior)

        return

    def translate(self,uppaal):
        self.process.translate(uppaal)
        for i in self.behavior_annex:
            i.translate(uppaal)
        return





