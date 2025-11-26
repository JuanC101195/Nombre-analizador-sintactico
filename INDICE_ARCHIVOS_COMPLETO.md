# 📂 ÍNDICE COMPLETO DE ARCHIVOS - LAB2

**Proyecto**: Teoría de la Computación - Proyectos Completos  
**Autores**: Juan Esteban Cardozo Rivera, Juan Sebastián Gómez Usuga  
**Última Actualización**: 26 de noviembre de 2025

---

## 🎯 ARCHIVOS PRINCIPALES

### ⭐ PARTE 1: Analizadores Sintácticos

#### Analizador Descendente (LL)
```
📄 programa.py                       ← PARSER DESCENDENTE - 656 líneas
📄 test_programa.py                  ← Pruebas del descendente (62 tests)
📄 prueba_rapida.py                  ← Pruebas rápidas
📄 prueba_errores.py                 ← Pruebas de errores
```

#### Analizador Ascendente (LR Shift-Reduce)
```
📄 analizador_ascendente.py          ← PARSER ASCENDENTE - 711 líneas
📄 test_analizador_funcional.py     ← Pruebas funcionales (29 tests)
📄 test_analizador_ascendente.py    ← Pruebas adicionales
📄 debug_ascendente.py               ← Debug auxiliar
```

### ⭐ PARTE 2: Máquinas de Turing

#### Máquina de Turing - Aritmética Unaria
```
📄 maquina_turing_aritmetica.py     ← MT ARITMÉTICA - 580 líneas
                                      Operaciones: suma y multiplicación unaria
                                      Ejemplos: 111+11 → 11111 (3+2=5)
```

#### Máquina de Turing - Reconocimiento de Lenguajes
```
📄 maquina_turing_lenguajes.py      ← MT LENGUAJES - 650 líneas
                                      Lenguajes: a^n b^n, palíndromos, a^n b^2n
                                      Ejemplos: 13 casos de prueba
```

---

## 📚 DOCUMENTACIÓN

### Documentación Principal
```
📄 README.md                         ← README PRINCIPAL - Visión completa de 4 proyectos
📄 LICENSE                           ← Licencia MIT
📄 LEER_PRIMERO.txt                  ← Instrucciones iniciales
```

### Documentación Analizadores Sintácticos
```
📄 README_ASCENDENTE.md              ← Documentación técnica del ascendente
📄 RESUMEN_PROYECTO.md               ← Resumen ejecutivo
📄 COMPARACION_PROYECTOS.md          ← Análisis comparativo LL vs LR
📄 GUIA_USO.md                       ← Guía rápida de uso
📄 INDICE_ARCHIVOS.md                ← Índice anterior (este archivo lo reemplaza)
📄 INDICE_ARCHIVOS_COMPLETO.md       ← ESTE ARCHIVO
```

### Documentación Máquinas de Turing
```
📄 README_TURING.md                  ← DOCUMENTACIÓN COMPLETA DE MT
                                      • Fundamentos teóricos
                                      • Definición formal
                                      • Tesis de Church-Turing
                                      • Jerarquía de Chomsky
                                      • Ejemplos de uso
                                      • Casos de prueba

📄 RESUMEN_TURING.md                 ← RESUMEN EJECUTIVO DE MT
                                      • Objetivos cumplidos
                                      • Comparación con clase
                                      • Estadísticas del proyecto
                                      • Algoritmos implementados
```

### Documentación Técnica (Carpeta docs/)
```
📁 docs/
   📄 VALIDACION_COMPLETA.md         ← Validación del descendente
   📄 RESULTADOS_PRUEBAS.md          ← Resultados detallados 62 pruebas
   📄 GUIA_USO.md                    ← Manual de usuario
```

---

## 📊 ESTADÍSTICAS DEL PROYECTO

### Líneas de Código por Programa
```
programa.py                    656 líneas
analizador_ascendente.py       711 líneas
maquina_turing_aritmetica.py   580 líneas
maquina_turing_lenguajes.py    650 líneas
──────────────────────────────────────────
TOTAL CÓDIGO:                 2,597 líneas
```

### Tests Automatizados
```
test_programa.py               62 tests ✅
test_analizador_funcional.py   29 tests ✅
──────────────────────────────────────────
TOTAL TESTS:                   91 tests (100% passing)
```

### Documentación
```
README.md                      ~450 líneas
README_ASCENDENTE.md           ~400 líneas
README_TURING.md               ~500 líneas
RESUMEN_TURING.md              ~380 líneas
Otros docs/                    ~600 líneas
──────────────────────────────────────────
TOTAL DOCS:                   ~2,330 líneas
```

### GRAN TOTAL DEL PROYECTO
```
CÓDIGO:                        2,597 líneas
DOCUMENTACIÓN:                 2,330 líneas
TESTS:                            91 tests
EJEMPLOS INTERACTIVOS:            42 ejemplos
──────────────────────────────────────────
TOTAL:                        ~4,927 líneas de código y documentación
```

---

## 🎯 CÓMO USAR ESTE PROYECTO

### Para Ejecutar Analizadores Sintácticos
```bash
# Analizador Descendente (LL)
python programa.py

# Analizador Ascendente (Shift-Reduce)
python analizador_ascendente.py
```

### Para Ejecutar Máquinas de Turing
```bash
# MT Aritmética (suma y multiplicación unaria)
python maquina_turing_aritmetica.py

# MT Lenguajes (a^n b^n, palíndromos, a^n b^2n)
python maquina_turing_lenguajes.py
```

### Para Ejecutar Tests
```bash
# Tests del descendente (62 tests)
python test_programa.py

# Tests del ascendente (29 tests)
python test_analizador_funcional.py
```

---

## 📖 GUÍA DE LECTURA RECOMENDADA

### Para Comenzar (5 minutos)
1. **README.md** - Visión general de los 4 proyectos
2. **LEER_PRIMERO.txt** - Instrucciones básicas

### Para Entender Analizadores (15 minutos)
1. **README_ASCENDENTE.md** - Documentación técnica completa
2. **COMPARACION_PROYECTOS.md** - Diferencias LL vs LR
3. **GUIA_USO.md** - Cómo usar los analizadores

### Para Entender Máquinas de Turing (20 minutos)
1. **README_TURING.md** - Documentación completa de MT
   - Fundamentos teóricos
   - Definición formal
   - Tesis de Church-Turing
   - Jerarquía de Chomsky
   - Ejemplos detallados

2. **RESUMEN_TURING.md** - Resumen ejecutivo
   - Comparación con ejemplos de clase
   - Algoritmos implementados
   - Casos de prueba

### Para Profundizar (30+ minutos)
1. **docs/RESULTADOS_PRUEBAS.md** - Detalles de 62 tests
2. **RESUMEN_PROYECTO.md** - Resumen ejecutivo analizadores
3. Revisar código fuente de cada programa

---

## 🔍 BÚSQUEDA RÁPIDA

### Quiero ver...
- **Código del analizador descendente** → `programa.py`
- **Código del analizador ascendente** → `analizador_ascendente.py`
- **Código MT aritmética** → `maquina_turing_aritmetica.py`
- **Código MT lenguajes** → `maquina_turing_lenguajes.py`
- **Documentación completa MT** → `README_TURING.md`
- **Comparación LL vs LR** → `COMPARACION_PROYECTOS.md`
- **Todos los tests** → `test_*.py`
- **Guía de uso** → `GUIA_USO.md`
- **Resumen general** → `README.md`

### Quiero entender...
- **Analizador Descendente** → `README.md` + `programa.py`
- **Analizador Ascendente** → `README_ASCENDENTE.md` + `analizador_ascendente.py`
- **Máquinas de Turing** → `README_TURING.md`
- **Diferencias LL/LR** → `COMPARACION_PROYECTOS.md`
- **Teoría de MT** → `README_TURING.md` (sección teoría)
- **Algoritmos MT** → `RESUMEN_TURING.md` (sección algoritmos)

---

## 📦 ESTRUCTURA COMPLETA DEL REPOSITORIO

```
Lab2/
│
├── 🎯 PROGRAMAS PRINCIPALES (4)
│   ├── programa.py                       (656 líneas - Analizador Descendente)
│   ├── analizador_ascendente.py          (711 líneas - Analizador Ascendente)
│   ├── maquina_turing_aritmetica.py      (580 líneas - MT Aritmética)
│   └── maquina_turing_lenguajes.py       (650 líneas - MT Lenguajes)
│
├── 🧪 TESTS (3)
│   ├── test_programa.py                  (62 tests - Descendente)
│   ├── test_analizador_funcional.py      (29 tests - Ascendente)
│   ├── test_analizador_ascendente.py     (Tests adicionales)
│   ├── prueba_rapida.py                  (Pruebas rápidas)
│   └── prueba_errores.py                 (Pruebas de errores)
│
├── 📚 DOCUMENTACIÓN PRINCIPAL (3)
│   ├── README.md                         (README principal - 4 proyectos)
│   ├── LICENSE                           (Licencia MIT)
│   └── LEER_PRIMERO.txt                  (Instrucciones iniciales)
│
├── 📚 DOCUMENTACIÓN ANALIZADORES (5)
│   ├── README_ASCENDENTE.md              (Doc técnica ascendente)
│   ├── RESUMEN_PROYECTO.md               (Resumen ejecutivo)
│   ├── COMPARACION_PROYECTOS.md          (Comparación LL vs LR)
│   ├── GUIA_USO.md                       (Guía de uso)
│   └── INDICE_ARCHIVOS.md                (Índice anterior)
│
├── 📚 DOCUMENTACIÓN MÁQUINAS DE TURING (2)
│   ├── README_TURING.md                  (Documentación completa MT)
│   └── RESUMEN_TURING.md                 (Resumen ejecutivo MT)
│
├── 📚 DOCUMENTACIÓN TÉCNICA (docs/)
│   ├── VALIDACION_COMPLETA.md            (Validación descendente)
│   ├── RESULTADOS_PRUEBAS.md             (Resultados 62 pruebas)
│   └── GUIA_USO.md                       (Manual de usuario)
│
├── 🔧 ARCHIVOS DE DESARROLLO
│   ├── debug_ascendente.py               (Debug auxiliar)
│   └── __pycache__/                      (Cache de Python)
│
├── 📋 ÍNDICES
│   ├── INDICE_ARCHIVOS.md                (Índice anterior)
│   └── INDICE_ARCHIVOS_COMPLETO.md       ← ESTE ARCHIVO
│
└── 🔄 CONTROL DE VERSIONES
    ├── .git/                             (Repositorio Git)
    └── .gitignore                        (Archivos ignorados)
```

---

## 🎓 CONTENIDO POR PROYECTO

### PROYECTO 1: Analizador Descendente (LL)
**Archivos:**
- `programa.py` (656 líneas)
- `test_programa.py` (62 tests)
- `prueba_rapida.py`
- `prueba_errores.py`
- `docs/VALIDACION_COMPLETA.md`
- `docs/RESULTADOS_PRUEBAS.md`

**Características:**
- Parser recursivo descendente
- Gramática LL(1)
- Operadores: `+`, `-`, `*`, `/`, `%`, `**`, `^`
- GUI con Tkinter
- 62 tests (100% passing)

---

### PROYECTO 2: Analizador Ascendente (LR)
**Archivos:**
- `analizador_ascendente.py` (711 líneas)
- `test_analizador_funcional.py` (29 tests)
- `test_analizador_ascendente.py`
- `README_ASCENDENTE.md`
- `RESUMEN_PROYECTO.md`
- `COMPARACION_PROYECTOS.md`
- `GUIA_USO.md`

**Características:**
- Algoritmo Shift-Reduce
- Asignaciones: `var = expresión`
- Multiplicación implícita: `7(3)` → `7*(3)`
- Traza completa Shift-Reduce
- GUI con 4 pestañas
- 29 tests (100% passing)

---

### PROYECTO 3: Máquina de Turing - Aritmética
**Archivos:**
- `maquina_turing_aritmetica.py` (580 líneas)
- `README_TURING.md` (sección aritmética)
- `RESUMEN_TURING.md` (sección aritmética)

**Características:**
- Suma unaria: `111+11 → 11111` (3+2=5)
- Multiplicación unaria: `11*111 → 111111` (2×3=6)
- Visualización de cinta y cabezal
- 8 ejemplos predefinidos
- GUI con 4 pestañas

---

### PROYECTO 4: Máquina de Turing - Lenguajes
**Archivos:**
- `maquina_turing_lenguajes.py` (650 líneas)
- `README_TURING.md` (sección lenguajes)
- `RESUMEN_TURING.md` (sección lenguajes)

**Características:**
- L = {a^n b^n}: Igual número de a's y b's
- Palíndromos: Cadenas simétricas
- L = {a^n b^2n}: Doble de b's que a's
- Tablas de transiciones completas
- 13 ejemplos predefinidos
- GUI con 4 pestañas

---

## ✅ VALIDACIÓN DEL PROYECTO

### Analizadores Sintácticos
- ✅ 91/91 tests pasando (100%)
- ✅ Ambos programas funcionando
- ✅ GUIs operativas
- ✅ Documentación completa

### Máquinas de Turing
- ✅ 2 programas completos
- ✅ 5 operaciones/lenguajes diferentes
- ✅ 21 ejemplos interactivos
- ✅ Documentación exhaustiva
- ✅ Diferenciación con ejemplos de clase

---

## 🚀 PRÓXIMOS PASOS

### Si Quieres Ejecutar
1. Abre cualquiera de los 4 programas principales
2. Interactúa con la GUI
3. Prueba los ejemplos predefinidos

### Si Quieres Entender
1. Lee `README.md` (visión general)
2. Lee documentación específica de cada proyecto
3. Revisa el código fuente

### Si Quieres Validar
1. Ejecuta los tests: `python test_*.py`
2. Verifica los 91 tests pasando
3. Prueba casos de borde en las GUIs

---

## 📞 SOPORTE

### Documentación Principal
- **README.md**: Información general de los 4 proyectos
- **README_TURING.md**: Todo sobre Máquinas de Turing
- **README_ASCENDENTE.md**: Todo sobre analizador ascendente

### ¿Tienes Dudas?
1. Consulta la documentación específica del proyecto
2. Revisa los ejemplos en las GUIs
3. Ejecuta los tests para verificar funcionamiento

---

## 🎉 RESUMEN FINAL

### 4 Proyectos Completos
✅ Analizador Descendente (LL) - 656 líneas, 62 tests
✅ Analizador Ascendente (LR) - 711 líneas, 29 tests  
✅ MT Aritmética Unaria - 580 líneas, 8 ejemplos
✅ MT Lenguajes Formales - 650 líneas, 13 ejemplos

### Estadísticas Totales
📊 ~2,600 líneas de código
📊 ~2,300 líneas de documentación
📊 91 tests automatizados
📊 42 ejemplos interactivos
📊 11 archivos de documentación

### Calidad del Proyecto
⭐ 100% tests pasando
⭐ Código bien estructurado
⭐ Documentación exhaustiva
⭐ GUIs profesionales
⭐ Fundamentos teóricos sólidos

---

**🎓 PROYECTO ACADÉMICO DE TEORÍA DE LA COMPUTACIÓN**

*Implementación completa de Analizadores Sintácticos (LL y LR) y Máquinas de Turing (Aritmética y Lenguajes) con interfaces gráficas y documentación profesional.*

---

**Última actualización:** 26 de noviembre de 2025  
**Autores:** Juan Esteban Cardozo Rivera, Juan Sebastián Gómez Usuga  
**Estado:** ✅ PROYECTO COMPLETO
