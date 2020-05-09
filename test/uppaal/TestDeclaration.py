import unittest
from uppaal.Declaration import Declaration

class TestDeclaration(unittest.TestCase):

    def test_add_(self):
        d=Declaration()
        c=d.add_variable('int','a','2')
        c.name='b'
        self.assertEqual(d.variable_declarations[0].name,c.name)

if __name__ == '__main__':
    unittest.main()


