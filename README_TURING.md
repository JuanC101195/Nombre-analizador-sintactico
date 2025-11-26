# 🎰 Máquinas de Turing - Simuladores Interactivos

**Autores:** Juan Esteban Cardozo Rivera, Juan Sebastián Gómez Usuga

---

## 📖 Descripción General

Este proyecto implementa dos simuladores completos de **Máquinas de Turing** con interfaces gráficas interactivas en Python. Ambos programas permiten visualizar el funcionamiento paso a paso de estas máquinas teóricas fundamentales en la ciencia de la computación.

## 🎯 Programas Implementados

### 1️⃣ **maquina_turing_aritmetica.py**
Operaciones aritméticas en representación unaria

**Lenguaje:** Números en representación unaria
- `3 = 111`
- `5 = 11111`

**Operaciones:**
- ✅ **Suma:** `111+11 → 11111` (3+2=5)
- ✅ **Multiplicación:** `11*111 → 111111` (2×3=6)

**Características:**
- Representación visual de la cinta con el cabezal
- Traza completa de transiciones
- 8 ejemplos predefinidos
- Documentación teórica integrada

---

### 2️⃣ **maquina_turing_lenguajes.py**
Reconocimiento de lenguajes formales

**Lenguajes implementados:**

#### 📌 L = {a^n b^n c^n | n ≥ 1}
Cadenas con igual número de a's, b's y c's
- ✅ Válidos: `abc`, `aabbcc`, `aaabbbccc`
- ❌ Inválidos: `ab`, `aabbc`, `abcabc`, `cba`

**⚠️ IMPORTANTE:** Este es un **lenguaje TIPO 1** (sensible al contexto), NO puede ser generado por una gramática libre de contexto (Tipo 2).

**Gramática Sensible al Contexto:**
```
S → aSBC | aBC
CB → BC
aB → ab
bB → bb
bC → bc
cC → cc
```

#### 📌 Palíndromos L = {w | w = w^R}
Cadenas simétricas sobre {a, b}
- ✅ Válidos: `a`, `aba`, `abba`, `aabbaa`
- ❌ Inválidos: `ab`, `aab`, `abab`

**Gramática:**
```
S → aSa | bSb | a | b | ε
```

#### 📌 L = {a^n b^2n | n ≥ 1}
Doble de b's que a's
- ✅ Válidos: `abb`, `aabbbb`, `aaabbbbbb`
- ❌ Inválidos: `ab`, `aabbb`

**Gramática:**
```
S → aSbb | abb
```

---

## 🚀 Ejecución

### Requisitos
- Python 3.x
- Tkinter (incluido en la mayoría de instalaciones de Python)

### Ejecutar programa 1 (Aritmética)
```bash
python maquina_turing_aritmetica.py
```

### Ejecutar programa 2 (Lenguajes)
```bash
python maquina_turing_lenguajes.py
```

---

## 📊 Interfaz Gráfica

Ambos programas incluyen **4 pestañas** con información detallada:

### 🟢 Pestaña 1: Resultado
- Veredicto: ACEPTADA o RECHAZADA
- Detalles de la entrada
- Estadísticas de ejecución
- Estado final de la máquina

### 🔄 Pestaña 2: Traza de Ejecución
Tabla completa con:
- Paso número
- Estado actual
- Contenido de la cinta
- Posición del cabezal
- Símbolo leído
- Acción realizada

### 📋 Pestaña 3: Tabla de Transiciones
Función δ completa:
```
δ(estado, símbolo) → (nuevo_estado, escribir, mover)
```

### 📚 Pestaña 4: Teoría
- Definición formal de Máquina de Turing
- Tesis de Church-Turing
- Explicación del algoritmo
- Jerarquía de Chomsky
- Aplicaciones prácticas

---

## 🎓 Fundamentos Teóricos

### Definición Formal de Máquina de Turing

Una Máquina de Turing es una 7-tupla:

**M = (Q, Σ, Γ, δ, q₀, B, F)**

Donde:
- **Q:** Conjunto finito de estados
- **Σ:** Alfabeto de entrada
- **Γ:** Alfabeto de la cinta (Σ ⊆ Γ)
- **δ:** Función de transición Q × Γ → Q × Γ × {L, R, -}
- **q₀:** Estado inicial (q₀ ∈ Q)
- **B:** Símbolo blanco (B ∈ Γ - Σ)
- **F:** Conjunto de estados finales (F ⊆ Q)

### Funcionamiento

1. La máquina comienza en **q₀** con la entrada en la cinta
2. En cada paso:
   - Lee el símbolo bajo el cabezal
   - Consulta la función de transición δ
   - Escribe un nuevo símbolo
   - Mueve el cabezal (L/R/-)
   - Cambia de estado
3. Se detiene al alcanzar un estado final

---

## 📝 Ejemplos de Uso

### Programa 1: Aritmética Unaria

#### Suma: 3 + 2
```
Entrada:  111+11
Proceso:  111+11 → 1111+1 → 11111+
Resultado: 11111 (5)
```

#### Multiplicación: 2 × 3
```
Entrada:  11*111
Proceso:  [Suma 111 dos veces]
Resultado: 111111 (6)
```

### Programa 2: Lenguajes Formales

#### Ejemplo a^n b^n
```
Entrada:  aabb
Proceso:
  Paso 1: Xabb  → Marca primera 'a'
  Paso 2: XabY  → Marca última 'b'
  Paso 3: XXbY  → Marca segunda 'a'
  Paso 4: XXYY  → Marca penúltima 'b'
Resultado: ACEPTADA
```

#### Ejemplo Palíndromo
```
Entrada:  abba
Proceso:
  Paso 1: XbbX  → Marca extremos 'a'
  Paso 2: XXXX  → Marca extremos 'b'
Resultado: ACEPTADA (es simétrico)
```

---

## 🎯 Estrategias de Reconocimiento

### 1. Lenguaje a^n b^n (Ping-Pong)
1. Marca la primera 'a' como X
2. Busca la primera 'b' disponible y márcala como Y
3. Regresa al inicio
4. Repite hasta procesar toda la cadena
5. Si solo quedan marcas → ACEPTAR

### 2. Palíndromos (Comparación de Extremos)
1. Lee símbolo izquierdo y márcalo
2. Viaja al extremo derecho
3. Verifica que coincida
4. Márcalo y regresa
5. Repite hacia el centro
6. Si todos coinciden → ACEPTAR

### 3. Lenguaje a^n b^2n (Proporción 1:2)
1. Por cada 'a', busca exactamente 2 'b's
2. Marca las 3 como procesadas
3. Regresa al inicio
4. Si la proporción es exacta → ACEPTAR

---

## 📊 Complejidad Computacional

### Aritmética Unaria
- **Suma:** O(n) - Lineal en tamaño de entrada
- **Multiplicación:** O(n×m) - Proporcional al producto

### Reconocimiento de Lenguajes
- **a^n b^n:** O(n²) - Cuadrático
- **Palíndromos:** O(n²) - Cuadrático
- **a^n b^2n:** O(n²) - Cuadrático

Todos usan espacio O(n) en la cinta.

---

## 🌟 Jerarquía de Chomsky

```
Tipo 0: Recursivamente Enumerables ← Máquinas de Turing (estos programas)
  ↑
Tipo 1: Sensibles al Contexto
  ↑
Tipo 2: Libres de Contexto ← Lenguajes implementados (a^n b^n, etc.)
  ↑
Tipo 3: Regulares ← Autómatas Finitos
```

**Los lenguajes L = {a^n b^n} y similares son Tipo 2 (Libres de Contexto)**, lo que significa que:
- ❌ NO pueden ser reconocidos por Autómatas Finitos
- ✅ SÍ pueden ser reconocidos por Autómatas de Pila
- ✅ SÍ pueden ser reconocidos por Máquinas de Turing

---

## 🎓 Tesis de Church-Turing

> **"Todo lo que es efectivamente calculable puede ser calculado por una Máquina de Turing"**

Esta tesis establece que las Máquinas de Turing representan el **límite teórico de la computación**. Nuestros programas demuestran:

1. **Universalidad:** Pueden simular cualquier algoritmo
2. **Decidibilidad:** Determinan si una cadena pertenece a un lenguaje
3. **Límites:** Algunos problemas son inherentemente irresolubles

---

## 🔍 Diferencias con Ejemplos de Clase

### Similitudes Conceptuales
✅ Ambos usan representaciones clásicas (unaria, lenguajes formales)
✅ Implementan algoritmos de marcado y verificación
✅ Incluyen visualización de transiciones

### Diferencias Implementadas

#### Programa 1 (Aritmética):
- **Clase:** Ejemplos básicos de suma
- **Nuestro:** Suma + Multiplicación + GUI completa

#### Programa 2 (Lenguajes):
- **Clase:** Solo a^n b^n
- **Nuestro:** 3 lenguajes diferentes (a^n b^n, palíndromos, a^n b^2n)

---

## 📂 Estructura de Archivos

```
Lab2/
├── maquina_turing_aritmetica.py      # Programa 1: Operaciones aritméticas
├── maquina_turing_lenguajes.py       # Programa 2: Reconocimiento de lenguajes
├── README_TURING.md                  # Esta documentación
├── programa.py                       # Analizador descendente (proyecto anterior)
└── analizador_ascendente.py          # Analizador ascendente (proyecto anterior)
```

---

## 🎯 Casos de Prueba

### Programa 1: Aritmética

#### Suma
| Entrada | Resultado | Explicación |
|---------|-----------|-------------|
| `1+1` | `11` | 1+1=2 |
| `111+11` | `11111` | 3+2=5 |
| `1111+111` | `1111111` | 4+3=7 |
| `11111+1111` | `111111111` | 5+4=9 |

#### Multiplicación
| Entrada | Resultado | Explicación |
|---------|-----------|-------------|
| `1*1` | `1` | 1×1=1 |
| `11*111` | `111111` | 2×3=6 |
| `111*11` | `111111` | 3×2=6 |
| `11*1111` | `11111111` | 2×4=8 |

### Programa 2: Lenguajes

#### a^n b^n
| Entrada | Resultado | Explicación |
|---------|-----------|-------------|
| `ab` | ✅ ACEPTADA | n=1 |
| `aabb` | ✅ ACEPTADA | n=2 |
| `aaabbb` | ✅ ACEPTADA | n=3 |
| `aab` | ❌ RECHAZADA | Faltan 'b's |
| `abb` | ❌ RECHAZADA | Sobran 'b's |
| ` ` (vacío) | ✅ ACEPTADA | n=0 (ε) |

#### Palíndromos
| Entrada | Resultado | Explicación |
|---------|-----------|-------------|
| `a` | ✅ ACEPTADA | Palíndromo de 1 |
| `aba` | ✅ ACEPTADA | Simétrico |
| `abba` | ✅ ACEPTADA | Simétrico |
| `aabbaa` | ✅ ACEPTADA | Simétrico |
| `ab` | ❌ RECHAZADA | No simétrico |
| `abab` | ❌ RECHAZADA | No simétrico |

#### a^n b^2n
| Entrada | Resultado | Explicación |
|---------|-----------|-------------|
| `abb` | ✅ ACEPTADA | 1:2 (n=1) |
| `aabbbb` | ✅ ACEPTADA | 2:4 (n=2) |
| `aaabbbbbb` | ✅ ACEPTADA | 3:6 (n=3) |
| `ab` | ❌ RECHAZADA | Falta 1 'b' |
| `aabbb` | ❌ RECHAZADA | Falta 1 'b' |

---

## 🎨 Características de la Interfaz

### Controles
- **Campo de entrada:** Introduce la cadena a procesar
- **Selector de lenguaje:** (Solo programa 2) Elige a^n b^n, palíndromo o a^n b^2n
- **Botón Ejecutar:** Procesa la entrada
- **Botón Limpiar:** Reinicia la interfaz
- **Botón Ejemplos:** Carga ejemplos predefinidos

### Visualización
- 🟢 Verde: Cadena ACEPTADA
- 🔴 Rojo: Cadena RECHAZADA
- 📊 Tabla de transiciones completa
- 🎞️ Animación paso a paso
- 📋 Historial de operaciones

---

## 🔬 Aplicaciones Prácticas

### 1. Compiladores
- Análisis sintáctico
- Verificación de paréntesis balanceados
- Validación de estructuras anidadas

### 2. Procesamiento de Texto
- Reconocimiento de patrones
- Validación de formatos
- Análisis de simetría

### 3. Teoría de la Computación
- Demostración de decidibilidad
- Estudio de complejidad computacional
- Límites de la computación

### 4. Educación
- Visualización de algoritmos abstractos
- Comprensión de autómatas
- Fundamentos de la informática teórica

---

## 📚 Referencias Teóricas

### Conceptos Fundamentales
1. **Máquina de Turing (1936):** Alan Turing
2. **Tesis de Church-Turing:** Equivalencia computacional
3. **Jerarquía de Chomsky:** Clasificación de lenguajes
4. **Decidibilidad:** Problemas resolubles vs irresolubles

### Lenguajes Formales
- **L = {a^n b^n}:** Ejemplo clásico de lenguaje no regular
- **Palíndromos:** Simetría y reversibilidad
- **L = {a^n b^2n}:** Proporciones y conteo

---

## 🏆 Comparación: Máquinas de Turing vs Autómatas

| Característica | Autómatas Finitos | Autómatas de Pila | Máquinas de Turing |
|----------------|-------------------|-------------------|--------------------|
| **Memoria** | Solo estado | Pila (LIFO) | Cinta infinita |
| **Movimiento** | Solo avanza | Solo avanza | Bidireccional |
| **Potencia** | Lenguajes regulares | Lenguajes libres contexto | Todos los computables |
| **Ejemplos** | a*b* | a^n b^n | Cualquier algoritmo |
| **Estos programas** | ❌ | Parcial ✓ | ✅ Completo |

---

## ✨ Resumen

### Logros del Proyecto
✅ **Dos simuladores completos** de Máquinas de Turing
✅ **5 operaciones diferentes** implementadas
✅ **Interfaces gráficas** intuitivas y educativas
✅ **Visualización paso a paso** de transiciones
✅ **Documentación teórica** completa integrada
✅ **13 ejemplos predefinidos** listos para probar
✅ **Tablas de transiciones** formales y completas

### Conceptos Demostrados
- ✅ Tesis de Church-Turing
- ✅ Decidibilidad de lenguajes
- ✅ Jerarquía de Chomsky
- ✅ Complejidad computacional
- ✅ Límites de la computación

---

## 👥 Autores

**Juan Esteban Cardozo Rivera**
**Juan Sebastián Gómez Usuga**

---

## 📅 Información del Proyecto

- **Fecha:** Noviembre 2025
- **Curso:** Teoría de la Computación
- **Herramienta:** Python 3 + Tkinter
- **Líneas de código:** ~1,300 (ambos programas)
- **Tiempo de desarrollo:** Proyecto académico

---

## 🎯 Conclusiones

Las **Máquinas de Turing** son el modelo computacional más poderoso que existe teóricamente. Estos programas demuestran:

1. **Universalidad:** Pueden simular cualquier cálculo efectivo
2. **Simplicidad:** Con solo 7 componentes básicos
3. **Potencia:** Reconocen lenguajes que otros autómatas no pueden
4. **Fundamento:** Base teórica de todos los ordenadores modernos

Los dos simuladores implementados proporcionan una **herramienta educativa completa** para comprender estos conceptos fundamentales de la ciencia de la computación.

---

**¡Gracias por explorar estos simuladores de Máquinas de Turing!** 🎉
