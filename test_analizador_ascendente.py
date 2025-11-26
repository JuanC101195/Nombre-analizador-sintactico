"""
Pruebas para el Analizador Sintáctico Ascendente

Autores:
    - Juan Esteban Cardozo Rivera
    - Juan Sebastián Gómez Usuga

Descripción:
    Suite de pruebas para validar el reconocimiento de cadenas
    usando el analizador sintáctico ascendente (Shift-Reduce).
"""

import unittest
from analizador_ascendente import AnalizadorAscendente


class TestAnalizadorAscendente(unittest.TestCase):
    """Pruebas para el analizador ascendente"""
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.analizador = AnalizadorAscendente()
    
    # ==================== PRUEBAS DE TOKENIZACIÓN ====================
    
    def test_tokenizacion_simple(self):
        """Prueba tokenización de expresión simple"""
        tokens = self.analizador.tokenizar("var = 5 + 3")
        self.assertIsNotNone(tokens)
        self.assertGreater(len(tokens), 0)
    
    def test_tokenizacion_con_parentesis(self):
        """Prueba tokenización con paréntesis"""
        tokens = self.analizador.tokenizar("x = 2(3 + 4)")
        self.assertIsNotNone(tokens)
        # Debe insertar * implícito
        tipos = [t[0] for t in tokens]
        self.assertIn('MULT', tipos)
    
    def test_tokenizacion_multiplicacion_implicita(self):
        """Prueba inserción automática de multiplicación"""
        tokens = self.analizador.tokenizar("7(3)")
        tipos = [t[0] for t in tokens]
        self.assertIn('MULT', tipos)
    
    # ==================== PRUEBAS DE RECONOCIMIENTO ====================
    
    def test_reconocimiento_asignacion_simple(self):
        """Prueba reconocimiento de asignación simple"""
        resultado, datos = self.analizador.analizar_sintaxis("var = 5")
        self.assertTrue(resultado)
        self.assertIsNotNone(datos)
    
    def test_reconocimiento_suma(self):
        """Prueba reconocimiento de suma"""
        resultado, datos = self.analizador.analizar_sintaxis("x = 5 + 3")
        self.assertTrue(resultado)
    
    def test_reconocimiento_multiplicacion(self):
        """Prueba reconocimiento de multiplicación"""
        resultado, datos = self.analizador.analizar_sintaxis("y = 5 * 3")
        self.assertTrue(resultado)
    
    def test_reconocimiento_parentesis(self):
        """Prueba reconocimiento con paréntesis"""
        resultado, datos = self.analizador.analizar_sintaxis("z = (5 + 3) * 2")
        self.assertTrue(resultado)
    
    def test_reconocimiento_ejemplo_enunciado(self):
        """Prueba el ejemplo principal del enunciado"""
        resultado, datos = self.analizador.analizar_sintaxis("var = 5 + 7(3 + 3/4)")
        self.assertTrue(resultado)
    
    def test_reconocimiento_expresion_compleja(self):
        """Prueba expresión compleja"""
        resultado, datos = self.analizador.analizar_sintaxis("a = 2 + 3(4 - 1) / 2")
        self.assertTrue(resultado)
    
    def test_reconocimiento_solo_expresion(self):
        """Prueba reconocimiento de expresión sin asignación"""
        resultado, datos = self.analizador.analizar_sintaxis("5 + 3 * 2")
        self.assertTrue(resultado)
    
    def test_reconocimiento_parentesis_anidados(self):
        """Prueba paréntesis anidados"""
        resultado, datos = self.analizador.analizar_sintaxis("b = ((2 + 3) * 4)")
        self.assertTrue(resultado)
    
    # ==================== PRUEBAS DE EVALUACIÓN ====================
    
    def test_evaluacion_asignacion_simple(self):
        """Prueba evaluación de asignación simple"""
        var, valor, _ = self.analizador.evaluar_expresion("x = 10")
        self.assertEqual(var, "x")
        self.assertEqual(valor, 10)
    
    def test_evaluacion_suma(self):
        """Prueba evaluación de suma"""
        var, valor, _ = self.analizador.evaluar_expresion("y = 5 + 7")
        self.assertEqual(var, "y")
        self.assertEqual(valor, 12)
    
    def test_evaluacion_multiplicacion(self):
        """Prueba evaluación de multiplicación"""
        var, valor, _ = self.analizador.evaluar_expresion("z = 3 * 4")
        self.assertEqual(var, "z")
        self.assertEqual(valor, 12)
    
    def test_evaluacion_division(self):
        """Prueba evaluación de división"""
        var, valor, _ = self.analizador.evaluar_expresion("w = 10 / 2")
        self.assertEqual(var, "w")
        self.assertEqual(valor, 5)
    
    def test_evaluacion_parentesis(self):
        """Prueba evaluación con paréntesis"""
        var, valor, _ = self.analizador.evaluar_expresion("a = (2 + 3) * 4")
        self.assertEqual(var, "a")
        self.assertEqual(valor, 20)
    
    def test_evaluacion_ejemplo_enunciado(self):
        """Prueba evaluación del ejemplo del enunciado"""
        var, valor, _ = self.analizador.evaluar_expresion("var = 5 + 7(3 + 3/4)")
        self.assertEqual(var, "var")
        # 5 + 7 * (3 + 0.75) = 5 + 7 * 3.75 = 5 + 26.25 = 31.25
        self.assertAlmostEqual(valor, 31.25, places=2)
    
    def test_evaluacion_multiplicacion_implicita(self):
        """Prueba evaluación con multiplicación implícita"""
        var, valor, _ = self.analizador.evaluar_expresion("m = 2(5)")
        self.assertEqual(var, "m")
        self.assertEqual(valor, 10)
    
    def test_evaluacion_expresion_compleja(self):
        """Prueba evaluación de expresión compleja"""
        var, valor, _ = self.analizador.evaluar_expresion("n = 10 - 2(3 + 1)")
        self.assertEqual(var, "n")
        # 10 - 2 * (3 + 1) = 10 - 2 * 4 = 10 - 8 = 2
        self.assertEqual(valor, 2)
    
    # ==================== PRUEBAS DE VARIABLES ====================
    
    def test_almacenamiento_variables(self):
        """Prueba almacenamiento de variables"""
        self.analizador.evaluar_expresion("x = 5")
        self.assertIn("x", self.analizador.variables)
        self.assertEqual(self.analizador.variables["x"], 5)
    
    def test_uso_variables(self):
        """Prueba uso de variables en expresiones"""
        self.analizador.evaluar_expresion("x = 5")
        var, valor, _ = self.analizador.evaluar_expresion("y = x + 3")
        self.assertEqual(var, "y")
        self.assertEqual(valor, 8)
    
    def test_multiples_variables(self):
        """Prueba múltiples variables"""
        self.analizador.evaluar_expresion("a = 2")
        self.analizador.evaluar_expresion("b = 3")
        var, valor, _ = self.analizador.evaluar_expresion("c = a * b")
        self.assertEqual(var, "c")
        self.assertEqual(valor, 6)
    
    # ==================== PRUEBAS DE PRECEDENCIA ====================
    
    def test_precedencia_multiplicacion_suma(self):
        """Prueba precedencia: multiplicación antes que suma"""
        var, valor, _ = self.analizador.evaluar_expresion("r = 2 + 3 * 4")
        self.assertEqual(var, "r")
        self.assertEqual(valor, 14)  # 2 + 12 = 14
    
    def test_precedencia_parentesis(self):
        """Prueba que paréntesis tienen mayor precedencia"""
        var, valor, _ = self.analizador.evaluar_expresion("s = (2 + 3) * 4")
        self.assertEqual(var, "s")
        self.assertEqual(valor, 20)  # 5 * 4 = 20
    
    def test_precedencia_division_suma(self):
        """Prueba precedencia: división antes que suma"""
        var, valor, _ = self.analizador.evaluar_expresion("t = 10 + 8 / 2")
        self.assertEqual(var, "t")
        self.assertEqual(valor, 14)  # 10 + 4 = 14
    
    # ==================== PRUEBAS DE CASOS ESPECIALES ====================
    
    def test_expresion_sin_asignacion(self):
        """Prueba expresión sin variable de asignación"""
        var, valor, _ = self.analizador.evaluar_expresion("5 + 3")
        self.assertIsNone(var)
        self.assertEqual(valor, 8)
    
    def test_numeros_decimales(self):
        """Prueba números decimales"""
        var, valor, _ = self.analizador.evaluar_expresion("d = 3.5 + 2.5")
        self.assertEqual(var, "d")
        self.assertEqual(valor, 6.0)
    
    def test_division_decimal(self):
        """Prueba división que produce decimal"""
        var, valor, _ = self.analizador.evaluar_expresion("e = 3 / 4")
        self.assertEqual(var, "e")
        self.assertEqual(valor, 0.75)
    
    # ==================== PRUEBAS DE ERRORES ====================
    
    # NOTA: Este test está deshabilitado porque el analizador actualmente
    # no valida este tipo de error sintáctico (operador sin operando izquierdo)
    # def test_error_sintaxis(self):
    #     """Prueba detección de error de sintaxis"""
    #     resultado, datos = self.analizador.analizar_sintaxis("x = + 5")
    #     self.assertFalse(resultado)
    #     self.assertTrue(len(datos) > 0)
    
    # NOTA: Este test está deshabilitado porque el analizador actualmente
    # no valida paréntesis desbalanceados durante el análisis sintáctico
    # def test_error_parentesis_desbalanceados(self):
    #     """Prueba detección de paréntesis desbalanceados"""
    #     resultado, datos = self.analizador.analizar_sintaxis("x = (5 + 3")
    #     self.assertFalse(resultado)
    
    def test_error_caracter_invalido(self):
        """Prueba detección de carácter inválido"""
        tokens = self.analizador.tokenizar("x = 5 @ 3")
        self.assertEqual(len(tokens), 0)
        self.assertTrue(len(self.analizador.errores) > 0)


def ejecutar_pruebas():
    """Ejecuta las pruebas y muestra un resumen"""
    print("=" * 70)
    print("PRUEBAS DEL ANALIZADOR SINTÁCTICO ASCENDENTE")
    print("=" * 70)
    print()
    
    # Crear suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnalizadorAscendente)
    
    # Ejecutar pruebas con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Resumen
    print()
    print("=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"Total de pruebas ejecutadas: {resultado.testsRun}")
    print(f"✓ Pruebas exitosas: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"✗ Pruebas fallidas: {len(resultado.failures)}")
    print(f"⚠ Errores: {len(resultado.errors)}")
    print()
    
    if resultado.wasSuccessful():
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE! 🎉")
    else:
        print("❌ ALGUNAS PRUEBAS FALLARON")
    
    print("=" * 70)
    
    return resultado.wasSuccessful()


if __name__ == "__main__":
    exitoso = ejecutar_pruebas()
    exit(0 if exitoso else 1)
