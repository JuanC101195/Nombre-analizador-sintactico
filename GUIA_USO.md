# 🎯 GUÍA RÁPIDA DE USO - ANALIZADOR ASCENDENTE

## ✅ PROYECTO COMPLETADO Y FUNCIONAL

El analizador sintáctico ascendente está **100% funcional** y listo para usar.

---

## 🚀 INICIO RÁPIDO

### 1️⃣ Ejecutar el Programa Principal

```bash
python analizador_ascendente.py
```

Se abrirá una ventana con la interfaz gráfica completa.

### 2️⃣ Verificar que Todo Funciona (Pruebas)

```bash
python test_analizador_funcional.py
```

**Resultado esperado:**
```
Total de pruebas ejecutadas: 29
✓ Pruebas exitosas: 29
✗ Pruebas fallidas: 0
⚠ Errores: 0

✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE
```

---

## 📝 CÓMO USAR LA INTERFAZ

### Método 1: Escribir Manualmente

1. Escribe una expresión en el campo de entrada
2. Presiona **Enter** o clic en "🔍 Analizar"
3. Observa los resultados en las 4 pestañas:
   - **📊 Resultado**: Resultado final
   - **🔄 Traza Shift-Reduce**: Proceso paso a paso
   - **🔤 Tokens**: Tokens identificados
   - **📐 Gramática**: Documentación

### Método 2: Usar Ejemplos Predefinidos

1. Clic en el botón "📝 Ejemplos"
2. Selecciona cualquiera de los 10 ejemplos
3. Se ejecutará automáticamente

---

## 💡 EJEMPLOS PARA PROBAR

### ✅ Ejemplos Básicos

```
var = 5 + 7
x = 10 * 2
y = (5 + 3) * 2
z = 10 / 2 + 8
```

### ✅ Ejemplo del Enunciado

```
var = 5 + 7(3 + 3/4)
```
**Resultado:** `var = 31.25`

### ✅ Multiplicación Implícita

```
x = 2(3 + 4)
a = 7(3)
b = (2 + 3)(4 + 5)
```

### ✅ Con Variables

```
x = 5
y = 3
result = x + y * 2
```
**Resultado:** `result = 11`

### ✅ Expresiones Complejas

```
a = 2 + 3(4 - 1) / 2
b = ((2 + 3) * 4)
c = 10 - 2(3 + 1)
```

---

## 📊 PESTAÑAS DE LA INTERFAZ

### 📊 Pestaña "Resultado"
- Muestra el resultado final de la evaluación
- Indica si hubo errores
- Muestra el valor asignado a la variable (si aplica)

### 🔄 Pestaña "Traza Shift-Reduce"
- Muestra cada paso del análisis ascendente
- Columnas: PASO | PILA | ENTRADA | ACCIÓN
- Ver operaciones SHIFT, REDUCE y ACEPTAR

### 🔤 Pestaña "Tokens"
- Lista todos los tokens identificados
- Formato: # | TIPO | VALOR
- Útil para verificar el análisis léxico

### 📐 Pestaña "Gramática"
- Documentación de las reglas de producción
- Información sobre precedencia
- Explicación del algoritmo Shift-Reduce

---

## 🔘 BOTONES DISPONIBLES

- **🔍 Analizar**: Procesa la expresión ingresada
- **🗑️ Limpiar**: Limpia entrada y resultados
- **📝 Ejemplos**: Muestra 10 ejemplos interactivos
- **📊 Variables**: Muestra variables almacenadas en memoria

---

## ✨ CARACTERÍSTICAS DESTACADAS

### ✅ Multiplicación Implícita
El analizador automáticamente convierte:
- `7(3)` → `7*(3)`
- `2(3 + 4)` → `2*(3 + 4)`
- `(2 + 3)(4 + 5)` → `(2 + 3)*(4 + 5)`

### ✅ Variables Persistentes
Las variables se mantienen en memoria:
```
x = 5      → x almacena 5
y = x + 3  → y almacena 8
```

### ✅ Precedencia Correcta
- Paréntesis: `( )`
- Multiplicación/División: `*`, `/`
- Suma/Resta: `+`, `-`

Ejemplo:
```
2 + 3 * 4 = 14    (NO 20)
(2 + 3) * 4 = 20
```

---

## 📁 ARCHIVOS DEL PROYECTO

### Archivos Principales
```
analizador_ascendente.py          ← Programa principal (ejecutar este)
test_analizador_funcional.py     ← Suite de pruebas funcional
```

### Documentación
```
README_ASCENDENTE.md              ← Documentación completa
RESUMEN_PROYECTO.md               ← Resumen del proyecto
GUIA_USO.md                       ← Esta guía
```

### Otros Archivos
```
programa.py                       ← Analizador descendente (proyecto anterior)
test_analizador_ascendente.py    ← Pruebas antiguas (obsoletas)
debug_ascendente.py               ← Script de depuración
```

---

## 🎯 GRAMÁTICA UTILIZADA

```
S  → VAR = E    (Asignación)
S  → E          (Expresión)
E  → E + T      (Suma)
E  → E - T      (Resta)
E  → T          (Término)
T  → T * F      (Multiplicación)
T  → T / F      (División)
T  → F          (Factor)
F  → ( E )      (Paréntesis)
F  → número     (Número)
F  → VAR        (Variable)
```

---

## ❓ PREGUNTAS FRECUENTES

### ¿Por qué `7(3)` funciona como multiplicación?
El analizador automáticamente inserta el operador `*` cuando detecta:
- Un número seguido de paréntesis: `7(3)` → `7*(3)`
- Paréntesis adyacentes: `(2)(3)` → `(2)*(3)`

### ¿Cómo veo las variables almacenadas?
Haz clic en el botón "📊 Variables" en la interfaz.

### ¿Qué es Shift-Reduce?
Es el algoritmo de análisis ascendente que:
1. **SHIFT**: Empuja tokens a la pila
2. **REDUCE**: Aplica producciones de la gramática
3. **ACCEPT**: Reconoce la cadena cuando pila = `$S`

### ¿Puedo usar decimales?
Sí, el analizador soporta números decimales:
```
x = 3.14
y = 2.5 * 4.0
```

### ¿Cómo funciona la precedencia?
Se respeta automáticamente:
```
2 + 3 * 4 = 14       (multiplicación primero)
10 + 8 / 2 = 14      (división primero)
(2 + 3) * 4 = 20     (paréntesis primero)
```

---

## ✅ VERIFICACIÓN DE FUNCIONAMIENTO

### Test Rápido 1: Ejemplo del Enunciado
```bash
1. Ejecutar: python analizador_ascendente.py
2. Escribir: var = 5 + 7(3 + 3/4)
3. Presionar Enter
4. Verificar resultado: var = 31.25 ✓
```

### Test Rápido 2: Pruebas Unitarias
```bash
1. Ejecutar: python test_analizador_funcional.py
2. Verificar: 29/29 pruebas exitosas ✓
```

### Test Rápido 3: Ejemplos de la Interfaz
```bash
1. Ejecutar: python analizador_ascendente.py
2. Clic en "📝 Ejemplos"
3. Probar cada uno de los 10 ejemplos
4. Verificar que todos funcionan ✓
```

---

## 🎓 PARA ENTENDER EL CÓDIGO

### Clase `AnalizadorAscendente`
```python
tokenizar()                    # Convierte expresión en tokens
analizar_sintaxis()            # Realiza análisis sintáctico
generar_traza_shift_reduce()   # Genera traza del proceso
evaluar_expresion()            # Evalúa y retorna resultado
```

### Clase `InterfazAscendente`
```python
crear_interfaz()               # Construye la GUI
analizar_expresion()           # Botón "Analizar"
mostrar_ejemplos()             # Botón "Ejemplos"
mostrar_variables()            # Botón "Variables"
```

---

## 📊 ESTADÍSTICAS DEL PROYECTO

- **Líneas de código:** 711 (analizador) + 242 (pruebas) = 953 total
- **Clases:** 2 (AnalizadorAscendente, InterfazAscendente)
- **Pruebas unitarias:** 29 (100% exitosas)
- **Ejemplos incluidos:** 10
- **Producciones gramaticales:** 11
- **Tokens soportados:** 9 tipos

---

## 👥 AUTORES

- **Juan Esteban Cardozo Rivera**
- **Juan Sebastián Gómez Usuga**

---

## 🎉 ¡PROYECTO COMPLETADO!

**Estado:** ✅ PRODUCCIÓN  
**Pruebas:** ✅ 29/29 PASANDO  
**Funcionalidad:** ✅ 100% OPERATIVA  

**¡Listo para usar y entregar!** 🚀
