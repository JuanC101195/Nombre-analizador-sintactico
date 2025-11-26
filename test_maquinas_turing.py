"""
Tests Automatizados para Máquinas de Turing
Autores: Juan Esteban Cardozo Rivera, Juan Sebastián Gómez Usuga

Tests completos para verificar el funcionamiento correcto de:
1. maquina_turing_aritmetica.py
2. maquina_turing_lenguajes.py
"""

import unittest
import sys
import os

# Añadir el directorio actual al path para importar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from maquina_turing_aritmetica import MaquinaTuring
from maquina_turing_lenguajes import MaquinaTuringLenguajes


class TestMaquinaTuringAritmetica(unittest.TestCase):
    """Tests para Máquina de Turing - Operaciones Aritméticas"""
    
    def setUp(self):
        """Configurar máquina antes de cada test"""
        self.mt = MaquinaTuring()
    
    def test_suma_basica(self):
        """Test: Suma básica 1+1 = 2"""
        resultado, historial = self.mt.suma_unaria(1, 1)
        self.assertEqual(resultado, 2, "1+1 debe ser 2")
        self.assertTrue(len(historial) > 0, "Debe generar historial")
    
    def test_suma_3_mas_2(self):
        """Test: Suma 3+2 = 5"""
        resultado, historial = self.mt.suma_unaria(3, 2)
        self.assertEqual(resultado, 5, "3+2 debe ser 5")
    
    def test_suma_4_mas_3(self):
        """Test: Suma 4+3 = 7"""
        resultado, historial = self.mt.suma_unaria(4, 3)
        self.assertEqual(resultado, 7, "4+3 debe ser 7")
    
    def test_suma_5_mas_4(self):
        """Test: Suma 5+4 = 9"""
        resultado, historial = self.mt.suma_unaria(5, 4)
        self.assertEqual(resultado, 9, "5+4 debe ser 9")
    
    def test_suma_cero(self):
        """Test: Suma con cero 5+0 = 5"""
        resultado, historial = self.mt.suma_unaria(5, 0)
        self.assertEqual(resultado, 5, "5+0 debe ser 5")
    
    def test_multiplicacion_basica(self):
        """Test: Multiplicación básica 1*1 = 1"""
        resultado, historial = self.mt.multiplicacion_unaria(1, 1)
        self.assertEqual(resultado, 1, "1*1 debe ser 1")
        self.assertTrue(len(historial) > 0, "Debe generar historial")
    
    def test_multiplicacion_2_por_3(self):
        """Test: Multiplicación 2*3 = 6"""
        resultado, historial = self.mt.multiplicacion_unaria(2, 3)
        self.assertEqual(resultado, 6, "2*3 debe ser 6")
    
    def test_multiplicacion_3_por_2(self):
        """Test: Multiplicación 3*2 = 6"""
        resultado, historial = self.mt.multiplicacion_unaria(3, 2)
        self.assertEqual(resultado, 6, "3*2 debe ser 6")
    
    def test_multiplicacion_2_por_4(self):
        """Test: Multiplicación 2*4 = 8"""
        resultado, historial = self.mt.multiplicacion_unaria(2, 4)
        self.assertEqual(resultado, 8, "2*4 debe ser 8")
    
    def test_multiplicacion_por_cero(self):
        """Test: Multiplicación por cero 5*0 = 0"""
        resultado, historial = self.mt.multiplicacion_unaria(5, 0)
        self.assertEqual(resultado, 0, "5*0 debe ser 0")
    
    def test_historial_no_vacio(self):
        """Test: El historial debe contener pasos"""
        resultado, historial = self.mt.suma_unaria(2, 2)
        self.assertGreater(len(historial), 0, "El historial no debe estar vacío")
        self.assertIn('paso', historial[0], "Cada paso debe tener número")
        self.assertIn('estado', historial[0], "Cada paso debe tener estado")
        self.assertIn('cinta', historial[0], "Cada paso debe mostrar cinta")


class TestMaquinaTuringLenguajes(unittest.TestCase):
    """Tests para Máquina de Turing - Reconocimiento de Lenguajes"""
    
    def setUp(self):
        """Configurar máquina antes de cada test"""
        self.mt = MaquinaTuringLenguajes()
    
    # ===== TESTS PARA L = {a^n b^n c^n} =====
    
    def test_anbncn_abc(self):
        """Test a^n b^n c^n: 'abc' debe ser aceptada (1:1:1)"""
        aceptada, historial = self.mt.reconocer_anbn("abc")
        self.assertTrue(aceptada, "'abc' debe ser aceptada en a^n b^n c^n")
    
    def test_anbncn_aabbcc(self):
        """Test a^n b^n c^n: 'aabbcc' debe ser aceptada (2:2:2)"""
        aceptada, historial = self.mt.reconocer_anbn("aabbcc")
        self.assertTrue(aceptada, "'aabbcc' debe ser aceptada")
    
    def test_anbncn_aaabbbccc(self):
        """Test a^n b^n c^n: 'aaabbbccc' debe ser aceptada (3:3:3)"""
        aceptada, historial = self.mt.reconocer_anbn("aaabbbccc")
        self.assertTrue(aceptada, "'aaabbbccc' debe ser aceptada")
    
    def test_anbncn_aaaabbbbcccc(self):
        """Test a^n b^n c^n: 'aaaabbbbcccc' debe ser aceptada (4:4:4)"""
        aceptada, historial = self.mt.reconocer_anbn("aaaabbbbcccc")
        self.assertTrue(aceptada, "'aaaabbbbcccc' debe ser aceptada")
    
    def test_anbncn_rechaza_ab(self):
        """Test a^n b^n c^n: 'ab' debe ser rechazada (falta c)"""
        aceptada, historial = self.mt.reconocer_anbn("ab")
        self.assertFalse(aceptada, "'ab' debe ser rechazada")
    
    def test_anbncn_rechaza_aabbc(self):
        """Test a^n b^n c^n: 'aabbc' debe ser rechazada (falta una c)"""
        aceptada, historial = self.mt.reconocer_anbn("aabbc")
        self.assertFalse(aceptada, "'aabbc' debe ser rechazada")
    
    def test_anbncn_rechaza_abcc(self):
        """Test a^n b^n c^n: 'abcc' debe ser rechazada (sobra una c)"""
        aceptada, historial = self.mt.reconocer_anbn("abcc")
        self.assertFalse(aceptada, "'abcc' debe ser rechazada")
    
    def test_anbncn_rechaza_abcabc(self):
        """Test a^n b^n c^n: 'abcabc' debe ser rechazada (intercalado)"""
        aceptada, historial = self.mt.reconocer_anbn("abcabc")
        self.assertFalse(aceptada, "'abcabc' debe ser rechazada")
    
    def test_anbncn_rechaza_cba(self):
        """Test a^n b^n c^n: 'cba' debe ser rechazada (orden inverso)"""
        aceptada, historial = self.mt.reconocer_anbn("cba")
        self.assertFalse(aceptada, "'cba' debe ser rechazada")
    
    # ===== TESTS PARA PALÍNDROMOS =====
    
    def test_palindromo_cadena_vacia(self):
        """Test palíndromo: Cadena vacía debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("")
        self.assertTrue(aceptada, "Cadena vacía es palíndromo")
    
    def test_palindromo_a(self):
        """Test palíndromo: 'a' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("a")
        self.assertTrue(aceptada, "'a' es palíndromo")
    
    def test_palindromo_b(self):
        """Test palíndromo: 'b' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("b")
        self.assertTrue(aceptada, "'b' es palíndromo")
    
    def test_palindromo_aa(self):
        """Test palíndromo: 'aa' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("aa")
        self.assertTrue(aceptada, "'aa' es palíndromo")
    
    def test_palindromo_aba(self):
        """Test palíndromo: 'aba' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("aba")
        self.assertTrue(aceptada, "'aba' es palíndromo")
    
    def test_palindromo_abba(self):
        """Test palíndromo: 'abba' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("abba")
        self.assertTrue(aceptada, "'abba' es palíndromo")
    
    def test_palindromo_aabbaa(self):
        """Test palíndromo: 'aabbaa' debe ser aceptada"""
        aceptada, historial = self.mt.reconocer_palindromo("aabbaa")
        self.assertTrue(aceptada, "'aabbaa' es palíndromo")
    
    def test_palindromo_rechaza_ab(self):
        """Test palíndromo: 'ab' debe ser rechazada"""
        aceptada, historial = self.mt.reconocer_palindromo("ab")
        self.assertFalse(aceptada, "'ab' no es palíndromo")
    
    def test_palindromo_rechaza_aab(self):
        """Test palíndromo: 'aab' debe ser rechazada"""
        aceptada, historial = self.mt.reconocer_palindromo("aab")
        self.assertFalse(aceptada, "'aab' no es palíndromo")
    
    def test_palindromo_rechaza_abab(self):
        """Test palíndromo: 'abab' debe ser rechazada"""
        aceptada, historial = self.mt.reconocer_palindromo("abab")
        self.assertFalse(aceptada, "'abab' no es palíndromo")
    
    # ===== TESTS PARA L = {a^n b^2n} =====
    
    def test_anb2n_abb(self):
        """Test a^n b^2n: 'abb' debe ser aceptada (1:2)"""
        aceptada, historial = self.mt.reconocer_anb2n("abb")
        self.assertTrue(aceptada, "'abb' debe ser aceptada (1:2)")
    
    def test_anb2n_aabbbb(self):
        """Test a^n b^2n: 'aabbbb' debe ser aceptada (2:4)"""
        aceptada, historial = self.mt.reconocer_anb2n("aabbbb")
        self.assertTrue(aceptada, "'aabbbb' debe ser aceptada (2:4)")
    
    def test_anb2n_aaabbbbbb(self):
        """Test a^n b^2n: 'aaabbbbbb' debe ser aceptada (3:6)"""
        aceptada, historial = self.mt.reconocer_anb2n("aaabbbbbb")
        self.assertTrue(aceptada, "'aaabbbbbb' debe ser aceptada (3:6)")
    
    def test_anb2n_rechaza_ab(self):
        """Test a^n b^2n: 'ab' debe ser rechazada (falta 1 b)"""
        aceptada, historial = self.mt.reconocer_anb2n("ab")
        self.assertFalse(aceptada, "'ab' debe ser rechazada")
    
    def test_anb2n_rechaza_aabbb(self):
        """Test a^n b^2n: 'aabbb' debe ser rechazada (falta 1 b)"""
        aceptada, historial = self.mt.reconocer_anb2n("aabbb")
        self.assertFalse(aceptada, "'aabbb' debe ser rechazada")
    
    def test_anb2n_rechaza_abbb(self):
        """Test a^n b^2n: 'abbb' debe ser rechazada (sobra 1 b)"""
        aceptada, historial = self.mt.reconocer_anb2n("abbb")
        self.assertFalse(aceptada, "'abbb' debe ser rechazada")
    
    # ===== TESTS GENERALES =====
    
    def test_historial_generado(self):
        """Test: Verificar que se genera historial"""
        aceptada, historial = self.mt.reconocer_anbn("ab")
        self.assertGreater(len(historial), 0, "Debe generar historial")
        self.assertIn('paso', historial[0], "Cada paso debe tener número")
        self.assertIn('estado', historial[0], "Cada paso debe tener estado")
        self.assertIn('accion', historial[0], "Cada paso debe tener acción")


class TestIntegracion(unittest.TestCase):
    """Tests de integración para verificar casos especiales"""
    
    def test_aritmetica_numeros_grandes(self):
        """Test: Operaciones con números más grandes"""
        mt = MaquinaTuring()
        resultado, _ = mt.suma_unaria(10, 5)
        self.assertEqual(resultado, 15, "10+5 debe ser 15")
    
    def test_lenguajes_cadenas_largas(self):
        """Test: Cadenas más largas para verificar eficiencia"""
        mt = MaquinaTuringLenguajes()
        # a^5 b^5 c^5
        aceptada, historial = mt.reconocer_anbn("aaaaabbbbbccccc")
        self.assertTrue(aceptada, "a^5 b^5 c^5 debe ser aceptada")
        self.assertLess(len(historial), 1000, "No debe exceder límite de pasos")
    
    def test_estados_finales_correctos(self):
        """Test: Verificar estados finales correctos"""
        mt_arit = MaquinaTuring()
        mt_leng = MaquinaTuringLenguajes()
        
        # Estado de aceptación debe ser correcto
        self.assertEqual(mt_leng.estado_aceptacion, 'qaccept')
        self.assertEqual(mt_leng.estado_rechazo, 'qreject')


def run_tests():
    """Ejecutar todos los tests con reporte detallado"""
    # Crear suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Añadir tests
    suite.addTests(loader.loadTestsFromTestCase(TestMaquinaTuringAritmetica))
    suite.addTests(loader.loadTestsFromTestCase(TestMaquinaTuringLenguajes))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegracion))
    
    # Ejecutar con reporte detallado
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS - MÁQUINAS DE TURING")
    print("="*70)
    print(f"Tests ejecutados:  {result.testsRun}")
    print(f"Tests exitosos:    {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Tests fallidos:    {len(result.failures)}")
    print(f"Errores:           {len(result.errors)}")
    print("="*70)
    
    if result.wasSuccessful():
        print("✅ TODOS LOS TESTS PASARON CORRECTAMENTE")
        print("✅ LAS MÁQUINAS DE TURING FUNCIONAN PERFECTAMENTE")
        return 0
    else:
        print("❌ ALGUNOS TESTS FALLARON")
        return 1


if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)
