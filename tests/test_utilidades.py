import unittest

from utilidades import calcular_antiguedad_vehiculo


class TestUtilidades(unittest.TestCase):

    def test_calcular_antiguedad(self):
        fecha_fabricacion_auto = 2020
        antiguedad = calcular_antiguedad_vehiculo(fecha_fabricacion_auto)
        
        self.assertEqual(antiguedad, 4)
        
    def test_calcular_antiguedad_1(self):
        fecha_fabricacion_auto = 2010
        antiguedad = calcular_antiguedad_vehiculo(fecha_fabricacion_auto)
        
        self.assertEqual(antiguedad, 14)

if __name__ == '__main__':
    unittest.main()