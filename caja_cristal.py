import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertAlmostEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 10

        resultado = es_mayor_de_edad(edad)

        self.assertAlmostEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()

