# Analizador Sintáctico Descendente Recursivo - Calculadora

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-62%2F62%20passing-brightgreen.svg)

Implementación de un analizador sintáctico descendente recursivo (parser LL(1)) para evaluar expresiones matemáticas con interfaz gráfica.

## 👥 Autores

- **Juan Esteban Cardozo Rivera**
- **Juan Sebastián Gómez Usuga**

## 📋 Descripción

Este proyecto implementa un compilador simplificado que realiza:
- **Análisis Léxico**: Tokenización mediante expresiones regulares
- **Análisis Sintáctico**: Parser descendente recursivo LL(1)
- **Evaluación Semántica**: Cálculo de expresiones aritméticas
- **Interfaz Gráfica**: Aplicación completa con Tkinter

## ✨ Características

### Operadores Soportados
- ➕ Suma (`+`)
- ➖ Resta (`-`)
- ✖️ Multiplicación (`*`)
- ➗ División (`/`)
- 📐 Módulo (`%`)
- 🔢 Potenciación (`**` o `^`)
- 🔤 Paréntesis (`()`)
- ➖ Números negativos

### Funcionalidades
- ✅ Análisis léxico completo
- ✅ Análisis sintáctico con gramática LL(1)
- ✅ Evaluación precisa de expresiones
- ✅ Traza de derivación en tiempo real
- ✅ Manejo robusto de errores
- ✅ Historial de cálculos
- ✅ Exportación de resultados
- ✅ 10 ejemplos interactivos

## 📐 Gramática

```
E  → T E'
E' → + T E' | - T E' | ε
T  → P T'
T' → * P T' | / P T' | % P T' | ε
P  → F P'
P' → ** F P' | ^ F P' | ε
F  → ( E ) | número | -número
```

**Tipo**: Gramática Libre de Contexto (GLC)  
**Parser**: LL(1) - Análisis Descendente Recursivo  
**Precedencia**: `()` > `**` > `* / %` > `+ -`

## 🚀 Instalación

### Requisitos
- Python 3.8 o superior
- Tkinter (incluido con Python en Windows)

### Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/analizador-sintactico.git
cd analizador-sintactico
```

### Ejecutar el programa
```bash
python programa.py
```

## 🧪 Pruebas

El proyecto incluye una suite completa de 62 pruebas automatizadas.

### Ejecutar todas las pruebas
```bash
# Suite completa (44 tests unitarios)
python test_programa.py

# Pruebas rápidas (8 tests)
python prueba_rapida.py

# Pruebas de errores (10 tests)
python prueba_errores.py
```

### Resultados
```
✅ 62 pruebas ejecutadas
✅ 62 exitosas (100%)
❌ 0 fallidas (0%)
```

## 📖 Uso

### Interfaz Gráfica

1. **Ingresar expresión**: Escribe la expresión en el campo de entrada
2. **Analizar**: Presiona Enter o el botón "Analizar"
3. **Ver resultados**: Navega por las pestañas para ver:
   - 📊 Resultado de la evaluación
   - 🔤 Tokens identificados
   - 🌳 Traza de derivación
   - 📐 Gramática utilizada

### Ejemplos de Uso

```python
# Operaciones básicas
2 + 3           → 5.0
5 * 4           → 20.0
10 / 2          → 5.0
10 % 3          → 1.0
2 ** 3          → 8.0

# Precedencia de operadores
2 + 3 * 4       → 14.0  (no 20)
2 * 3 ** 2      → 18.0  (no 36)

# Paréntesis
(2 + 3) * 4     → 20.0
((2+3)*(4-1))/2 → 7.5

# Números decimales y negativos
3.5 + 2.5       → 6.0
-5 + 3          → -2.0
-(5 + 3)        → -8.0

# Expresiones complejas
2 ** 3 + 10 % 3 * 2              → 10.0
(2 + 3) * 4 - 10 / 2 + 3 ** 2   → 24.0
```

## 🎯 Casos de Prueba

### ✅ Pruebas Exitosas
- Operaciones básicas (7 tests)
- Precedencia de operadores (4 tests)
- Paréntesis y anidamiento (5 tests)
- Números decimales (4 tests)
- Números negativos (4 tests)
- Expresiones complejas (4 tests)
- Tokenización (3 tests)
- Casos extremos (5 tests)

### ❌ Detección de Errores
- División por cero
- Módulo por cero
- Caracteres inválidos
- Paréntesis desbalanceados
- Sintaxis incorrecta
- Expresiones incompletas

## 📁 Estructura del Proyecto

```
Lab2/
├── programa.py                 # Programa principal con interfaz gráfica
├── test_programa.py           # Suite completa de 44 pruebas
├── prueba_rapida.py          # 8 pruebas rápidas
├── prueba_errores.py         # 10 pruebas de errores
├── README.md                  # Este archivo
├── LICENSE                    # Licencia MIT
├── .gitignore                # Archivos ignorados por Git
└── docs/
    ├── VALIDACION_COMPLETA.md    # Resumen de validación
    ├── RESULTADOS_PRUEBAS.md     # Resultados detallados
    ├── GUIA_USO.md               # Guía completa de uso
    └── RESUMEN_FINAL.txt         # Resumen ejecutivo
```

## 🛠️ Tecnologías

- **Lenguaje**: Python 3.8+
- **GUI**: Tkinter
- **Testing**: unittest
- **Regex**: re (expresiones regulares)

## 📊 Rendimiento

- **Tiempo de análisis**: < 0.001 segundos por expresión
- **Suite de pruebas**: 0.020 segundos (62 tests)
- **Uso de memoria**: Mínimo
- **Estabilidad**: 100% de pruebas exitosas

## 🎓 Contexto Académico

Este proyecto fue desarrollado como parte del laboratorio de **Análisis Sintáctico** en el curso de Compiladores/Lenguajes de Programación. Cumple con todos los requisitos:

- ✅ Analizador sintáctico implementado
- ✅ Tokens reconocidos correctamente
- ✅ Resultados de operaciones presentados
- ✅ Errores de sintaxis indicados
- ✅ Implementado en Python
- ✅ Modo gráfico funcional

## 📄 Documentación

La documentación completa está disponible en la carpeta `docs/`:

- **VALIDACION_COMPLETA.md**: Resumen ejecutivo del proyecto
- **RESULTADOS_PRUEBAS.md**: Documentación detallada de las 62 pruebas
- **GUIA_USO.md**: Manual completo de usuario
- **RESUMEN_FINAL.txt**: Vista general del proyecto

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

**Juan Esteban Cardozo Rivera** - [GitHub](https://github.com/TU_USUARIO)  
**Juan Sebastián Gómez Usuga** - [GitHub](https://github.com/TU_USUARIO)

## 🙏 Agradecimientos

- Curso de Compiladores/Lenguajes de Programación
- Comunidad de Python
- Documentación de Tkinter

---

**Estado del Proyecto**: ✅ Completo y Validado  
**Última Actualización**: 12 de noviembre de 2025

⭐ Si te gusta este proyecto, no olvides darle una estrella!
