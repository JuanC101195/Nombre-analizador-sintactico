from analizador_ascendente import AnalizadorAscendente

a = AnalizadorAscendente()
resultado, datos = a.analizar('var = 5')

print("=" * 70)
print("TRAZA DEL ANÁLISIS")
print("=" * 70)

if isinstance(datos, list) and len(datos) > 0:
    if isinstance(datos[0], dict):
        for d in datos:
            print(f"Paso {d['paso']}: Pila={d['pila']}, Entrada={d['entrada']}")
            print(f"           Acción: {d['accion']}")
            print()
    else:
        # Son errores
        print("ERRORES:")
        for error in datos:
            print(f"  - {error}")

print(f"\nResultado final: {resultado}")
print(f"Pila final: {a.pila}")
