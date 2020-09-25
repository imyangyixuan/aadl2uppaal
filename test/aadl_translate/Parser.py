from aadl.AADLModel import AADLModel


if __name__ == '__main__':
    test = AADLModel('model_1.aadl',"model_1_rwr_impl_Instance.aaxl2",['model_1_rwr1_impl_Instance.aaxl2','model_1_rwr2_impl_Instance.aaxl2'])
    test.parse()
    test.show()
