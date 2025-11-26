# 🎓 Teoría de la Computación - Proyectos Completos

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-91%2F91%20passing-brightgreen.svg)

Implementación completa de **Analizadores Sintácticos** y **Máquinas de Turing** con interfaces gráficas interactivas.

## 👥 Autores

- **Juan Esteban Cardozo Rivera**
- **Juan Sebastián Gómez Usuga**

## 📋 Descripción General

Este repositorio contiene **CUATRO proyectos completos** de teoría de la computación:

### 📊 PARTE 1: Analizadores Sintácticos

Implementaciones de parsers con dos enfoques diferentes:

### 🔽 Proyecto 1: Analizador Descendente (Top-Down)
Implementación de un **parser LL(1)** recursivo descendente para evaluar expresiones matemáticas.

- **Archivo principal**: `programa.py`
- **Algoritmo**: Análisis Recursivo Descendente
- **Tipo**: Top-Down (Raíz → Hojas)
- **Pruebas**: 62 tests pasando (100%)

### 🔼 Proyecto 2: Analizador Ascendente (Bottom-Up)
Implementación de un **parser Shift-Reduce** para reconocer y evaluar expresiones con asignaciones.

- **Archivo principal**: `analizador_ascendente.py`
- **Algoritmo**: Shift-Reduce (LR)
- **Tipo**: Bottom-Up (Hojas → Raíz)
- **Pruebas**: 29 tests pasando (100%)
- **Características especiales**: Multiplicación implícita, traza detallada

## 🎯 Características por Proyecto

### Analizador Descendente (LL)
- ✅ Análisis léxico completo
- ✅ Parser recursivo descendente
- ✅ Evaluación de expresiones matemáticas
- ✅ Operadores: `+`, `-`, `*`, `/`, `%`, `**`, `^`
- ✅ Números negativos y decimales
- ✅ Interfaz gráfica con Tkinter
- ✅ 62 pruebas unitarias

### Analizador Ascendente (LR)
- ✅ Algoritmo Shift-Reduce
- ✅ Reconocimiento de asignaciones: `var = expresión`
- ✅ **Multiplicación implícita**: `7(3)` → `7*(3)`
- ✅ Traza completa del análisis Shift-Reduce
- ✅ Operadores: `+`, `-`, `*`, `/`, `()`
- ✅ Interfaz gráfica con 4 pestañas informativas
- ✅ 29 pruebas unitarias
- ✅ Almacenamiento de variables

### 🎰 PARTE 2: Máquinas de Turing

Implementaciones de simuladores de Máquinas de Turing:

#### 🔢 Programa 3: Operaciones Aritméticas
Máquina de Turing para cálculos en representación unaria.

- **Archivo principal**: `maquina_turing_aritmetica.py`
- **Operaciones**: Suma y multiplicación unaria
- **Ejemplos**: `111+11 = 11111` (3+2=5), `11*111 = 111111` (2×3=6)
- **Características**: Visualización de cinta y cabezal paso a paso

#### 🔤 Programa 4: Reconocimiento de Lenguajes
Máquina de Turing para verificar lenguajes formales.

- **Archivo principal**: `maquina_turing_lenguajes.py`
- **Lenguajes**:
  - L = {a^n b^n c^n}: Igual número de a's, b's y c's (Tipo 1)
  - Palíndromos: Cadenas simétricas sobre {a, b}
  - L = {a^n b^2n}: Doble de b's que a's
- **Características**: 3 algoritmos de reconocimiento diferentes

## 🚀 Inicio Rápido

### 📊 Analizadores Sintácticos

#### Ejecutar Analizador Descendente (LL)
```bash
python programa.py
```

#### Ejecutar Analizador Ascendente (Shift-Reduce)
```bash
python analizador_ascendente.py
```

#### Ejecutar Pruebas de Analizadores
```bash
# Pruebas del descendente
python test_programa.py

# Pruebas del ascendente
python test_analizador_funcional.py
```

### 🎰 Máquinas de Turing

#### Ejecutar Máquina de Turing - Aritmética
```bash
python maquina_turing_aritmetica.py
```

#### Ejecutar Máquina de Turing - Lenguajes
```bash
python maquina_turing_lenguajes.py
```

## 📐 Especificaciones Formales

### 📊 Analizadores Sintácticos

#### Gramática Descendente (LL)

```
E  → T E'
E' → + T E' | - T E' | ε
T  → P T'
T' → * P T' | / P T' | % P T' | ε
P  → F P'
P' → ** F P' | ^ F P' | ε
F  → ( E ) | número | -número
```

**Tipo**: Top-Down (LL)  
**Precedencia**: `()` > `**` > `* / %` > `+ -`

#### Gramática Ascendente (LR)

```
S  → VAR = E | E
E  → E + T | E - T | T
T  → T * F | T / F | F
F  → ( E ) | número | VAR
```

**Tipo**: Bottom-Up (Shift-Reduce)  
**Característica especial**: Permite recursión por izquierda  
**Precedencia**: `()` > `* /` > `+ -`

### 🎰 Máquinas de Turing

#### Definición Formal

**M = (Q, Σ, Γ, δ, q₀, B, F)**

Donde:
- **Q:** Conjunto finito de estados
- **Σ:** Alfabeto de entrada
- **Γ:** Alfabeto de la cinta (Σ ⊆ Γ)
- **δ:** Función de transición Q × Γ → Q × Γ × {L, R, -}
- **q₀:** Estado inicial (q₀ ∈ Q)
- **B:** Símbolo blanco (B ∈ Γ - Σ)
- **F:** Conjunto de estados finales (F ⊆ Q)

#### Lenguajes Formales Implementados

1. **L = {a^n b^n c^n | n ≥ 1}**
   - **Lenguaje Tipo 1** (sensible al contexto, NO libre de contexto)
   - Gramática CSG: `S → aSBC | aBC; CB → BC; aB → ab; bB → bb; bC → bc; cC → cc`
   - Ejemplos: `abc`, `aabbcc`, `aaabbbccc`

2. **L = {w | w = w^R, w ∈ {a,b}*}** (Palíndromos)
   - Gramática: `S → aSa | bSb | a | b | ε`
   - Ejemplos: `a`, `aba`, `abba`, `aabbaa`

3. **L = {a^n b^2n | n ≥ 1}**
   - Gramática: `S → aSbb | abb`
   - Ejemplos: `abb`, `aabbbb`, `aaabbbbbb`

## 🚀 Instalación

### Requisitos
- Python 3.8 o superior
- Tkinter (incluido con Python en Windows)

### Clonar el repositorio
```bash
git clone https://github.com/JuanC101195/Nombre-analizador-sintactico.git
cd Nombre-analizador-sintactico
```

### Ejecutar el programa
```bash
python programa.py
```

## 🧪 Pruebas

### Analizador Descendente
```bash
python test_programa.py        # 44 tests
python prueba_rapida.py        # 8 tests
python prueba_errores.py       # 10 tests
```

**Resultados**: ✅ 62/62 pruebas pasando (100%)

### Analizador Ascendente
```bash
python test_analizador_funcional.py    # 29 tests
```

**Resultados**: ✅ 29/29 pruebas pasando (100%)

### Total del Proyecto
```
✅ 91 pruebas ejecutadas
✅ 91 exitosas (100%)
❌ 0 fallidas (0%)
```

## 📖 Ejemplos de Uso

### Analizador Descendente

```python
# Operaciones básicas
2 + 3           → 5.0
5 * 4           → 20.0
2 ** 3          → 8.0

# Precedencia
2 + 3 * 4       → 14.0
(2 + 3) * 4     → 20.0

# Números negativos
-5 + 3          → -2.0
```

### Analizador Ascendente

```python
# Asignaciones
var = 5 + 7                    → var = 12

# Ejemplo del enunciado
var = 5 + 7(3 + 3/4)          → var = 31.25

# Multiplicación implícita
x = 2(3 + 4)                   → x = 14
a = 7(3)                       → a = 21
b = (2 + 3)(4 + 5)            → b = 45

# Variables en expresiones
x = 5
y = 3
result = x + y * 2             → result = 11
```

## 🎯 Casos de Prueba

### Analizador Descendente (62 tests)
- ✅ Operaciones básicas (7 tests)
- ✅ Precedencia de operadores (4 tests)
- ✅ Paréntesis y anidamiento (5 tests)
- ✅ Números decimales (4 tests)
- ✅ Números negativos (4 tests)
- ✅ Expresiones complejas (4 tests)
- ✅ Tokenización (3 tests)
- ✅ Casos extremos (5 tests)
- ✅ Detección de errores (10 tests)

### Analizador Ascendente (29 tests)
- ✅ Tokenización (5 tests)
- ✅ Reconocimiento sintáctico (5 tests)
- ✅ Evaluación de expresiones (9 tests)
- ✅ Precedencia de operadores (3 tests)
- ✅ Manejo de variables (3 tests)
- ✅ Traza Shift-Reduce (4 tests)

## 📁 Estructura del Proyecto

```
Lab2/
├── 📊 ANALIZADOR DESCENDENTE (LL)
│   ├── programa.py                    # Programa principal
│   ├── test_programa.py              # 44 pruebas unitarias
│   ├── prueba_rapida.py             # 8 pruebas rápidas
│   └── prueba_errores.py            # 10 pruebas de errores
│
├── 📈 ANALIZADOR ASCENDENTE (LR)
│   ├── analizador_ascendente.py     # Programa principal
│   ├── test_analizador_funcional.py # 29 pruebas unitarias
│   └── debug_ascendente.py          # Script de depuración
│
├── 📚 DOCUMENTACIÓN
│   ├── README.md                     # Este archivo
│   ├── README_ASCENDENTE.md         # Documentación ascendente
│   ├── GUIA_USO.md                  # Guía de uso
│   ├── RESUMEN_PROYECTO.md          # Resumen ejecutivo
│   ├── COMPARACION_PROYECTOS.md     # Comparativa LL vs LR
│   ├── INDICE_ARCHIVOS.md           # Índice completo
│   └── LICENSE                       # Licencia MIT
│
└── 📂 docs/
    ├── VALIDACION_COMPLETA.md       # Validación descendente
    ├── RESULTADOS_PRUEBAS.md        # Resultados detallados
    └── GUIA_USO.md                  # Manual de usuario
```

## 🛠️ Tecnologías

- **Lenguaje**: Python 3.8+
- **GUI**: Tkinter
- **Testing**: unittest
- **Regex**: re (expresiones regulares)

## 📊 Comparación de Algoritmos

| Característica | Descendente (LL) | Ascendente (LR) |
|---------------|------------------|-----------------|
| **Construcción** | Raíz → Hojas | Hojas → Raíz |
| **Algoritmo** | Recursivo | Shift-Reduce |
| **Gramáticas** | LL(1) | LR (más general) |
| **Recursión izq.** | ❌ No | ✅ Sí |
| **Implementación** | Más simple | Más compleja |
| **Detección errores** | Temprana | Más tardía |
| **Potencia** | Media | Alta |

Para más detalles, ver [COMPARACION_PROYECTOS.md](COMPARACION_PROYECTOS.md)

## 📊 Rendimiento

### Analizador Descendente
- **Tiempo de análisis**: < 0.001s por expresión
- **Suite de pruebas**: 0.020s (62 tests)

### Analizador Ascendente
- **Tiempo de análisis**: < 0.001s por expresión
- **Suite de pruebas**: 0.012s (29 tests)
- **Traza generada**: 15-30 pasos por expresión

## 🎓 Contexto Académico

Este proyecto fue desarrollado como parte del curso de **Teoría de la Computación**. Incluye **cuatro implementaciones completas**:

### ✅ PARTE 1: Analizadores Sintácticos

#### Analizador Descendente (LL)
- ✅ Parser recursivo descendente
- ✅ Gramática LL(1)
- ✅ Tokens reconocidos correctamente
- ✅ Evaluación de operaciones
- ✅ Detección de errores
- ✅ Modo gráfico funcional
- ✅ 62 tests (100%)

#### Analizador Ascendente (LR)
- ✅ Algoritmo Shift-Reduce implementado
- ✅ Reconocimiento de asignaciones: `var = expresión`
- ✅ **Ejemplo del enunciado funcional**: `var = 5 + 7(3 + 3/4) = 31.25`
- ✅ Multiplicación implícita automática
- ✅ Traza completa del análisis
- ✅ Modo gráfico con 4 pestañas
- ✅ Almacenamiento de variables
- ✅ 29 tests (100%)

### ✅ PARTE 2: Máquinas de Turing

#### Máquina de Turing - Aritmética
- ✅ Operaciones en representación unaria
- ✅ Suma: `111+11 → 11111` (3+2=5)
- ✅ Multiplicación: `11*111 → 111111` (2×3=6)
- ✅ Visualización de cinta y cabezal
- ✅ Traza paso a paso
- ✅ 8 ejemplos predefinidos

#### Máquina de Turing - Lenguajes
- ✅ Reconocimiento de L = {a^n b^n c^n} (Tipo 1)
- ✅ Verificación de palíndromos
- ✅ Reconocimiento de L = {a^n b^2n}
- ✅ Tablas de transiciones completas
- ✅ 13 ejemplos predefinidos
- ✅ Teoría integrada en GUI

## 📄 Documentación Completa

### Documentación General
- **README.md**: Este archivo (visión general de todos los proyectos)
- **LICENSE**: Licencia MIT del proyecto

### Documentación Analizadores Sintácticos
- **docs/VALIDACION_COMPLETA.md**: Resumen ejecutivo descendente
- **docs/RESULTADOS_PRUEBAS.md**: Documentación detallada de 62 pruebas
- **docs/GUIA_USO.md**: Manual completo de usuario
- **README_ASCENDENTE.md**: Documentación técnica ascendente
- **COMPARACION_PROYECTOS.md**: Análisis comparativo LL vs LR
- **INDICE_ARCHIVOS.md**: Índice completo de archivos

### Documentación Máquinas de Turing
- **README_TURING.md**: Documentación completa de ambas MT
  - Fundamentos teóricos
  - Definición formal de Máquina de Turing
  - Tesis de Church-Turing
  - Jerarquía de Chomsky
  - Ejemplos de uso detallados
  - Casos de prueba completos
  - Comparación con ejemplos de clase

## 🤝 Contribuciones

Este es un proyecto académico. Si deseas contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

**Juan Esteban Cardozo Rivera** - [GitHub](https://github.com/JuanC101195)  
**Juan Sebastián Gómez Usuga** - [GitHub](https://github.com/JuanC101195)

## 🙏 Agradecimientos

- Curso de Compiladores/Lenguajes de Programación
- Comunidad de Python
- Documentación de Tkinter

---

**Estado del Proyecto**: ✅ Completo y Validado (4 Programas)  
**Última Actualización**: 26 de noviembre de 2025

### 🎯 Proyectos Incluidos
- ✅ **Analizador Descendente (LL)**: 656 líneas, 62 tests
- ✅ **Analizador Ascendente (LR)**: 711 líneas, 29 tests
- ✅ **Máquina de Turing - Aritmética**: 580 líneas, 8 ejemplos
- ✅ **Máquina de Turing - Lenguajes**: 650 líneas, 13 ejemplos
- ✅ **Total**: ~3,900 líneas de código + documentación

### 📊 Estadísticas
- 4 programas completos con GUI
- 91 tests automatizados (analizadores)
- 21 ejemplos interactivos (máquinas de turing)
- 5 lenguajes formales implementados
- 10+ archivos de documentación

⭐ Si te gusta este proyecto, no olvides darle una estrella!
