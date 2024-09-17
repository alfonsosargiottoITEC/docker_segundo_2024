import unittest

from helpers import calcular_antiguedad


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_calcular_antiguedad(self):
        fecha_fabricacion_auto = 2020
        antiguedad = calcular_antiguedad(fecha_fabricacion_auto)
        
        self.assertEqual(antiguedad, 4)

if __name__ == '__main__':
    unittest.main()