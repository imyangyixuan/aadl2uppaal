from aadl.AADLModel import AADLModel
from aadl.Translator import Translator

if __name__ == '__main__':
    test = AADLModel('model_1.aadl',"model_1_rwr_impl_Instance.aaxl2",['model_1_rwr1_impl_Instance.aaxl2','model_1_rwr2_impl_Instance.aaxl2'])
    test.parse()
    test.show()
    Translator.translate(test)

