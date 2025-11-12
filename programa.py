"""
Analizador Sintáctico Descendente Recursivo - Calculadora Avanzada

Autores:
    - Juan Esteban Cardozo Rivera
    - Juan Sebastián Gómez Usuga

Descripción:
    Implementación de un analizador sintáctico descendente recursivo (parser LL(1))
    para evaluar expresiones matemáticas. Incluye análisis léxico, sintáctico y
    evaluación semántica con soporte para múltiples operadores aritméticos.

Características:
    - Análisis léxico con tokenización mediante expresiones regulares
    - Análisis sintáctico descendente recursivo
    - Soporte para operadores: +, -, *, /, %, ** (potenciación)
    - Manejo de paréntesis y precedencia de operadores
    - Interfaz gráfica con tkinter
    - Historial de cálculos y exportación de resultados

Gramática:
    E  → T E'
    E' → + T E' | - T E' | ε
    T  → P T'
    T' → * P T' | / P T' | % P T' | ε
    P  → F P'
    P' → ** F P' | ^ F P' | ε
    F  → ( E ) | número | -número
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import re
from datetime import datetime

class CalculadoraDescendente:
    def __init__(self):
        self.tokens = []
        self.posicion = 0
        self.errores = []
        self.traza_derivacion = []  # Para guardar el árbol de derivación
        
    def analizar(self, expresion):
        """Método principal para analizar la expresión"""
        self.tokens = self.tokenizar(expresion)
        self.posicion = 0
        self.errores = []
        self.traza_derivacion = []  # Reiniciar traza
        
        if not self.tokens:
            return None, ["Error: Expresión vacía"]
            
        try:
            self.traza_derivacion.append("Inicio del análisis sintáctico")
            resultado = self.E()
            if self.posicion < len(self.tokens):
                tokens_restantes = ' '.join([t[1] for t in self.tokens[self.posicion:]])
                self.errores.append(f"Error de sintaxis: Caracteres adicionales después de la expresión válida: '{tokens_restantes}'")
                return None, self.errores
            self.traza_derivacion.append("✓ Análisis sintáctico completado exitosamente")
            return resultado, self.errores
        except Exception as e:
            self.errores.append(f"Error de sintaxis: {str(e)}")
            return None, self.errores
    
    def tokenizar(self, expresion):
        """Convierte la expresión en una lista de tokens"""
        # Patrones para tokens
        patrones = [
            ('NUMERO', r'\d+(\.\d+)?'),      # Números enteros o decimales
            ('POT', r'\*\*|\^'),             # Potenciación (** o ^)
            ('MOD', r'%'),                   # Módulo
            ('SUMA', r'\+'),                 # Suma
            ('RESTA', r'\-'),                # Resta
            ('MULT', r'\*'),                 # Multiplicación
            ('DIV', r'\/'),                  # División
            ('PAREN_IZQ', r'\('),            # Paréntesis izquierdo
            ('PAREN_DER', r'\)'),            # Paréntesis derecho
            ('ESPACIO', r'\s+'),             # Espacios (se ignoran)
        ]
        
        tokens = []
        pos = 0
        
        while pos < len(expresion):
            coincide = False
            for tipo, patron in patrones:
                regex = re.compile(patron)
                match = regex.match(expresion, pos)
                if match:
                    valor = match.group()
                    if tipo != 'ESPACIO':  # Ignorar espacios
                        tokens.append((tipo, valor))
                    pos = match.end()
                    coincide = True
                    break
            
            if not coincide:
                # Caracter no reconocido
                self.errores.append(f"Error léxico: Caracter no válido '{expresion[pos]}' en la posición {pos}")
                self.errores.append(f"  Sugerencia: Solo se permiten números, operadores (+, -, *, /, **, ^, %) y paréntesis")
                return []
        
        return tokens
    
    def token_actual(self):
        """Retorna el token actual"""
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        return ('EOF', '')
    
    def consumir(self, tipo_esperado=None):
        """Consume el token actual y avanza a la siguiente posición"""
        if self.posicion >= len(self.tokens):
            raise Exception(f"Se esperaba '{tipo_esperado}' pero la expresión terminó inesperadamente")
            
        token_actual = self.tokens[self.posicion]
        
        if tipo_esperado and token_actual[0] != tipo_esperado:
            raise Exception(f"Se esperaba '{tipo_esperado}' pero se encontró '{token_actual[1]}'")
            
        self.posicion += 1
        return token_actual
    
    def E(self):
        """E → T E'"""
        self.traza_derivacion.append(f"  E → T E' (posición {self.posicion})")
        resultado = self.T()
        return self.E_prima(resultado)
    
    def E_prima(self, resultado_anterior):
        """E' → + T E' | - T E' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'SUMA':
            self.traza_derivacion.append(f"    E' → + T E' (sumando {resultado_anterior} + ...)")
            self.consumir('SUMA')
            resultado = resultado_anterior + self.T()
            return self.E_prima(resultado)
        elif token_actual[0] == 'RESTA':
            self.traza_derivacion.append(f"    E' → - T E' (restando {resultado_anterior} - ...)")
            self.consumir('RESTA')
            resultado = resultado_anterior - self.T()
            return self.E_prima(resultado)
        else:
            # ε (epsilon - producción vacía)
            self.traza_derivacion.append(f"    E' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def T(self):
        """T → P T'"""
        self.traza_derivacion.append(f"    T → P T' (posición {self.posicion})")
        resultado = self.P()
        return self.T_prima(resultado)
    
    def T_prima(self, resultado_anterior):
        """T' → * P T' | / P T' | % P T' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'MULT':
            self.traza_derivacion.append(f"      T' → * P T' (multiplicando {resultado_anterior} * ...)")
            self.consumir('MULT')
            resultado = resultado_anterior * self.P()
            return self.T_prima(resultado)
        elif token_actual[0] == 'DIV':
            self.traza_derivacion.append(f"      T' → / P T' (dividiendo {resultado_anterior} / ...)")
            self.consumir('DIV')
            divisor = self.P()
            if divisor == 0:
                raise Exception("División por cero detectada")
            resultado = resultado_anterior / divisor
            return self.T_prima(resultado)
        elif token_actual[0] == 'MOD':
            self.traza_derivacion.append(f"      T' → % P T' (módulo {resultado_anterior} % ...)")
            self.consumir('MOD')
            divisor = self.P()
            if divisor == 0:
                raise Exception("Módulo por cero no está definido")
            resultado = resultado_anterior % divisor
            return self.T_prima(resultado)
        else:
            # ε (epsilon - producción vacía)
            self.traza_derivacion.append(f"      T' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def P(self):
        """P → F P'"""
        self.traza_derivacion.append(f"      P → F P' (posición {self.posicion})")
        resultado = self.F()
        return self.P_prima(resultado)
    
    def P_prima(self, resultado_anterior):
        """P' → ** F P' | ^ F P' | ε"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'POT':
            self.traza_derivacion.append(f"        P' → ** F P' (potencia {resultado_anterior} ** ...)")
            self.consumir('POT')
            exponente = self.F()
            resultado = resultado_anterior ** exponente
            return self.P_prima(resultado)
        else:
            # ε (epsilon - producción vacía)
            self.traza_derivacion.append(f"        P' → ε (resultado parcial: {resultado_anterior})")
            return resultado_anterior
    
    def F(self):
        """F → ( E ) | numero | -numero"""
        token_actual = self.token_actual()
        
        if token_actual[0] == 'PAREN_IZQ':
            self.traza_derivacion.append(f"        F → ( E ) (subexpresión en paréntesis)")
            self.consumir('PAREN_IZQ')
            resultado = self.E()
            self.consumir('PAREN_DER')
            return resultado
        elif token_actual[0] == 'NUMERO':
            token = self.consumir('NUMERO')
            valor = float(token[1])
            self.traza_derivacion.append(f"        F → {valor} (número)")
            return valor
        elif token_actual[0] == 'RESTA':
            # Manejar números negativos
            self.traza_derivacion.append(f"        F → -número (número negativo)")
            self.consumir('RESTA')
            siguiente = self.token_actual()
            if siguiente[0] == 'NUMERO':
                token = self.consumir('NUMERO')
                return -float(token[1])
            elif siguiente[0] == 'PAREN_IZQ':
                # Permitir -(expresión)
                return -self.F()
            else:
                raise Exception("Se esperaba un número o expresión después del signo negativo")
        else:
            if token_actual[0] == 'EOF':
                raise Exception(f"Expresión incompleta: se esperaba un número o paréntesis")
            else:
                raise Exception(f"Token inesperado '{token_actual[1]}'. Se esperaba un número o paréntesis")


class InterfazCalculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Sintáctico Descendente - Calculadora Avanzada")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        self.calculadora = CalculadoraDescendente()
        self.historial = []  # Para guardar el historial de cálculos
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal con scrollbar
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Analizador Sintáctico Descendente Recursivo", 
                          font=("Arial", 16, "bold"), foreground="#2E86AB")
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Autores
        autores = ttk.Label(main_frame, 
                           text="Realizado por: Juan Esteban Cardozo Rivera • Juan Sebastián Gómez Usuga",
                           font=("Arial", 9, "italic"), foreground="#666")
        autores.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        
        # Descripción
        descripcion = ttk.Label(main_frame, 
                               text="Calculadora con análisis léxico y sintáctico • Soporta: +, -, *, /, %, ** (potencia)",
                               font=("Arial", 9), foreground="#555")
        descripcion.grid(row=2, column=0, columnspan=3, pady=(0, 15))
        
        # Frame de entrada
        entrada_frame = ttk.LabelFrame(main_frame, text="Entrada de Expresión", padding="10")
        entrada_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.entrada_expresion = ttk.Entry(entrada_frame, width=60, font=("Consolas", 12))
        self.entrada_expresion.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        self.entrada_expresion.bind('<Return>', lambda e: self.analizar_expresion())
        
        entrada_frame.columnconfigure(0, weight=1)
        
        # Botones principales
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=4, column=0, columnspan=3, pady=(0, 15))
        
        ttk.Button(botones_frame, text="🔍 Analizar", 
                  command=self.analizar_expresion, width=15).grid(row=0, column=0, padx=5)
        ttk.Button(botones_frame, text="🗑️ Limpiar", 
                  command=self.limpiar, width=15).grid(row=0, column=1, padx=5)
        ttk.Button(botones_frame, text="📝 Ejemplos", 
                  command=self.mostrar_ejemplos, width=15).grid(row=0, column=2, padx=5)
        ttk.Button(botones_frame, text="📊 Historial", 
                  command=self.mostrar_historial, width=15).grid(row=0, column=3, padx=5)
        ttk.Button(botones_frame, text="💾 Exportar", 
                  command=self.exportar_resultados, width=15).grid(row=0, column=4, padx=5)
        
        # Notebook para organizar resultados en pestañas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Pestaña 1: Resultado
        resultado_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(resultado_frame, text="📊 Resultado")
        
        self.resultado_texto = scrolledtext.ScrolledText(resultado_frame, width=70, height=8, 
                                                         font=("Consolas", 10), wrap=tk.WORD)
        self.resultado_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 2: Tokens
        tokens_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tokens_frame, text="🔤 Tokens")
        
        self.tokens_texto = scrolledtext.ScrolledText(tokens_frame, width=70, height=8, 
                                                      font=("Consolas", 9), wrap=tk.WORD)
        self.tokens_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 3: Árbol de derivación
        arbol_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(arbol_frame, text="🌳 Traza de Derivación")
        
        self.arbol_texto = scrolledtext.ScrolledText(arbol_frame, width=70, height=8, 
                                                     font=("Consolas", 9), wrap=tk.WORD)
        self.arbol_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 4: Gramática
        gramatica_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(gramatica_frame, text="📐 Gramática")
        
        self.mostrar_gramatica_info(gramatica_frame)
        
        # Configurar pesos para responsive
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
    
    def mostrar_gramatica_info(self, frame):
        """Muestra la información de la gramática utilizada"""
        gramatica_texto = scrolledtext.ScrolledText(frame, width=70, height=8, 
                                                    font=("Consolas", 9), wrap=tk.WORD)
        gramatica_texto.pack(fill=tk.BOTH, expand=True)
        
        info = """GRAMÁTICA LIBRE DE CONTEXTO (LL(1))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reglas de Producción:
─────────────────────
E  → T E'                    (Expresión)
E' → + T E' | - T E' | ε     (Expresión prima - suma/resta)
T  → P T'                    (Término)
T' → * P T' | / P T' | % P T' | ε    (Término prima - mult/div/mod)
P  → F P'                    (Potencia)
P' → ** F P' | ^ F P' | ε    (Potencia prima)
F  → ( E ) | número | -número  (Factor)

Precedencia de Operadores (Mayor a Menor):
──────────────────────────────────────────
1. Paréntesis: ( )
2. Potenciación: ** o ^
3. Multiplicación, División, Módulo: *, /, %
4. Suma, Resta: +, -

Tipo de Análisis:
─────────────────
• Análisis Sintáctico Descendente Recursivo
• Parser LL(1) (Left-to-right, Leftmost derivation, 1 lookahead)
• Sin recursividad por la izquierda

Tokens Reconocidos:
───────────────────
NUMERO, SUMA (+), RESTA (-), MULT (*), DIV (/), 
MOD (%), POT (** o ^), PAREN_IZQ ((), PAREN_DER ())
"""
        gramatica_texto.insert(tk.END, info)
        gramatica_texto.config(state=tk.DISABLED)
    
    def analizar_expresion(self):
        expresion = self.entrada_expresion.get().strip()
        
        if not expresion:
            messagebox.showwarning("Advertencia", "Por favor ingrese una expresión")
            return
        
        self.limpiar_resultados()
        
        try:
            # Mostrar tokens
            tokens = self.calculadora.tokenizar(expresion)
            if tokens:
                self.mostrar_tokens(tokens)
            
            # Realizar análisis sintáctico
            resultado, errores = self.calculadora.analizar(expresion)
            
            # Mostrar resultados
            if errores:
                self.mostrar_errores(errores)
            else:
                self.mostrar_resultado(resultado, expresion)
                self.mostrar_arbol_derivacion()
                
                # Agregar al historial
                self.agregar_al_historial(expresion, resultado)
                
        except Exception as e:
            self.resultado_texto.insert(tk.END, f"❌ Error inesperado: {str(e)}")
    
    def mostrar_tokens(self, tokens):
        self.tokens_texto.insert(tk.END, "ANÁLISIS LÉXICO - TOKENS IDENTIFICADOS\n")
        self.tokens_texto.insert(tk.END, "=" * 60 + "\n\n")
        
        # Tabla de tokens
        self.tokens_texto.insert(tk.END, f"{'#':<4} {'TIPO':<15} {'VALOR':<15} {'CATEGORÍA':<20}\n")
        self.tokens_texto.insert(tk.END, "-" * 60 + "\n")
        
        categorias = {
            'NUMERO': 'Operando',
            'SUMA': 'Operador Aritmético',
            'RESTA': 'Operador Aritmético',
            'MULT': 'Operador Aritmético',
            'DIV': 'Operador Aritmético',
            'MOD': 'Operador Aritmético',
            'POT': 'Operador Aritmético',
            'PAREN_IZQ': 'Delimitador',
            'PAREN_DER': 'Delimitador'
        }
        
        for i, (tipo, valor) in enumerate(tokens, 1):
            categoria = categorias.get(tipo, 'Desconocido')
            self.tokens_texto.insert(tk.END, f"{i:<4} {tipo:<15} {valor:<15} {categoria:<20}\n")
        
        self.tokens_texto.insert(tk.END, f"\n✓ Total de tokens: {len(tokens)}\n")
    
    def mostrar_resultado(self, resultado, expresion):
        self.resultado_texto.insert(tk.END, "╔═══════════════════════════════════════════════════════╗\n")
        self.resultado_texto.insert(tk.END, "║          ✓ ANÁLISIS COMPLETADO EXITOSAMENTE          ║\n")
        self.resultado_texto.insert(tk.END, "╚═══════════════════════════════════════════════════════╝\n\n")
        
        self.resultado_texto.insert(tk.END, f"Expresión Original:\n")
        self.resultado_texto.insert(tk.END, f"  {expresion}\n\n")
        
        self.resultado_texto.insert(tk.END, f"Resultado de la Evaluación:\n")
        self.resultado_texto.insert(tk.END, f"  {resultado}\n\n")
        
        self.resultado_texto.insert(tk.END, f"Estado del Análisis:\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Análisis léxico: CORRECTO\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Análisis sintáctico: CORRECTO\n")
        self.resultado_texto.insert(tk.END, f"  ✓ Evaluación semántica: CORRECTO\n\n")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.resultado_texto.insert(tk.END, f"Fecha y hora: {timestamp}\n")
    
    def mostrar_errores(self, errores):
        self.resultado_texto.insert(tk.END, "╔═══════════════════════════════════════════════════════╗\n")
        self.resultado_texto.insert(tk.END, "║            ❌ ERRORES DETECTADOS                      ║\n")
        self.resultado_texto.insert(tk.END, "╚═══════════════════════════════════════════════════════╝\n\n")
        
        for i, error in enumerate(errores, 1):
            self.resultado_texto.insert(tk.END, f"{i}. {error}\n\n")
        
        self.resultado_texto.insert(tk.END, "SUGERENCIAS:\n")
        self.resultado_texto.insert(tk.END, "• Revise la sintaxis de la expresión\n")
        self.resultado_texto.insert(tk.END, "• Verifique el balance de paréntesis\n")
        self.resultado_texto.insert(tk.END, "• Asegúrese de usar solo caracteres válidos\n")
        self.resultado_texto.insert(tk.END, "• Consulte la pestaña 'Gramática' para más información\n")
    
    def mostrar_arbol_derivacion(self):
        self.arbol_texto.insert(tk.END, "TRAZA DEL ANÁLISIS SINTÁCTICO DESCENDENTE\n")
        self.arbol_texto.insert(tk.END, "=" * 60 + "\n\n")
        
        if self.calculadora.traza_derivacion:
            for i, paso in enumerate(self.calculadora.traza_derivacion, 1):
                self.arbol_texto.insert(tk.END, f"{paso}\n")
        else:
            self.arbol_texto.insert(tk.END, "No hay información de derivación disponible.\n")
        
        self.arbol_texto.insert(tk.END, "\n" + "=" * 60 + "\n")
        self.arbol_texto.insert(tk.END, "LEYENDA:\n")
        self.arbol_texto.insert(tk.END, "• E: Expresión (suma/resta)\n")
        self.arbol_texto.insert(tk.END, "• T: Término (multiplicación/división/módulo)\n")
        self.arbol_texto.insert(tk.END, "• P: Potencia\n")
        self.arbol_texto.insert(tk.END, "• F: Factor (número o subexpresión)\n")
        self.arbol_texto.insert(tk.END, "• ε: Producción vacía (epsilon)\n")
    
    def agregar_al_historial(self, expresion, resultado):
        """Agrega una entrada al historial"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.historial.append({
            'tiempo': timestamp,
            'expresion': expresion,
            'resultado': resultado
        })
    
    def mostrar_historial(self):
        """Muestra el historial de cálculos"""
        historial_window = tk.Toplevel(self.root)
        historial_window.title("Historial de Cálculos")
        historial_window.geometry("600x400")
        
        ttk.Label(historial_window, text="Historial de Cálculos", 
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Crear texto con scroll
        historial_texto = scrolledtext.ScrolledText(historial_window, width=70, height=20, 
                                                    font=("Consolas", 10))
        historial_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        if not self.historial:
            historial_texto.insert(tk.END, "No hay cálculos en el historial.\n")
        else:
            historial_texto.insert(tk.END, f"{'HORA':<12} {'EXPRESIÓN':<30} {'RESULTADO':<15}\n")
            historial_texto.insert(tk.END, "=" * 60 + "\n")
            
            for entrada in self.historial:
                historial_texto.insert(tk.END, 
                    f"{entrada['tiempo']:<12} {entrada['expresion']:<30} {entrada['resultado']:<15}\n")
        
        historial_texto.config(state=tk.DISABLED)
        
        # Botones
        botones_frame = ttk.Frame(historial_window)
        botones_frame.pack(pady=10)
        
        ttk.Button(botones_frame, text="Limpiar Historial", 
                  command=lambda: self.limpiar_historial(historial_window)).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_frame, text="Cerrar", 
                  command=historial_window.destroy).pack(side=tk.LEFT, padx=5)
    
    def limpiar_historial(self, ventana):
        """Limpia el historial"""
        if messagebox.askyesno("Confirmar", "¿Desea limpiar todo el historial?"):
            self.historial.clear()
            ventana.destroy()
            messagebox.showinfo("Historial", "Historial limpiado exitosamente")
    
    def exportar_resultados(self):
        """Exporta los resultados actuales a un archivo"""
        contenido_resultado = self.resultado_texto.get(1.0, tk.END).strip()
        contenido_tokens = self.tokens_texto.get(1.0, tk.END).strip()
        contenido_arbol = self.arbol_texto.get(1.0, tk.END).strip()
        
        if not contenido_resultado:
            messagebox.showwarning("Exportar", "No hay resultados para exportar")
            return
        
        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")],
            title="Guardar análisis"
        )
        
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write("=" * 70 + "\n")
                    f.write("ANALIZADOR SINTÁCTICO DESCENDENTE - REPORTE DE ANÁLISIS\n")
                    f.write("=" * 70 + "\n")
                    f.write("Autores: Juan Esteban Cardozo Rivera\n")
                    f.write("         Juan Sebastián Gómez Usuga\n")
                    f.write("=" * 70 + "\n\n")
                    
                    f.write("RESULTADO DEL ANÁLISIS\n")
                    f.write("-" * 70 + "\n")
                    f.write(contenido_resultado + "\n\n")
                    
                    f.write("TOKENS IDENTIFICADOS\n")
                    f.write("-" * 70 + "\n")
                    f.write(contenido_tokens + "\n\n")
                    
                    f.write("TRAZA DE DERIVACIÓN\n")
                    f.write("-" * 70 + "\n")
                    f.write(contenido_arbol + "\n\n")
                    
                    f.write("=" * 70 + "\n")
                    f.write(f"Generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("=" * 70 + "\n")
                
                messagebox.showinfo("Exportar", f"Análisis exportado exitosamente a:\n{archivo}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar: {str(e)}")
    
    
    def limpiar(self):
        self.entrada_expresion.delete(0, tk.END)
        self.limpiar_resultados()
    
    def limpiar_resultados(self):
        self.resultado_texto.delete(1.0, tk.END)
        self.tokens_texto.delete(1.0, tk.END)
        self.arbol_texto.delete(1.0, tk.END)
    
    def mostrar_ejemplos(self):
        ejemplos = [
            ("Suma y resta", "2 + 3 - 1"),
            ("Precedencia", "2 + 3 * 4"),
            ("Paréntesis", "(5 - 2) * 3"),
            ("División", "10 / 2 + 8"),
            ("Decimales", "3.5 * 2 - 1"),
            ("Potencia", "2 ** 3 + 1"),
            ("Módulo", "10 % 3"),
            ("Compleja", "((2 + 3) * (4 - 1)) / 2"),
            ("Negativo", "-5 * 3 + 10"),
            ("Todo junto", "2 ** 3 + 10 % 3 * 2")
        ]
        
        ejemplo_window = tk.Toplevel(self.root)
        ejemplo_window.title("Ejemplos de Expresiones")
        ejemplo_window.geometry("400x450")
        
        ttk.Label(ejemplo_window, text="Seleccione un ejemplo:", 
                 font=("Arial", 12, "bold")).pack(pady=15)
        
        # Frame con scroll
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
                      command=hacer_lambda, width=45).pack()
        
        canvas.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=(0, 10))
        scrollbar.pack(side="right", fill="y", pady=(0, 10), padx=(0, 10))


def main():
    root = tk.Tk()
    app = InterfazCalculadora(root)
    root.mainloop()


if __name__ == "__main__":
    main()