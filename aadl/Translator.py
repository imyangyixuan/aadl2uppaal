from .Model import Model
from uppaal.UppaalModel import UppaalModel

class Translator(object):
    def translate(self,aadl):
        uppaal = UppaalModel()
        Model.translate(aadl,uppaal)
        return