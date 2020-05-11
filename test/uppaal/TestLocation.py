import unittest
from uppaal.Location import Location

class TestLocation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.l=Location('red',0)
        return

    def test_base(self):
        self.assertEqual('red',self.l.name)
        self.assertEqual('id0',self.l.id)
        return

    def test_urgent(self):
        self.l.set_urgent(True)
        self.assertEqual(True,self.l.is_urgent)
        self.assertEqual(False,self.l.is_committed)
        return

    def test_commited(self):
        self.l.set_committed(True)
        self.assertEqual(True,self.l.is_committed)
        self.assertEqual(False,self.l.is_urgent)
        return

if __name__ == '__main__':
    unittest.main()