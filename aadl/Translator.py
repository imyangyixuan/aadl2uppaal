from .AADLModel import AADLModel
from uppaal.UppaalModel import UppaalModel

class Translator(object):
    @staticmethod
    def translate(aadl):
        uppaal = UppaalModel()
        aadl.translate(uppaal)
        fp = open(aadl.process.name+'.xml','w')
        uppaal.writer().writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        return