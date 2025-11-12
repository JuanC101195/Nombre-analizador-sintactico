"""
Test Suite para el Analizador Sintáctico Descendente

Autores:
    - Juan Esteban Cardozo Rivera
    - Juan Sebastián Gómez Usuga

Descripción:
    Suite completa de pruebas para validar el analizador sintáctico,
    incluyendo casos exitosos y de error.
"""

import unittest
import sys
import re
from datetime import datetime

# Importar solo la clase del analizador (sin interfaz gráfica)
class CalculadoraDescendente:
    def __init__(self):
        self.tokens = []
        self.posicion = 0
        self.errores = []
        self.traza_derivacion = []
        
    def analizar(self, expresion):
        """Método principal para analizar la expresión"""
        self.tokens = self.tokenizar(expresion)
        self.posicion = 0
        self.errores = []
        self.traza_derivacion = []
        
        if not self.tokens:
            return None, ["Error: Expresión vacía"]
            
        try:
            self.traza_derivacion.append("Inicio del análisis sintáctico")
            resultado = self.E()
            if self.posicion < len(self.tokens):
                tokens_restantes = ' '.join([t[1] for t in self.tokens[self.posicion:]])
                self.errores.append(f"Error de sintaxis: Caracteres adicionales después de la expresión válida: '{tokens_restantes}'")
                return None, self.errores
            self.traza_derivacion.append("✓ Análisis sintáctico completado exitosamente")
            return resultado, self.errores
        except Exception as e:
            self.errores.append(f"Error de sintaxis: {str(e)}")
            return None, self.errores
    
    def tokenizar(self, expresion):
        """Convierte la expresión en una lista de tokens"""
        patrones = [
            ('NUMERO', r'\d+(\.\d+)?'),
            ('POT', r'\*\*|\^'),
            ('MOD', r'%'),
            ('SUMA', r'\+'),
            ('RESTA', r'\-'),
            ('MULT', r'\*'),
            ('DIV', r'\/'),
            ('PAREN_IZQ', r'\('),
            ('PAREN_DER', r'\)'),
            ('ESPACIO', r'\s+'),
        ]
        
        tokens = []
        pos = 0
        
        while pos < len(expresion):
            coincide = False
            for tipo, patron in patrones:
                regex = re.compile(patron)
                match = regex.match(expresion, pos)
                if match:
                    valor = match.group()
                    if tipo != 'ESPACIO':
                        tokens.append((tipo, valor))
                    pos = match.end()
                    coincide = True
                    break
            
            if not coincide:
                self.errores.append(f"Error léxico: Caracter no válido '{expresion[pos]}' en la posición {pos}")
                self.errores.append(f"  Sugerencia: Solo se permiten números, operadores (+, -, *, /, **, ^, %) y paréntesis")
                return []
        
        return tokens
    
    def token_actual(self):
        """Retorna el token actual"""
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        return ('EOF', '')
    
    def consumir(self, tipo_esperado=None):
        """Consume el token actual y avanza a la siguiente posición"""
        if self.posicion >= len(self.tokens):
            raise Exception(f"Se esperaba '{tipo_esperado}' pero la expresión terminó inesperadamente")
            
        token_actual = self.tokens[self.posicion]
        
        if tipo_esperado and token_actual[0] != tipo_esperado:
            raise Exception(f"Se esperaba '{tipo_esperado}' pero se encontró '{token_actual[1]}'")
            
        self.posicion += 1
        return token_actual
    
    def E(self):
        """E → T E'"""
        self.traza_derivacion.append(f"  E → T E' (posición {self.posicion})")
        resultado = self.T()
        return self.E_prima(resultado)
    
    def E_prima(self, resultado_anterior):
        """E' → + T E' | - T E' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'SUMA':
            self.traza_derivacion.append(f"    E' → + T E' (sumando {resultado_anterior} + ...)")
            self.consumir('SUMA')
            resultado = resultado_anterior + self.T()
            return self.E_prima(resultado)
        elif token_actual[0] == 'RESTA':
            self.traza_derivacion.append(f"    E' → - T E' (restando {resultado_anterior} - ...)")
            self.consumir('RESTA')
            resultado = resultado_anterior - self.T()
            return self.E_prima(resultado)
        else:
            self.traza_derivacion.append(f"    E' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def T(self):
        """T → P T'"""
        self.traza_derivacion.append(f"    T → P T' (posición {self.posicion})")
        resultado = self.P()
        return self.T_prima(resultado)
    
    def T_prima(self, resultado_anterior):
        """T' → * P T' | / P T' | % P T' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'MULT':
            self.traza_derivacion.append(f"      T' → * P T' (multiplicando {resultado_anterior} * ...)")
            self.consumir('MULT')
            resultado = resultado_anterior * self.P()
            return self.T_prima(resultado)
        elif token_actual[0] == 'DIV':
            self.traza_derivacion.append(f"      T' → / P T' (dividiendo {resultado_anterior} / ...)")
            self.consumir('DIV')
            divisor = self.P()
            if divisor == 0:
                raise Exception("División por cero detectada")
            resultado = resultado_anterior / divisor
            return self.T_prima(resultado)
        elif token_actual[0] == 'MOD':
            self.traza_derivacion.append(f"      T' → % P T' (módulo {resultado_anterior} % ...)")
            self.consumir('MOD')
            divisor = self.P()
            if divisor == 0:
                raise Exception("Módulo por cero no está definido")
            resultado = resultado_anterior % divisor
            return self.T_prima(resultado)
        else:
            self.traza_derivacion.append(f"      T' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def P(self):
        """P → F P'"""
        self.traza_derivacion.append(f"      P → F P' (posición {self.posicion})")
        resultado = self.F()
        return self.P_prima(resultado)
    
    def P_prima(self, resultado_anterior):
        """P' → ** F P' | ^ F P' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'POT':
            self.traza_derivacion.append(f"        P' → ** F P' (potencia {resultado_anterior} ** ...)")
            self.consumir('POT')
            exponente = self.F()
            resultado = resultado_anterior ** exponente
            return self.P_prima(resultado)
        else:
            self.traza_derivacion.append(f"        P' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def F(self):
        """F → ( E ) | numero | -numero"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'PAREN_IZQ':
            self.traza_derivacion.append(f"        F → ( E ) (subexpresión en paréntesis)")
            self.consumir('PAREN_IZQ')
            resultado = self.E()
            self.consumir('PAREN_DER')
            return resultado
        elif token_actual[0] == 'NUMERO':
            token = self.consumir('NUMERO')
            valor = float(token[1])
            self.traza_derivacion.append(f"        F → {valor} (número)")
            return valor
        elif token_actual[0] == 'RESTA':
            self.traza_derivacion.append(f"        F → -número (número negativo)")
            self.consumir('RESTA')
            siguiente = self.token_actual()
            if siguiente[0] == 'NUMERO':
                token = self.consumir('NUMERO')
                return -float(token[1])
            elif siguiente[0] == 'PAREN_IZQ':
                return -self.F()
            else:
                raise Exception("Se esperaba un número o expresión después del signo negativo")
        else:
            if token_actual[0] == 'EOF':
                raise Exception(f"Expresión incompleta: se esperaba un número o paréntesis")
            else:
                raise Exception(f"Token inesperado '{token_actual[1]}'. Se esperaba un número o paréntesis")


class TestCalculadoraDescendente(unittest.TestCase):
    """Suite de pruebas para el analizador sintáctico"""
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.calc = CalculadoraDescendente()
    
    # ==================== PRUEBAS DE OPERACIONES BÁSICAS ====================
    
    def test_suma_simple(self):
        """Test: Suma simple"""
        resultado, errores = self.calc.analizar("2 + 3")
        self.assertEqual(resultado, 5.0)
        self.assertEqual(len(errores), 0)
    
    def test_resta_simple(self):
        """Test: Resta simple"""
        resultado, errores = self.calc.analizar("5 - 3")
        self.assertEqual(resultado, 2.0)
        self.assertEqual(len(errores), 0)
    
    def test_multiplicacion_simple(self):
        """Test: Multiplicación simple"""
        resultado, errores = self.calc.analizar("4 * 5")
        self.assertEqual(resultado, 20.0)
        self.assertEqual(len(errores), 0)
    
    def test_division_simple(self):
        """Test: División simple"""
        resultado, errores = self.calc.analizar("10 / 2")
        self.assertEqual(resultado, 5.0)
        self.assertEqual(len(errores), 0)
    
    def test_modulo_simple(self):
        """Test: Módulo simple"""
        resultado, errores = self.calc.analizar("10 % 3")
        self.assertEqual(resultado, 1.0)
        self.assertEqual(len(errores), 0)
    
    def test_potencia_simple(self):
        """Test: Potencia simple"""
        resultado, errores = self.calc.analizar("2 ** 3")
        self.assertEqual(resultado, 8.0)
        self.assertEqual(len(errores), 0)
    
    def test_potencia_con_acento(self):
        """Test: Potencia con símbolo ^"""
        resultado, errores = self.calc.analizar("2 ^ 4")
        self.assertEqual(resultado, 16.0)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS DE PRECEDENCIA ====================
    
    def test_precedencia_mult_suma(self):
        """Test: Precedencia multiplicación sobre suma"""
        resultado, errores = self.calc.analizar("2 + 3 * 4")
        self.assertEqual(resultado, 14.0)
        self.assertEqual(len(errores), 0)
    
    def test_precedencia_div_resta(self):
        """Test: Precedencia división sobre resta"""
        resultado, errores = self.calc.analizar("10 - 6 / 2")
        self.assertEqual(resultado, 7.0)
        self.assertEqual(len(errores), 0)
    
    def test_precedencia_potencia_mult(self):
        """Test: Precedencia potencia sobre multiplicación"""
        resultado, errores = self.calc.analizar("2 * 3 ** 2")
        self.assertEqual(resultado, 18.0)
        self.assertEqual(len(errores), 0)
    
    def test_precedencia_completa(self):
        """Test: Precedencia completa de operadores"""
        resultado, errores = self.calc.analizar("2 + 3 * 2 ** 2")
        self.assertEqual(resultado, 14.0)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS CON PARÉNTESIS ====================
    
    def test_parentesis_simple(self):
        """Test: Paréntesis simple"""
        resultado, errores = self.calc.analizar("(2 + 3)")
        self.assertEqual(resultado, 5.0)
        self.assertEqual(len(errores), 0)
    
    def test_parentesis_precedencia(self):
        """Test: Paréntesis cambiando precedencia"""
        resultado, errores = self.calc.analizar("(2 + 3) * 4")
        self.assertEqual(resultado, 20.0)
        self.assertEqual(len(errores), 0)
    
    def test_parentesis_anidados(self):
        """Test: Paréntesis anidados"""
        resultado, errores = self.calc.analizar("((2 + 3) * (4 - 1))")
        self.assertEqual(resultado, 15.0)
        self.assertEqual(len(errores), 0)
    
    def test_parentesis_multiples(self):
        """Test: Múltiples paréntesis"""
        resultado, errores = self.calc.analizar("(2 + 3) * (4 + 5)")
        self.assertEqual(resultado, 45.0)
        self.assertEqual(len(errores), 0)
    
    def test_parentesis_complejos(self):
        """Test: Paréntesis complejos"""
        resultado, errores = self.calc.analizar("((2 + 3) * (4 - 1)) / 2")
        self.assertEqual(resultado, 7.5)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS CON NÚMEROS DECIMALES ====================
    
    def test_decimal_simple(self):
        """Test: Número decimal simple"""
        resultado, errores = self.calc.analizar("3.5")
        self.assertEqual(resultado, 3.5)
        self.assertEqual(len(errores), 0)
    
    def test_operacion_decimales(self):
        """Test: Operación con decimales"""
        resultado, errores = self.calc.analizar("3.5 + 2.5")
        self.assertEqual(resultado, 6.0)
        self.assertEqual(len(errores), 0)
    
    def test_multiplicacion_decimales(self):
        """Test: Multiplicación con decimales"""
        resultado, errores = self.calc.analizar("2.5 * 4")
        self.assertEqual(resultado, 10.0)
        self.assertEqual(len(errores), 0)
    
    def test_division_decimales(self):
        """Test: División con decimales"""
        resultado, errores = self.calc.analizar("7.5 / 2.5")
        self.assertEqual(resultado, 3.0)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS CON NÚMEROS NEGATIVOS ====================
    
    def test_numero_negativo(self):
        """Test: Número negativo simple"""
        resultado, errores = self.calc.analizar("-5")
        self.assertEqual(resultado, -5.0)
        self.assertEqual(len(errores), 0)
    
    def test_suma_con_negativo(self):
        """Test: Suma con número negativo"""
        resultado, errores = self.calc.analizar("-5 + 3")
        self.assertEqual(resultado, -2.0)
        self.assertEqual(len(errores), 0)
    
    def test_multiplicacion_negativo(self):
        """Test: Multiplicación con negativo"""
        resultado, errores = self.calc.analizar("-5 * 3")
        self.assertEqual(resultado, -15.0)
        self.assertEqual(len(errores), 0)
    
    def test_parentesis_negativo(self):
        """Test: Paréntesis con negativo"""
        resultado, errores = self.calc.analizar("-(5 + 3)")
        self.assertEqual(resultado, -8.0)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS COMPLEJAS ====================
    
    def test_expresion_compleja_1(self):
        """Test: Expresión compleja 1"""
        resultado, errores = self.calc.analizar("2 + 3 * 4 - 5")
        self.assertEqual(resultado, 9.0)
        self.assertEqual(len(errores), 0)
    
    def test_expresion_compleja_2(self):
        """Test: Expresión compleja 2"""
        resultado, errores = self.calc.analizar("10 / 2 + 8 * 3")
        self.assertEqual(resultado, 29.0)
        self.assertEqual(len(errores), 0)
    
    def test_expresion_compleja_3(self):
        """Test: Expresión compleja 3"""
        resultado, errores = self.calc.analizar("2 ** 3 + 10 % 3 * 2")
        self.assertEqual(resultado, 10.0)
        self.assertEqual(len(errores), 0)
    
    def test_expresion_muy_compleja(self):
        """Test: Expresión muy compleja"""
        resultado, errores = self.calc.analizar("(2 + 3) * 4 - 10 / 2 + 3 ** 2")
        self.assertEqual(resultado, 24.0)
        self.assertEqual(len(errores), 0)
    
    # ==================== PRUEBAS DE ERRORES ====================
    
    def test_error_division_cero(self):
        """Test: Error división por cero"""
        resultado, errores = self.calc.analizar("10 / 0")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
        self.assertIn("División por cero", errores[0])
    
    def test_error_modulo_cero(self):
        """Test: Error módulo por cero"""
        resultado, errores = self.calc.analizar("10 % 0")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
        self.assertIn("Módulo por cero", errores[0])
    
    def test_error_caracter_invalido(self):
        """Test: Error caracter inválido"""
        resultado, errores = self.calc.analizar("2 + @")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
        # Los errores léxicos retornan lista vacía de tokens, luego expresión vacía
        self.assertTrue(any("Error léxico" in err or "vacía" in err for err in errores))
    
    def test_error_parentesis_desbalanceados_1(self):
        """Test: Error paréntesis sin cerrar"""
        resultado, errores = self.calc.analizar("(2 + 3")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
    
    def test_error_parentesis_desbalanceados_2(self):
        """Test: Error paréntesis extra"""
        resultado, errores = self.calc.analizar("2 + 3)")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
    
    def test_error_expresion_vacia(self):
        """Test: Error expresión vacía"""
        resultado, errores = self.calc.analizar("")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
        self.assertIn("vacía", errores[0])
    
    def test_error_operador_solo(self):
        """Test: Error operador sin operandos"""
        resultado, errores = self.calc.analizar("+")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
    
    def test_error_dos_operadores(self):
        """Test: Error dos operadores seguidos"""
        resultado, errores = self.calc.analizar("2 + * 3")
        self.assertIsNone(resultado)
        self.assertGreater(len(errores), 0)
    
    # ==================== PRUEBAS DE TOKENIZACIÓN ====================
    
    def test_tokenizacion_basica(self):
        """Test: Tokenización básica"""
        tokens = self.calc.tokenizar("2 + 3")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0][0], 'NUMERO')
        self.assertEqual(tokens[1][0], 'SUMA')
        self.assertEqual(tokens[2][0], 'NUMERO')
    
    def test_tokenizacion_compleja(self):
        """Test: Tokenización compleja"""
        tokens = self.calc.tokenizar("2 ** 3 + 10 % 3")
        self.assertEqual(len(tokens), 7)
        tipos = [t[0] for t in tokens]
        self.assertIn('POT', tipos)
        self.assertIn('MOD', tipos)
    
    def test_tokenizacion_parentesis(self):
        """Test: Tokenización con paréntesis"""
        tokens = self.calc.tokenizar("(2 + 3)")
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0][0], 'PAREN_IZQ')
        self.assertEqual(tokens[4][0], 'PAREN_DER')
    
    # ==================== PRUEBAS DE CASOS EXTREMOS ====================
    
    def test_espacios_multiples(self):
        """Test: Espacios múltiples"""
        resultado, errores = self.calc.analizar("2    +     3")
        self.assertEqual(resultado, 5.0)
        self.assertEqual(len(errores), 0)
    
    def test_sin_espacios(self):
        """Test: Sin espacios"""
        resultado, errores = self.calc.analizar("2+3*4")
        self.assertEqual(resultado, 14.0)
        self.assertEqual(len(errores), 0)
    
    def test_numero_grande(self):
        """Test: Números grandes"""
        resultado, errores = self.calc.analizar("1000 + 2000")
        self.assertEqual(resultado, 3000.0)
        self.assertEqual(len(errores), 0)
    
    def test_muchas_operaciones(self):
        """Test: Muchas operaciones encadenadas"""
        resultado, errores = self.calc.analizar("1 + 2 + 3 + 4 + 5")
        self.assertEqual(resultado, 15.0)
        self.assertEqual(len(errores), 0)
    
    def test_potencias_encadenadas(self):
        """Test: Potencias encadenadas"""
        resultado, errores = self.calc.analizar("2 ** 2 ** 2")
        self.assertEqual(resultado, 16.0)
        self.assertEqual(len(errores), 0)


def run_tests():
    """Ejecuta todas las pruebas y genera un reporte"""
    print("=" * 80)
    print("SUITE DE PRUEBAS - ANALIZADOR SINTÁCTICO DESCENDENTE")
    print("Autores: Juan Esteban Cardozo Rivera • Juan Sebastián Gómez Usuga")
    print("=" * 80)
    print()
    
    # Crear suite de pruebas
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculadoraDescendente)
    
    # Ejecutar pruebas con reporte detallado
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Resumen final
    print()
    print("=" * 80)
    print("RESUMEN DE PRUEBAS")
    print("=" * 80)
    print(f"Total de pruebas ejecutadas: {result.testsRun}")
    print(f"✓ Pruebas exitosas: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"✗ Pruebas fallidas: {len(result.failures)}")
    print(f"✗ Errores: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE! 🎉")
        print("El analizador sintáctico está funcionando correctamente.")
    else:
        print("⚠️  ALGUNAS PRUEBAS FALLARON")
        print("Revise los errores anteriores para más detalles.")
    
    print("=" * 80)
    print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
