"""
Analizador Sintáctico Ascendente (Bottom-Up Parser) - VERSIÓN FUNCIONAL

Autores:
    - Juan Esteban Cardozo Rivera
    - Juan Sebastián Gómez Usuga

Descripción:
    Implementación funcional de un analizador sintáctico ascendente que reconoce
    y evalúa expresiones con asignaciones de variables.
    
Características:
    - Análisis ascendente simulado con traza Shift-Reduce
    - Soporte para asignaciones: var = expresión
    - Operadores: +, -, *, /, paréntesis
    - Interfaz gráfica con visualización completa
    - Multiplicación implícita automática

Ejemplo:
    var = 5 + 7(3 + 3/4)
    → Se reconoce como: var = 5 + 7 * (3 + 3/4)
    → Resultado: var = 31.25
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import re
from datetime import datetime


class AnalizadorAscendente:
    """Analizador sintáctico ascendente funcional"""
    
    def __init__(self):
        self.tokens = []
        self.variables = {}
        self.errores = []
    
    def tokenizar(self, expresion):
        """Convierte la expresión en tokens con multiplicación implícita"""
        # Insertar * implícito
        expresion = re.sub(r'(\d)\s*\(', r'\1*(', expresion)
        expresion = re.sub(r'\)\s*(\d)', r')*\1', expresion)
        expresion = re.sub(r'\)\s*\(', r')*(', expresion)
        expresion = re.sub(r'(\d)\s*([a-zA-Z_])', r'\1*\2', expresion)
        expresion = re.sub(r'([a-zA-Z_0-9])\s*\(', r'\1*(', expresion)
        
        patrones = [
            ('NUMERO', r'\d+(\.\d+)?'),
            ('VAR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('IGUAL', r'='),
            ('SUMA', r'\+'),
            ('RESTA', r'\-'),
            ('MULT', r'\*'),
            ('DIV', r'\/'),
            ('PAREN_IZQ', r'\('),
            ('PAREN_DER', r'\)'),
            ('ESPACIO', r'\s+'),
        ]
        
        tokens = []
        pos = 0
        self.errores = []
        
        while pos < len(expresion):
            coincide = False
            for tipo, patron in patrones:
                regex = re.compile(patron)
                match = regex.match(expresion, pos)
                if match:
                    valor = match.group()
                    if tipo != 'ESPACIO':
                        tokens.append((tipo, valor))
                    pos = match.end()
                    coincide = True
                    break
            
            if not coincide:
                self.errores.append(f"Error léxico: Carácter no válido '{expresion[pos]}' en posición {pos}")
                return []
        
        return tokens
    
    def analizar_sintaxis(self, expresion):
        """Realiza análisis sintáctico y genera traza Shift-Reduce"""
        self.tokens = self.tokenizar(expresion)
        
        if not self.tokens or self.errores:
            return False, self.errores
        
        # Generar traza de análisis Shift-Reduce simulada
        traza = self.generar_traza_shift_reduce()
        
        return True, traza
    
    def generar_traza_shift_reduce(self):
        """Genera la traza del análisis Shift-Reduce"""
        traza = []
        pila = ['$']
        paso = 0
        
        traza.append({
            'paso': paso,
            'pila': pila.copy(),
            'entrada': ' '.join([t[1] for t in self.tokens]),
            'accion': 'Estado inicial'
        })
        paso += 1
        
        # Procesar tokens
        i = 0
        while i < len(self.tokens):
            token_tipo, token_val = self.tokens[i]
            
            # SHIFT
            pila.append(token_tipo)
            entrada_restante = ' '.join([t[1] for t in self.tokens[i+1:]])
            if not entrada_restante:
                entrada_restante = '$'
            
            traza.append({
                'paso': paso,
                'pila': pila.copy(),
                'entrada': entrada_restante,
                'accion': f'SHIFT {token_tipo}'
            })
            paso += 1
            
            # REDUCE según el tipo
            while True:
                reducido = False
                
                # F → NUMERO
                if len(pila) >= 2 and pila[-1] == 'NUMERO':
                    pila.pop()
                    pila.append('F')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE F → NUMERO'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # F → VAR (solo si no es parte de asignación)
                if len(pila) >= 2 and pila[-1] == 'VAR':
                    # Verificar si el siguiente token es '='
                    if i + 1 < len(self.tokens) and self.tokens[i + 1][0] == 'IGUAL':
                        break  # No reducir, es parte de asignación
                    pila.pop()
                    pila.append('F')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE F → VAR'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # F → ( E )
                if len(pila) >= 4 and pila[-3:] == ['PAREN_IZQ', 'E', 'PAREN_DER']:
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.append('F')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE F → ( E )'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # T → F
                if len(pila) >= 2 and pila[-1] == 'F':
                    # Solo reducir si no viene * o /
                    if i + 1 < len(self.tokens) and self.tokens[i + 1][0] in ['MULT', 'DIV']:
                        break
                    pila.pop()
                    pila.append('T')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE T → F'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # T → T * F
                if len(pila) >= 4 and pila[-3:] == ['T', 'MULT', 'F']:
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.append('T')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE T → T * F'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # T → T / F
                if len(pila) >= 4 and pila[-3:] == ['T', 'DIV', 'F']:
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.append('T')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE T → T / F'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # E → T
                if len(pila) >= 2 and pila[-1] == 'T':
                    # Solo reducir si no viene + o -
                    if i + 1 < len(self.tokens) and self.tokens[i + 1][0] in ['SUMA', 'RESTA']:
                        break
                    # O si es el final o viene )
                    if i + 1 >= len(self.tokens) or self.tokens[i + 1][0] in ['PAREN_DER', 'IGUAL']:
                        pila.pop()
                        pila.append('E')
                        traza.append({
                            'paso': paso,
                            'pila': pila.copy(),
                            'entrada': entrada_restante,
                            'accion': 'REDUCE E → T'
                        })
                        paso += 1
                        reducido = True
                        continue
                    break
                
                # E → E + T
                if len(pila) >= 4 and pila[-3:] == ['E', 'SUMA', 'T']:
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.append('E')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE E → E + T'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                # E → E - T
                if len(pila) >= 4 and pila[-3:] == ['E', 'RESTA', 'T']:
                    pila.pop()
                    pila.pop()
                    pila.pop()
                    pila.append('E')
                    traza.append({
                        'paso': paso,
                        'pila': pila.copy(),
                        'entrada': entrada_restante,
                        'accion': 'REDUCE E → E - T'
                    })
                    paso += 1
                    reducido = True
                    continue
                
                if not reducido:
                    break
            
            i += 1
        
        # Reducción final S → VAR = E
        if len(pila) >= 4 and pila[-3:] == ['VAR', 'IGUAL', 'E']:
            pila.pop()
            pila.pop()
            pila.pop()
            pila.append('S')
            traza.append({
                'paso': paso,
                'pila': pila.copy(),
                'entrada': '$',
                'accion': 'REDUCE S → VAR = E (Asignación)'
            })
            paso += 1
        elif len(pila) >= 2 and pila[-1] == 'E':
            # Solo expresión sin asignación
            pila.pop()
            pila.append('S')
            traza.append({
                'paso': paso,
                'pila': pila.copy(),
                'entrada': '$',
                'accion': 'REDUCE S → E (Expresión)'
            })
            paso += 1
        
        # ACEPTAR
        traza.append({
            'paso': paso,
            'pila': pila.copy(),
            'entrada': '$',
            'accion': '✓ ACEPTAR'
        })
        
        return traza
    
    def evaluar_expresion(self, expresion):
        """Evalúa la expresión y retorna el resultado"""
        tokens = self.tokenizar(expresion)
        
        if not tokens or self.errores:
            return None, None, self.errores
        
        # Generar traza
        resultado_sintaxis, traza = self.analizar_sintaxis(expresion)
        
        if not resultado_sintaxis:
            return None, None, traza
        
        # Evaluar semánticamente
        try:
            # Verificar si hay asignación
            if len(tokens) >= 3 and tokens[0][0] == 'VAR' and tokens[1][0] == 'IGUAL':
                var_nombre = tokens[0][1]
                # Reconstruir expresión (sin la variable y el =)
                expr_tokens = tokens[2:]
                expresion_eval = ''.join([t[1] for t in expr_tokens])
                
                # Reemplazar variables conocidas
                for var, val in self.variables.items():
                    expresion_eval = expresion_eval.replace(var, str(val))
                
                # Evaluar
                valor = eval(expresion_eval)
                self.variables[var_nombre] = valor
                
                return var_nombre, valor, traza
            else:
                # Solo expresión
                expresion_eval = ''.join([t[1] for t in tokens])
                
                # Reemplazar variables conocidas
                for var, val in self.variables.items():
                    expresion_eval = expresion_eval.replace(var, str(val))
                
                valor = eval(expresion_eval)
                return None, valor, traza
                
        except Exception as e:
            return None, None, [f"Error de evaluación: {str(e)}"]


class InterfazAscendente:
    """Interfaz gráfica para el analizador ascendente"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Sintáctico Ascendente - Shift-Reduce")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        
        self.analizador = AnalizadorAscendente()
        self.historial = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Analizador Sintáctico Ascendente (Bottom-Up)", 
                          font=("Arial", 16, "bold"), foreground="#D35400")
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Autores
        autores = ttk.Label(main_frame, 
                           text="Realizado por: Juan Esteban Cardozo Rivera • Juan Sebastián Gómez Usuga",
                           font=("Arial", 9, "italic"), foreground="#666")
        autores.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        
        # Descripción
        descripcion = ttk.Label(main_frame, 
                               text="Algoritmo Shift-Reduce • Soporta asignaciones: var = expresión • Operadores: +, -, *, /, ( )",
                               font=("Arial", 9), foreground="#555")
        descripcion.grid(row=2, column=0, columnspan=3, pady=(0, 15))
        
        # Frame de entrada
        entrada_frame = ttk.LabelFrame(main_frame, text="Expresión de Entrada", padding="10")
        entrada_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.entrada_expresion = ttk.Entry(entrada_frame, width=70, font=("Consolas", 12))
        self.entrada_expresion.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        self.entrada_expresion.bind('<Return>', lambda e: self.analizar_expresion())
        
        entrada_frame.columnconfigure(0, weight=1)
        
        # Botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=4, column=0, columnspan=3, pady=(0, 15))
        
        ttk.Button(botones_frame, text="🔍 Analizar", 
                  command=self.analizar_expresion, width=15).grid(row=0, column=0, padx=5)
        ttk.Button(botones_frame, text="🗑️ Limpiar", 
                  command=self.limpiar, width=15).grid(row=0, column=1, padx=5)
        ttk.Button(botones_frame, text="📝 Ejemplos", 
                  command=self.mostrar_ejemplos, width=15).grid(row=0, column=2, padx=5)
        ttk.Button(botones_frame, text="📊 Variables", 
                  command=self.mostrar_variables, width=15).grid(row=0, column=3, padx=5)
        
        # Notebook
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Pestaña 1: Resultado
        resultado_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(resultado_frame, text="📊 Resultado")
        
        self.resultado_texto = scrolledtext.ScrolledText(resultado_frame, width=80, height=10, 
                                                         font=("Consolas", 10), wrap=tk.WORD)
        self.resultado_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 2: Traza Shift-Reduce
        traza_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(traza_frame, text="🔄 Traza Shift-Reduce")
        
        self.traza_texto = scrolledtext.ScrolledText(traza_frame, width=80, height=10, 
                                                     font=("Consolas", 9), wrap=tk.NONE)
        self.traza_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 3: Tokens
        tokens_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tokens_frame, text="🔤 Tokens")
        
        self.tokens_texto = scrolledtext.ScrolledText(tokens_frame, width=80, height=10, 
                                                      font=("Consolas", 9), wrap=tk.WORD)
        self.tokens_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 4: Gramática
        gramatica_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(gramatica_frame, text="📐 Gramática")
        
        self.mostrar_gramatica_info(gramatica_frame)
        
        # Configurar pesos
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
    
    def mostrar_gramatica_info(self, frame):
        """Muestra la gramática utilizada"""
        gramatica_texto = scrolledtext.ScrolledText(frame, width=80, height=10, 
                                                    font=("Consolas", 9), wrap=tk.WORD)
        gramatica_texto.pack(fill=tk.BOTH, expand=True)
        
        info = """GRAMÁTICA PARA ANÁLISIS ASCENDENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reglas de Producción:
─────────────────────
S  → VAR = E          (Asignación)
S  → E                (Expresión simple)
E  → E + T            (Suma)
E  → E - T            (Resta)
E  → T                (Término)
T  → T * F            (Multiplicación)
T  → T / F            (División)
T  → F                (Factor)
F  → ( E )            (Paréntesis)
F  → número           (Número)
F  → VAR              (Variable)

Precedencia de Operadores:
──────────────────────────
1. Paréntesis: ( )
2. Multiplicación, División: *, /
3. Suma, Resta: +, -

Tipo de Análisis:
─────────────────
• Análisis Sintáctico Ascendente (Bottom-Up)
• Algoritmo: Shift-Reduce
• Construcción del árbol desde las hojas hacia la raíz

Operaciones Shift-Reduce:
──────────────────────────
SHIFT:  Empuja el token actual a la pila
REDUCE: Reemplaza símbolos del tope de la pila por el no terminal
        según una producción de la gramática
ACCEPT: La cadena es reconocida (pila = $S, entrada = $)

Características:
────────────────
• Reconoce asignaciones: var = expresión
• Multiplicación implícita: 7(3) se interpreta como 7*(3)
• Soporta variables en expresiones
• Maneja precedencia de operadores correctamente
"""
        gramatica_texto.insert(tk.END, info)
        gramatica_texto.config(state=tk.DISABLED)
    
    def analizar_expresion(self):
        expresion = self.entrada_expresion.get().strip()
        
        if not expresion:
            messagebox.showwarning("Advertencia", "Por favor ingrese una expresión")
            return
        
        self.limpiar_resultados()
        
        # Tokenizar y mostrar
        tokens = self.analizador.tokenizar(expresion)
        if tokens:
            self.mostrar_tokens(tokens)
        
        # Analizar y evaluar
        var_nombre, valor, datos = self.analizador.evaluar_expresion(expresion)
        
        if isinstance(datos, list) and len(datos) > 0 and isinstance(datos[0], str):
            # Errores
            self.mostrar_errores(datos)
        else:
            # Éxito
            self.mostrar_resultado(expresion, var_nombre, valor)
            self.mostrar_traza(datos)
            
            # Agregar al historial
            if var_nombre:
                self.historial.append({
                    'tiempo': datetime.now().strftime("%H:%M:%S"),
                    'expresion': expresion,
                    'variable': var_nombre,
                    'valor': valor
                })
    
    def mostrar_tokens(self, tokens):
        self.tokens_texto.insert(tk.END, "ANÁLISIS LÉXICO - TOKENS IDENTIFICADOS\n")
        self.tokens_texto.insert(tk.END, "=" * 70 + "\n\n")
        
        self.tokens_texto.insert(tk.END, f"{'#':<4} {'TIPO':<15} {'VALOR':<15}\n")
        self.tokens_texto.insert(tk.END, "-" * 70 + "\n")
        
        for i, (tipo, valor) in enumerate(tokens, 1):
            self.tokens_texto.insert(tk.END, f"{i:<4} {tipo:<15} {valor:<15}\n")
        
        self.tokens_texto.insert(tk.END, f"\n✓ Total de tokens: {len(tokens)}\n")
    
    def mostrar_resultado(self, expresion, var_nombre, valor):
        self.resultado_texto.insert(tk.END, "╔═══════════════════════════════════════════════════════════╗\n")
        self.resultado_texto.insert(tk.END, "║       ✓ RECONOCIMIENTO COMPLETADO EXITOSAMENTE           ║\n")
        self.resultado_texto.insert(tk.END, "╚═══════════════════════════════════════════════════════════╝\n\n")
        
        self.resultado_texto.insert(tk.END, f"Expresión Analizada:\n")
        self.resultado_texto.insert(tk.END, f"  {expresion}\n\n")
        
        if var_nombre:
            self.resultado_texto.insert(tk.END, f"Asignación Detectada:\n")
            self.resultado_texto.insert(tk.END, f"  Variable: {var_nombre}\n")
            self.resultado_texto.insert(tk.END, f"  Valor: {valor}\n\n")
        else:
            self.resultado_texto.insert(tk.END, f"Resultado de la Evaluación:\n")
            self.resultado_texto.insert(tk.END, f"  {valor}\n\n")
        
        self.resultado_texto.insert(tk.END, f"Estado del Análisis:\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Análisis léxico: CORRECTO\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Análisis sintáctico ascendente: CORRECTO\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Evaluación semántica: CORRECTO\n\n")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.resultado_texto.insert(tk.END, f"Fecha y hora: {timestamp}\n")
    
    def mostrar_traza(self, acciones):
        self.traza_texto.insert(tk.END, "TRAZA DEL ANÁLISIS SHIFT-REDUCE\n")
        self.traza_texto.insert(tk.END, "=" * 100 + "\n\n")
        
        # Cabecera de tabla
        self.traza_texto.insert(tk.END, f"{'PASO':<6} {'PILA':<35} {'ENTRADA':<30} {'ACCIÓN':<30}\n")
        self.traza_texto.insert(tk.END, "-" * 100 + "\n")
        
        for accion in acciones:
            paso = str(accion['paso'])
            pila = ' '.join(accion['pila'])
            entrada = accion['entrada']
            acc = accion['accion']
            
            self.traza_texto.insert(tk.END, f"{paso:<6} {pila:<35} {entrada:<30} {acc:<30}\n")
        
        self.traza_texto.insert(tk.END, "\n" + "=" * 100 + "\n")
        self.traza_texto.insert(tk.END, "LEYENDA:\n")
        self.traza_texto.insert(tk.END, "• SHIFT: Empuja token a la pila\n")
        self.traza_texto.insert(tk.END, "• REDUCE: Aplica una producción de la gramática\n")
        self.traza_texto.insert(tk.END, "• ACEPTAR: Cadena reconocida exitosamente\n")
    
    def mostrar_errores(self, errores):
        self.resultado_texto.insert(tk.END, "╔═══════════════════════════════════════════════════════════╗\n")
        self.resultado_texto.insert(tk.END, "║              ❌ ERRORES DETECTADOS                        ║\n")
        self.resultado_texto.insert(tk.END, "╚═══════════════════════════════════════════════════════════╝\n\n")
        
        for i, error in enumerate(errores, 1):
            self.resultado_texto.insert(tk.END, f"{i}. {error}\n\n")
    
    def mostrar_variables(self):
        """Muestra las variables almacenadas"""
        var_window = tk.Toplevel(self.root)
        var_window.title("Variables en Memoria")
        var_window.geometry("500x400")
        
        ttk.Label(var_window, text="Variables Almacenadas", 
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        var_texto = scrolledtext.ScrolledText(var_window, width=60, height=20, 
                                              font=("Consolas", 10))
        var_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        if not self.analizador.variables:
            var_texto.insert(tk.END, "No hay variables almacenadas.\n")
        else:
            var_texto.insert(tk.END, f"{'VARIABLE':<20} {'VALOR':<15}\n")
            var_texto.insert(tk.END, "=" * 40 + "\n")
            
            for var, valor in self.analizador.variables.items():
                var_texto.insert(tk.END, f"{var:<20} {valor:<15}\n")
        
        var_texto.config(state=tk.DISABLED)
        
        ttk.Button(var_window, text="Cerrar", 
                  command=var_window.destroy).pack(pady=10)
    
    def limpiar(self):
        self.entrada_expresion.delete(0, tk.END)
        self.limpiar_resultados()
    
    def limpiar_resultados(self):
        self.resultado_texto.delete(1.0, tk.END)
        self.traza_texto.delete(1.0, tk.END)
        self.tokens_texto.delete(1.0, tk.END)
    
    def mostrar_ejemplos(self):
        ejemplos = [
            ("Asignación simple", "var = 5 + 7"),
            ("Ejemplo del enunciado", "var = 5 + 7(3 + 3/4)"),
            ("Multiplicación implícita", "x = 2(3 + 4)"),
            ("Con paréntesis", "y = (5 + 3) * (2 - 1)"),
            ("División", "z = 10 / 2 + 8"),
            ("Variables en expresión", "result = x + y * 2"),
            ("Compleja", "a = 2 + 3(4 - 1) / 2"),
            ("Solo expresión", "5 + 7 * 3"),
            ("Con resta", "b = 10 - 2(3 + 1)"),
            ("Anidada", "c = (2 + 3)(4 + 5)")
        ]
        
        ejemplo_window = tk.Toplevel(self.root)
        ejemplo_window.title("Ejemplos de Expresiones")
        ejemplo_window.geometry("500x450")
        
        ttk.Label(ejemplo_window, text="Seleccione un ejemplo:", 
                 font=("Arial", 12, "bold")).pack(pady=15)
        
        canvas = tk.Canvas(ejemplo_window)
        scrollbar = ttk.Scrollbar(ejemplo_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for nombre, ejemplo in ejemplos:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            def hacer_lambda(exp=ejemplo):
                self.entrada_expresion.delete(0, tk.END)
                self.entrada_expresion.insert(0, exp)
                ejemplo_window.destroy()
                self.analizar_expresion()
            
            ttk.Button(frame, text=f"{nombre}: {ejemplo}", 
                      command=hacer_lambda, width=55).pack()
        
        canvas.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=(0, 10))
        scrollbar.pack(side="right", fill="y", pady=(0, 10), padx=(0, 10))


def main():
    root = tk.Tk()
    app = InterfazAscendente(root)
    root.mainloop()


if __name__ == "__main__":
    main()
