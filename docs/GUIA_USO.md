# 📖 GUÍA DE USO Y PRUEBAS

**Analizador Sintáctico Descendente - Calculadora**  
**Autores:** Juan Esteban Cardozo Rivera • Juan Sebastián Gómez Usuga

---

## 🚀 CÓMO EJECUTAR EL PROGRAMA

### Programa Principal (Interfaz Gráfica)
```bash
python programa.py
```
Esto abrirá la interfaz gráfica completa con todas las funcionalidades.

### Suite Completa de Pruebas (44 tests)
```bash
python test_programa.py
```
Ejecuta todas las 44 pruebas unitarias y muestra el reporte completo.

### Pruebas Rápidas (8 tests)
```bash
python prueba_rapida.py
```
Ejecuta pruebas rápidas para verificación básica.

### Pruebas de Errores (10 tests)
```bash
python prueba_errores.py
```
Valida que todos los errores se detecten correctamente.

---

## 💡 CÓMO USAR LA INTERFAZ GRÁFICA

### 1. Ingresar Expresión
- Escribe la expresión matemática en el campo de entrada
- Presiona **Enter** o el botón **"Analizar"**

### 2. Ver Resultados
La interfaz tiene 4 pestañas:

**📊 Resultado:**
- Muestra el resultado de la evaluación
- Estado del análisis (léxico, sintáctico, semántico)
- Fecha y hora del análisis

**🔤 Tokens:**
- Lista todos los tokens identificados
- Muestra tipo, valor y categoría de cada token
- Total de tokens encontrados

**🌳 Traza de Derivación:**
- Muestra el proceso de análisis paso a paso
- Derivaciones de la gramática
- Valores intermedios del cálculo
- Leyenda explicativa

**📐 Gramática:**
- Reglas de producción completas
- Precedencia de operadores
- Tipo de análisis
- Tokens reconocidos

### 3. Botones Disponibles

**🔍 Analizar:** Procesa la expresión ingresada

**🗑️ Limpiar:** Limpia todos los campos

**📝 Ejemplos:** Muestra 10 ejemplos predefinidos para probar

**📊 Historial:** Muestra todas las expresiones evaluadas en la sesión

**💾 Exportar:** Guarda el análisis completo en un archivo .txt

---

## ✅ EJEMPLOS DE USO

### Operaciones Básicas
```
2 + 3           → 5
5 - 2           → 3
4 * 5           → 20
10 / 2          → 5
10 % 3          → 1
2 ** 3          → 8
2 ^ 4           → 16
```

### Con Precedencia
```
2 + 3 * 4       → 14  (no 20, porque * tiene mayor precedencia)
10 - 6 / 2      → 7   (no 2, porque / tiene mayor precedencia)
2 * 3 ** 2      → 18  (no 36, porque ** tiene mayor precedencia)
```

### Con Paréntesis
```
(2 + 3)         → 5
(2 + 3) * 4     → 20  (los paréntesis cambian la precedencia)
((2+3)*(4-1))   → 15  (paréntesis anidados)
```

### Números Decimales
```
3.5             → 3.5
3.5 + 2.5       → 6.0
2.5 * 4         → 10.0
```

### Números Negativos
```
-5              → -5
-5 + 3          → -2
-5 * 3          → -15
-(5 + 3)        → -8
```

### Expresiones Complejas
```
2 + 3 * 4 - 5                    → 9
10 / 2 + 8 * 3                   → 29
2 ** 3 + 10 % 3 * 2              → 10
(2 + 3) * 4 - 10 / 2 + 3 ** 2   → 24
```

---

## ❌ EJEMPLOS DE ERRORES

### Errores que el programa detecta:

**División por cero:**
```
10 / 0  → Error: División por cero detectada
```

**Módulo por cero:**
```
10 % 0  → Error: Módulo por cero no está definido
```

**Caracteres inválidos:**
```
2 + @   → Error léxico: Caracter no válido '@'
5 # 3   → Error léxico: Caracter no válido '#'
```

**Paréntesis desbalanceados:**
```
(2 + 3  → Error: Se esperaba 'PAREN_DER'
2 + 3)  → Error: Caracteres adicionales
```

**Sintaxis incorrecta:**
```
2 + * 3 → Error: Token inesperado '*'
+       → Error: Token inesperado '+'
2 +     → Error: Expresión incompleta
```

---

## 🧪 VERIFICAR QUE TODO FUNCIONA

### Ejecuta todas las pruebas en orden:

1. **Pruebas Rápidas** (debe tardar < 1 segundo):
```bash
python prueba_rapida.py
```
**Resultado esperado:** `🎉 ¡TODAS LAS PRUEBAS RÁPIDAS PASARON! 🎉`

2. **Pruebas de Errores** (debe tardar < 1 segundo):
```bash
python prueba_errores.py
```
**Resultado esperado:** `🎉 ¡TODOS LOS ERRORES SE MANEJAN CORRECTAMENTE! 🎉`

3. **Suite Completa** (debe tardar < 1 segundo):
```bash
python test_programa.py
```
**Resultado esperado:** `🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE! 🎉`
**Pruebas ejecutadas:** 44
**Exitosas:** 44
**Fallidas:** 0

4. **Programa Principal**:
```bash
python programa.py
```
**Resultado esperado:** Se abre la interfaz gráfica

---

## 📊 OPERADORES SOPORTADOS

| Operador | Símbolo | Ejemplo | Resultado |
|----------|---------|---------|-----------|
| Suma | + | 2 + 3 | 5 |
| Resta | - | 5 - 2 | 3 |
| Multiplicación | * | 4 * 5 | 20 |
| División | / | 10 / 2 | 5 |
| Módulo | % | 10 % 3 | 1 |
| Potencia | ** o ^ | 2 ** 3 | 8 |
| Paréntesis | ( ) | (2 + 3) * 4 | 20 |
| Negativo | - | -5 | -5 |

---

## 🎯 PRECEDENCIA DE OPERADORES

De mayor a menor precedencia:
1. **Paréntesis:** `( )`
2. **Potenciación:** `**` o `^`
3. **Multiplicación, División, Módulo:** `*`, `/`, `%`
4. **Suma, Resta:** `+`, `-`

**Asociatividad:** Izquierda a derecha (excepto potenciación: derecha a izquierda)

---

## 📁 ARCHIVOS DEL PROYECTO

```
Lab2/
│
├── programa.py                 # ⭐ Programa principal con interfaz
├── test_programa.py            # 📋 Suite completa (44 tests)
├── prueba_rapida.py           # ⚡ Pruebas rápidas (8 tests)
├── prueba_errores.py          # ❌ Pruebas de errores (10 tests)
│
├── VALIDACION_COMPLETA.md     # ✅ Resumen ejecutivo
├── RESULTADOS_PRUEBAS.md      # 📊 Resultados detallados
└── GUIA_USO.md                # 📖 Esta guía
```

---

## 💾 EXPORTAR RESULTADOS

1. Analiza una expresión
2. Haz clic en el botón **"💾 Exportar"**
3. Elige la ubicación y nombre del archivo
4. Se guardará un archivo .txt con:
   - Resultado del análisis
   - Tokens identificados
   - Traza de derivación completa
   - Fecha y hora
   - Información de autores

---

## 📚 PARA EL INFORME

### Capturas de Pantalla Recomendadas:

1. **Ventana principal** con una expresión simple
2. **Pestaña de Tokens** mostrando la tokenización
3. **Pestaña de Traza** con la derivación paso a paso
4. **Pestaña de Gramática** con las reglas
5. **Ventana de Ejemplos** mostrando opciones
6. **Ventana de Historial** con varios cálculos
7. **Error detectado** (ej: división por cero)
8. **Archivo exportado** abierto en un editor
9. **Terminal con pruebas** mostrando 44/44 exitosas

### Casos de Prueba para Demostración:

**Caso 1 - Simple:**
```
Expresión: 2 + 3 * 4
Resultado: 14
Explicación: Demuestra precedencia correcta
```

**Caso 2 - Paréntesis:**
```
Expresión: (2 + 3) * 4
Resultado: 20
Explicación: Paréntesis cambian la precedencia
```

**Caso 3 - Complejo:**
```
Expresión: 2 ** 3 + 10 % 3 * 2
Resultado: 10
Explicación: Todos los operadores en acción
```

**Caso 4 - Error:**
```
Expresión: 10 / 0
Error: División por cero detectada
Explicación: Manejo robusto de errores
```

---

## 🎓 TIPS PARA LA SUSTENTACIÓN

1. **Comienza mostrando pruebas:** Ejecuta `python test_programa.py` para demostrar que todo funciona.

2. **Abre el programa:** Ejecuta `python programa.py` para mostrar la interfaz.

3. **Demuestra casos simples primero:** 
   - `2 + 3`
   - `5 * 4`

4. **Muestra precedencia:**
   - `2 + 3 * 4` (resultado 14, no 20)

5. **Demuestra paréntesis:**
   - `(2 + 3) * 4` (resultado 20)

6. **Muestra la traza:**
   - Explica cómo se va derivando la expresión

7. **Demuestra errores:**
   - `10 / 0`
   - `2 + @`
   - `(2 + 3`

8. **Muestra funcionalidades extra:**
   - Historial
   - Exportar
   - Gramática

9. **Explica la gramática:**
   - Muestra la pestaña de gramática
   - Explica las producciones
   - Menciona que es LL(1)

10. **Cierra con las pruebas:**
    - 44 pruebas, 100% exitosas
    - Código robusto y validado

---

## ✅ CHECKLIST ANTES DE PRESENTAR

- [ ] Ejecutar `python test_programa.py` → 44/44 ✅
- [ ] Ejecutar `python prueba_rapida.py` → 8/8 ✅
- [ ] Ejecutar `python prueba_errores.py` → 10/10 ✅
- [ ] Ejecutar `python programa.py` → Interfaz se abre ✅
- [ ] Probar varios ejemplos en la interfaz
- [ ] Verificar que el historial funciona
- [ ] Verificar que la exportación funciona
- [ ] Revisar que los nombres de autores aparecen
- [ ] Tener capturas de pantalla listas
- [ ] Preparar explicación de la gramática

---

## 🎉 ¡TODO LISTO!

Tu programa está **100% funcional y validado**. Con:
- ✅ 62 pruebas exitosas en total
- ✅ Interfaz gráfica completa
- ✅ Documentación exhaustiva
- ✅ Código limpio y bien estructurado

**¡Éxito en tu sustentación!** 🚀

---

**Autores:**  
Juan Esteban Cardozo Rivera  
Juan Sebastián Gómez Usuga
