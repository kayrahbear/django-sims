'''
This is a simple test module.
'''
from django.test import SimpleTestCase
from .calc import add, subtract

class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
