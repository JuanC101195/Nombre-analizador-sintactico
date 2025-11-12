"""
Script de Pruebas Rápidas - Verificación Final
Ejecuta pruebas básicas sin interfaz gráfica
"""

from programa import CalculadoraDescendente

def test_rapido():
    """Pruebas rápidas para verificar funcionamiento"""
    calc = CalculadoraDescendente()
    
    print("=" * 70)
    print("PRUEBAS RÁPIDAS - VERIFICACIÓN FINAL")
    print("=" * 70)
    print()
    
    pruebas = [
        ("2 + 3", 5.0),
        ("2 * 3 + 4", 10.0),
        ("(2 + 3) * 4", 20.0),
        ("2 ** 3", 8.0),
        ("10 % 3", 1.0),
        ("2.5 * 4", 10.0),
        ("-5 + 3", -2.0),
        ("2 + 3 * 2 ** 2", 14.0),
    ]
    
    exitosas = 0
    fallidas = 0
    
    for expresion, esperado in pruebas:
        resultado, errores = calc.analizar(expresion)
        
        if resultado is not None and abs(resultado - esperado) < 0.0001:
            print(f"✅ {expresion:20} = {resultado:8.2f} (Esperado: {esperado:8.2f})")
            exitosas += 1
        else:
            print(f"❌ {expresion:20} = {resultado} (Esperado: {esperado})")
            if errores:
                print(f"   Errores: {errores}")
            fallidas += 1
    
    print()
    print("=" * 70)
    print(f"Resultado: {exitosas} exitosas, {fallidas} fallidas")
    
    if fallidas == 0:
        print("🎉 ¡TODAS LAS PRUEBAS RÁPIDAS PASARON! 🎉")
        print("El programa está listo para usar.")
    else:
        print("⚠️ Algunas pruebas fallaron")
    
    print("=" * 70)
    
    return fallidas == 0

if __name__ == "__main__":
    import sys
    success = test_rapido()
    sys.exit(0 if success else 1)
