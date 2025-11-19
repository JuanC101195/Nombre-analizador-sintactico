"""
Test Suite para Analizador Sintáctico Ascendente - VERSIÓN FUNCIONAL

Pruebas completas para verificar el correcto funcionamiento del analizador.
"""

import unittest
from analizador_ascendente import AnalizadorAscendente


class TestAnalizadorFuncional(unittest.TestCase):
    """Pruebas unitarias para el analizador ascendente funcional"""
    
    def setUp(self):
        """Prepara el analizador para cada prueba"""
        self.analizador = AnalizadorAscendente()
    
    # ==========================================
    # PRUEBAS DE TOKENIZACIÓN
    # ==========================================
    
    def test_tokenizacion_simple(self):
        """Prueba tokenización básica"""
        tokens = self.analizador.tokenizar("var = 5")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0], ('VAR', 'var'))
        self.assertEqual(tokens[1], ('IGUAL', '='))
        self.assertEqual(tokens[2], ('NUMERO', '5'))
    
    def test_tokenizacion_multiplicacion_implicita(self):
        """Prueba inserción automática de multiplicación"""
        tokens = self.analizador.tokenizar("7(3)")
        tipos = [t[0] for t in tokens]
        # Debe tener MULT entre NUMERO y PAREN_IZQ
        self.assertIn('MULT', tipos)
        self.assertTrue(tokens[1][0] == 'MULT')
    
    def test_tokenizacion_con_parentesis(self):
        """Prueba tokenización con paréntesis"""
        tokens = self.analizador.tokenizar("x = 2(3 + 4)")
        tipos = [t[0] for t in tokens]
        self.assertIn('MULT', tipos)  # Debe insertar * implícito
        self.assertIn('PAREN_IZQ', tipos)
        self.assertIn('PAREN_DER', tipos)
    
    def test_numeros_decimales(self):
        """Prueba números decimales"""
        tokens = self.analizador.tokenizar("x = 3.14")
        self.assertEqual(tokens[2], ('NUMERO', '3.14'))
    
    def test_error_caracter_invalido(self):
        """Prueba detección de carácter inválido"""
        tokens = self.analizador.tokenizar("x = 5 @ 3")
        self.assertEqual(len(tokens), 0)
        self.assertTrue(len(self.analizador.errores) > 0)
    
    # ==========================================
    # PRUEBAS DE RECONOCIMIENTO SINTÁCTICO
    # ==========================================
    
    def test_reconocimiento_asignacion_simple(self):
        """Prueba reconocimiento de asignación simple"""
        resultado, traza = self.analizador.analizar_sintaxis("var = 5")
        self.assertTrue(resultado)
        self.assertIsInstance(traza, list)
        self.assertTrue(len(traza) > 0)
    
    def test_reconocimiento_ejemplo_enunciado(self):
        """Prueba el ejemplo principal del enunciado"""
        resultado, traza = self.analizador.analizar_sintaxis("var = 5 + 7(3 + 3/4)")
        self.assertTrue(resultado)
        self.assertIsInstance(traza, list)
    
    def test_reconocimiento_expresion_compleja(self):
        """Prueba expresión compleja"""
        resultado, traza = self.analizador.analizar_sintaxis("a = 2 + 3(4 - 1) / 2")
        self.assertTrue(resultado)
    
    def test_reconocimiento_solo_expresion(self):
        """Prueba reconocimiento de expresión sin asignación"""
        resultado, traza = self.analizador.analizar_sintaxis("5 + 3 * 2")
        self.assertTrue(resultado)
    
    def test_reconocimiento_parentesis_anidados(self):
        """Prueba paréntesis anidados"""
        resultado, traza = self.analizador.analizar_sintaxis("b = ((2 + 3) * 4)")
        self.assertTrue(resultado)
    
    # ==========================================
    # PRUEBAS DE EVALUACIÓN
    # ==========================================
    
    def test_evaluacion_asignacion_simple(self):
        """Prueba evaluación de asignación simple"""
        var, valor, _ = self.analizador.evaluar_expresion("x = 10")
        self.assertEqual(var, 'x')
        self.assertEqual(valor, 10)
        self.assertEqual(self.analizador.variables['x'], 10)
    
    def test_evaluacion_ejemplo_enunciado(self):
        """Prueba evaluación del ejemplo del enunciado"""
        var, valor, _ = self.analizador.evaluar_expresion("var = 5 + 7(3 + 3/4)")
        # 5 + 7*(3 + 0.75) = 5 + 7*3.75 = 5 + 26.25 = 31.25
        self.assertEqual(var, 'var')
        self.assertAlmostEqual(valor, 31.25, places=2)
    
    def test_evaluacion_suma(self):
        """Prueba evaluación de suma"""
        _, valor, _ = self.analizador.evaluar_expresion("5 + 3")
        self.assertEqual(valor, 8)
    
    def test_evaluacion_multiplicacion(self):
        """Prueba evaluación de multiplicación"""
        _, valor, _ = self.analizador.evaluar_expresion("5 * 3")
        self.assertEqual(valor, 15)
    
    def test_evaluacion_division(self):
        """Prueba evaluación de división"""
        _, valor, _ = self.analizador.evaluar_expresion("10 / 2")
        self.assertEqual(valor, 5)
    
    def test_evaluacion_parentesis(self):
        """Prueba evaluación con paréntesis"""
        _, valor, _ = self.analizador.evaluar_expresion("(5 + 3) * 2")
        self.assertEqual(valor, 16)
    
    def test_evaluacion_multiplicacion_implicita(self):
        """Prueba evaluación con multiplicación implícita"""
        _, valor, _ = self.analizador.evaluar_expresion("2(3 + 4)")
        self.assertEqual(valor, 14)
    
    def test_evaluacion_expresion_compleja(self):
        """Prueba evaluación de expresión compleja"""
        var, valor, _ = self.analizador.evaluar_expresion("a = 2 + 3(4 - 1) / 2")
        # 2 + 3*(4-1)/2 = 2 + 3*3/2 = 2 + 9/2 = 2 + 4.5 = 6.5
        self.assertEqual(var, 'a')
        self.assertAlmostEqual(valor, 6.5, places=1)
    
    def test_division_decimal(self):
        """Prueba división que produce decimal"""
        _, valor, _ = self.analizador.evaluar_expresion("10 / 4")
        self.assertEqual(valor, 2.5)
    
    # ==========================================
    # PRUEBAS DE PRECEDENCIA
    # ==========================================
    
    def test_precedencia_multiplicacion_suma(self):
        """Prueba precedencia: multiplicación antes que suma"""
        _, valor, _ = self.analizador.evaluar_expresion("2 + 3 * 4")
        self.assertEqual(valor, 14)  # 2 + 12 = 14, NO (2 + 3) * 4 = 20
    
    def test_precedencia_division_suma(self):
        """Prueba precedencia: división antes que suma"""
        _, valor, _ = self.analizador.evaluar_expresion("10 + 8 / 2")
        self.assertEqual(valor, 14)  # 10 + 4 = 14
    
    def test_precedencia_parentesis(self):
        """Prueba que paréntesis tienen mayor precedencia"""
        _, valor, _ = self.analizador.evaluar_expresion("(2 + 3) * 4")
        self.assertEqual(valor, 20)
    
    # ==========================================
    # PRUEBAS DE VARIABLES
    # ==========================================
    
    def test_almacenamiento_variables(self):
        """Prueba almacenamiento de variables"""
        self.analizador.evaluar_expresion("x = 10")
        self.analizador.evaluar_expresion("y = 20")
        self.assertEqual(self.analizador.variables['x'], 10)
        self.assertEqual(self.analizador.variables['y'], 20)
    
    def test_uso_variables(self):
        """Prueba uso de variables en expresiones"""
        self.analizador.evaluar_expresion("x = 5")
        self.analizador.evaluar_expresion("y = 3")
        _, valor, _ = self.analizador.evaluar_expresion("z = x + y")
        self.assertEqual(valor, 8)
    
    def test_multiples_variables(self):
        """Prueba múltiples variables"""
        self.analizador.evaluar_expresion("x = 10")
        _, valor, _ = self.analizador.evaluar_expresion("result = x * 2")
        self.assertEqual(valor, 20)
    
    # ==========================================
    # PRUEBAS DE TRAZA SHIFT-REDUCE
    # ==========================================
    
    def test_traza_contiene_shift(self):
        """Verifica que la traza contiene operaciones SHIFT"""
        _, traza = self.analizador.analizar_sintaxis("x = 5")
        acciones = [paso['accion'] for paso in traza]
        tiene_shift = any('SHIFT' in accion for accion in acciones)
        self.assertTrue(tiene_shift)
    
    def test_traza_contiene_reduce(self):
        """Verifica que la traza contiene operaciones REDUCE"""
        _, traza = self.analizador.analizar_sintaxis("x = 5")
        acciones = [paso['accion'] for paso in traza]
        tiene_reduce = any('REDUCE' in accion for accion in acciones)
        self.assertTrue(tiene_reduce)
    
    def test_traza_termina_aceptar(self):
        """Verifica que la traza termina en ACEPTAR"""
        _, traza = self.analizador.analizar_sintaxis("x = 5")
        ultima_accion = traza[-1]['accion']
        self.assertIn('ACEPTAR', ultima_accion)
    
    def test_traza_pila_inicial(self):
        """Verifica que la pila inicial contiene $"""
        _, traza = self.analizador.analizar_sintaxis("x = 5")
        pila_inicial = traza[0]['pila']
        self.assertEqual(pila_inicial[0], '$')


def run_tests():
    """Ejecuta las pruebas con salida formateada"""
    print("=" * 70)
    print("PRUEBAS DEL ANALIZADOR SINTÁCTICO ASCENDENTE - VERSIÓN FUNCIONAL")
    print("=" * 70)
    print()
    
    # Crear suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnalizadorFuncional)
    
    # Ejecutar con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen
    print()
    print("=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"Total de pruebas ejecutadas: {result.testsRun}")
    print(f"✓ Pruebas exitosas: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"✗ Pruebas fallidas: {len(result.failures)}")
    print(f"⚠ Errores: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    else:
        print("❌ ALGUNAS PRUEBAS FALLARON")
    
    print("=" * 70)
    print()
    
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit(run_tests())
