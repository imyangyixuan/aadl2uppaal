import unittest
from uppaal.Declaration import _VariableDec, _FunctionDec, Declaration, SystemDeclaration
from uppaal.DataType import DataType


class Test_Variable_Declaration(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.v = _VariableDec(DataType.integer(), 'a', '3')
        self.v1 = _VariableDec(DataType.integer(), 'a', '')
        return

    def test_init(self):
        self.assertEqual(self.v.type, DataType.integer())
        self.assertEqual(self.v.name, 'a')
        self.assertEqual(self.v.is_assigned, True)
        self.assertEqual(self.v.value, '3')

        self.assertEqual(self.v1.type, DataType.integer())
        self.assertEqual(self.v1.name, 'a')
        self.assertEqual(self.v1.is_assigned, False)
        self.assertEqual(self.v1.value, '')
        return

    def test_str(self):
        self.assertEqual(str(self.v), 'int a=3;')
        self.assertEqual(str(self.v1), 'int a;')
        return

    def test_writer(self):
        self.assertEqual(self.v.__str__(), 'int a=3;')
        self.assertEqual(self.v1.__str__(), 'int a;')
        return

    def test_set(self):
        v = _VariableDec(DataType.integer(), 'a', '')

        v.set_type(DataType.float())
        self.assertEqual(v.type, DataType.float())

        v.set_name('b')
        self.assertEqual(v.name, 'b')

        v.set_value('')
        self.assertEqual(v.value, '')
        self.assertEqual(v.is_assigned, False)

        v.set_value('3')
        self.assertEqual(v.value, '3')
        self.assertEqual(v.is_assigned, True)
        return


class Test_Function_Declaration(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.f = _FunctionDec(DataType.integer(), 'fun', 'int a,int b', '\treturn a+b;')
        return

    def test_init(self):
        self.assertEqual(self.f.type, DataType.integer())
        self.assertEqual(self.f.name, 'fun')
        self.assertEqual(self.f.param, 'int a,int b')
        self.assertEqual(self.f.code, '\treturn a+b;')
        return

    def test_set(self):
        self.f.set_type(DataType.float())
        self.assertEqual(self.f.type, DataType.float())

        self.f.set_name('method')
        self.assertEqual(self.f.name, 'method')

        self.f.set_param('int a')
        self.assertEqual(self.f.param, 'int a')

        self.f.set_code('\treturn a+1')
        self.assertEqual(self.f.code, '\treturn a+1')
        return


class TestDeclaration(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.d = Declaration()
        return

    def test_add(self):
        v = self.d.add_variable(DataType.integer(), 'a', '2')
        v1 = self.d.add_variable(DataType.float(), 'b', '')
        f = self.d.add_function(DataType.integer(), 'sum', 'int a,int b', '\treturn a+b;')
        f1 = self.d.add_function(DataType.float(), 'increase_half', 'float v', '\treturn v+0.5;')

        self.assertEqual(isinstance(v, _VariableDec), True)
        self.assertEqual(isinstance(v1, _VariableDec), True)
        self.assertEqual(isinstance(f, _FunctionDec), True)
        self.assertEqual(isinstance(f1, _FunctionDec), True)

        self.assertEqual(len(self.d.variable_declarations), 2)
        self.assertEqual(len(self.d.function_declarations), 2)
        return

    def test_writer(self):
        result = 'int a=2;\nfloat b;\n\n\nint sum(int a,int b){\n\treturn a+b;\n}\nfloat increase_half(float v){\n\treturn v+0.5;\n}\n'

        self.assertEqual(self.d.__str__(), result)
        return


class TestSystemDeclaration(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.sd = SystemDeclaration()
        return

    def test_add(self):
        self.sd.add_process('a')
        self.sd.add_process('b')
        self.assertEqual(len(self.sd.processes), 2)
        return

    def test_writer(self):
        result = 'Process0=a();\nProcess1=b();\n\n\nsystem Process0,Process1;'

        self.assertEqual(result, self.sd.__str__())
        return


if __name__ == '__main__':
    unittest.main()
