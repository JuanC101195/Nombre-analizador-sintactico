# Analizador Sintáctico Ascendente (Bottom-Up Parser)

## Autores
- Juan Esteban Cardozo Rivera
- Juan Sebastián Gómez Usuga

## Descripción

Este proyecto implementa un **analizador sintáctico ascendente** usando el algoritmo **Shift-Reduce** para reconocer y evaluar expresiones con asignaciones de variables.

## Características

### ✨ Funcionalidades Principales

- ✅ **Análisis Ascendente (Bottom-Up)**: Construcción del árbol desde las hojas hacia la raíz
- ✅ **Algoritmo Shift-Reduce**: Implementación de operaciones SHIFT y REDUCE
- ✅ **Asignaciones de Variables**: Soporte para `var = expresión`
- ✅ **Operadores Aritméticos**: +, -, *, /, paréntesis
- ✅ **Multiplicación Implícita**: `7(3)` se interpreta como `7*(3)`
- ✅ **Interfaz Gráfica**: Visualización completa del proceso
- ✅ **Traza Completa**: Muestra cada paso del análisis Shift-Reduce

### 📐 Gramática Implementada

```
S  → VAR = E          (Asignación)
E  → E + T            (Suma)
E  → E - T            (Resta)
E  → T                (Término)
T  → T * F            (Multiplicación)
T  → T / F            (División)
T  → F                (Factor)
F  → ( E )            (Paréntesis)
F  → número           (Número)
F  → VAR              (Variable)
```

### 🔄 Operaciones Shift-Reduce

- **SHIFT**: Empuja el token actual a la pila
- **REDUCE**: Reemplaza símbolos del tope de la pila por un no terminal
- **ACCEPT**: La cadena es reconocida exitosamente
- **ERROR**: La cadena no pertenece al lenguaje

## 🚀 Uso

### Ejecutar el Programa

```bash
python analizador_ascendente.py
```

### Ejemplos de Expresiones

1. **Ejemplo del enunciado**: `var = 5 + 7(3 + 3/4)`
2. **Asignación simple**: `x = 10 + 5`
3. **Multiplicación implícita**: `y = 2(3 + 4)`
4. **Con paréntesis**: `z = (5 + 3) * 2`
5. **Expresión compleja**: `a = 2 + 3(4 - 1) / 2`

## 📊 Interfaz Gráfica

La interfaz incluye 4 pestañas:

1. **Resultado**: Muestra el resultado de la evaluación y el estado del análisis
2. **Traza Shift-Reduce**: Tabla detallada con cada paso del análisis
3. **Tokens**: Lista de tokens identificados en el análisis léxico
4. **Gramática**: Documentación de la gramática utilizada

## 🧪 Pruebas

Ejecutar las pruebas:

```bash
python test_analizador_ascendente.py
```

Las pruebas incluyen:
- Tokenización y análisis léxico
- Reconocimiento de sintaxis
- Evaluación de expresiones
- Manejo de variables
- Precedencia de operadores
- Detección de errores

## 📝 Notas Técnicas

### Diferencias con el Analizador Descendente

| Aspecto | Descendente | Ascendente |
|---------|-------------|------------|
| **Dirección** | Top-Down | Bottom-Up |
| **Construcción** | Raíz → Hojas | Hojas → Raíz |
| **Algoritmo** | Recursivo | Shift-Reduce |
| **Predicción** | Usa lookahead para decidir | Reduce cuando encuentra patrón |
| **Gramática** | LL(1) | LR |

### Multiplicación Implícita

El analizador automáticamente inserta el operador de multiplicación (`*`) en los siguientes casos:

- `número(expresión)` → `número*(expresión)`
- `)número` → `)*número`
- `)(` → `)*(`
- `número variable` → `número*variable`

## 🛠️ Estructura del Proyecto

```
Lab2/
├── analizador_ascendente.py          # Programa principal
├── test_analizador_ascendente.py     # Suite de pruebas
├── debug_ascendente.py                # Script de depuración
└── README_ASCENDENTE.md               # Este archivo
```

## 📚 Recursos

- [Teoría de Compiladores](https://en.wikipedia.org/wiki/LR_parser)
- [Algoritmo Shift-Reduce](https://en.wikipedia.org/wiki/Shift-reduce_parser)
- [Parsing Ascendente](https://en.wikipedia.org/wiki/Bottom-up_parsing)

## 📄 Licencia

MIT License - Ver archivo LICENSE

---

**Fecha de Creación**: 19 de Noviembre de 2025  
**Versión**: 1.0
