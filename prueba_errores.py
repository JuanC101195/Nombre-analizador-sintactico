"""
Pruebas de Manejo de Errores
Verifica que todos los errores se detecten correctamente
"""

from programa import CalculadoraDescendente

def test_errores():
    """Pruebas de detección de errores"""
    calc = CalculadoraDescendente()
    
    print("=" * 70)
    print("PRUEBAS DE MANEJO DE ERRORES")
    print("=" * 70)
    print()
    
    pruebas_error = [
        ("10 / 0", "división por cero"),
        ("10 % 0", "módulo por cero"),
        ("2 + @", "caracter inválido"),
        ("(2 + 3", "paréntesis sin cerrar"),
        ("2 + 3)", "paréntesis extra"),
        ("", "expresión vacía"),
        ("+", "operador sin operandos"),
        ("2 + * 3", "dos operadores seguidos"),
        ("2 +", "expresión incompleta"),
        ("* 3", "comienza con operador"),
    ]
    
    exitosas = 0
    fallidas = 0
    
    for expresion, descripcion in pruebas_error:
        resultado, errores = calc.analizar(expresion)
        
        if resultado is None and len(errores) > 0:
            print(f"✅ Error detectado correctamente: {descripcion}")
            print(f"   Expresión: '{expresion}'")
            print(f"   Mensaje: {errores[0][:60]}...")
            exitosas += 1
        else:
            print(f"❌ Error NO detectado: {descripcion}")
            print(f"   Expresión: '{expresion}'")
            print(f"   Resultado inesperado: {resultado}")
            fallidas += 1
        print()
    
    print("=" * 70)
    print(f"Resultado: {exitosas} errores detectados correctamente, {fallidas} fallidas")
    
    if fallidas == 0:
        print("🎉 ¡TODOS LOS ERRORES SE MANEJAN CORRECTAMENTE! 🎉")
        print("El sistema de validación está funcionando perfectamente.")
    else:
        print("⚠️ Algunos errores no se detectaron")
    
    print("=" * 70)
    
    return fallidas == 0

if __name__ == "__main__":
    import sys
    success = test_errores()
    sys.exit(0 if success else 1)
