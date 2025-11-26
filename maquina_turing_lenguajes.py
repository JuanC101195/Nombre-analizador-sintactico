"""
Máquina de Turing - Reconocimiento de Lenguajes
Autores: Juan Esteban Cardozo Rivera, Juan Sebastián Gómez Usuga

Descripción:
    Implementación de una Máquina de Turing para reconocer lenguajes formales.
    Ejemplos: a^n b^n c^n, palíndromos, patrones específicos
    
Características:
    - Reconocimiento de lenguaje L = {a^n b^n c^n} (n ≥ 1) - Tipo 1
    - Verificación de palíndromos sobre {a,b}
    - Reconocimiento de patrones a^n b^2n (proporción 1:2)
    - Interfaz gráfica con visualización paso a paso
    - Tabla de transiciones completa
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime


class MaquinaTuringLenguajes:
    """Máquina de Turing para reconocer lenguajes formales"""
    
    def __init__(self):
        self.cinta = []
        self.posicion_cabezal = 0
        self.estado_actual = 'q0'
        self.estado_aceptacion = 'qaccept'
        self.estado_rechazo = 'qreject'
        self.simbolo_blanco = '∅'
        self.historial = []
        self.max_pasos = 1000
        
    def inicializar_cinta(self, cadena):
        """Inicializa la cinta con la cadena de entrada"""
        if not cadena:
            self.cinta = [self.simbolo_blanco]
        else:
            self.cinta = list(cadena) + [self.simbolo_blanco]
        self.posicion_cabezal = 0
        self.estado_actual = 'q0'
        self.historial = []
        
    def leer_simbolo(self):
        """Lee el símbolo en la posición actual"""
        if self.posicion_cabezal < 0 or self.posicion_cabezal >= len(self.cinta):
            return self.simbolo_blanco
        return self.cinta[self.posicion_cabezal]
    
    def escribir_simbolo(self, simbolo):
        """Escribe un símbolo en la posición actual"""
        while self.posicion_cabezal >= len(self.cinta):
            self.cinta.append(self.simbolo_blanco)
        
        if self.posicion_cabezal >= 0:
            self.cinta[self.posicion_cabezal] = simbolo
    
    def mover_cabezal(self, direccion):
        """Mueve el cabezal: 'R' (derecha), 'L' (izquierda), '-' (stay)"""
        if direccion == 'R':
            self.posicion_cabezal += 1
        elif direccion == 'L':
            self.posicion_cabezal -= 1
    
    def registrar_paso(self, accion=""):
        """Registra el estado actual en el historial"""
        cinta_visual = ''.join(self.cinta).replace(self.simbolo_blanco, '_')
        self.historial.append({
            'paso': len(self.historial),
            'estado': self.estado_actual,
            'cinta': cinta_visual,
            'posicion': self.posicion_cabezal,
            'simbolo': self.leer_simbolo(),
            'accion': accion
        })
    
    def reconocer_anbn(self, cadena):
        """
        Reconoce el lenguaje L = {a^n b^n c^n | n ≥ 0}
        Ejemplos válidos: ε, abc, aabbcc, aaabbbccc
        Estrategia: Marcar 'a', 'b' y 'c' en tríos hasta que no quede nada
        NOTA: Este es un lenguaje tipo-1 (sensible al contexto), NO tipo-2
        """
        self.inicializar_cinta(cadena)
        self.registrar_paso("Inicio - Verificando a^n b^n c^n")
        
        # Tabla de transiciones para a^n b^n c^n
        transiciones = {
            # Estado q0: Busca 'a' para marcar
            ('q0', 'a'): ('q1', 'X', 'R', "Marca 'a' como X, busca 'b' pareja"),
            ('q0', 'X'): ('q0', 'X', 'R', "Salta 'a's ya marcadas"),
            ('q0', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Cadena vacía ε - ACEPTADA"),
            
            # Estado q1: Busca 'b' para emparejar con la 'a'
            ('q1', 'a'): ('q1', 'a', 'R', "Salta 'a's no marcadas"),
            ('q1', 'b'): ('q2', 'Y', 'R', "Marca 'b' como Y, busca 'c'"),
            ('q1', 'Y'): ('q1', 'Y', 'R', "Salta 'b's ya marcadas"),
            
            # Estado q2: Busca 'c' para completar el trío
            ('q2', 'b'): ('q2', 'b', 'R', "Salta 'b's no marcadas"),
            ('q2', 'Y'): ('q2', 'Y', 'R', "Salta 'b's ya marcadas"),
            ('q2', 'Z'): ('q2', 'Z', 'R', "Salta 'c's ya marcadas"),
            ('q2', 'c'): ('q3', 'Z', 'L', "Marca 'c' como Z, regresa al inicio"),
            
            # Estado q3: Regresa al inicio
            ('q3', 'Z'): ('q3', 'Z', 'L', "Retrocede sobre 'Z's"),
            ('q3', 'Y'): ('q3', 'Y', 'L', "Retrocede sobre 'Y's"),
            ('q3', 'b'): ('q3', 'b', 'L', "Retrocede sobre 'b's"),
            ('q3', 'a'): ('q3', 'a', 'L', "Retrocede sobre 'a's"),
            ('q3', 'X'): ('q3', 'X', 'L', "Retrocede sobre 'X's"),
            ('q3', self.simbolo_blanco): ('q4', self.simbolo_blanco, 'R', "Llegó al inicio"),
            
            # Estado q4: Verificar si quedan 'a's sin marcar
            ('q4', 'X'): ('q4', 'X', 'R', "Salta 'X's"),
            ('q4', 'a'): ('q0', 'a', '-', "Hay más 'a's, repetir proceso"),
            ('q4', 'Y'): ('q5', 'Y', 'R', "Ya no hay 'a's, verificar final"),
            
            # Estado q5: Verificación final - solo deben quedar Y's y Z's
            ('q5', 'Y'): ('q5', 'Y', 'R', "Verifica 'Y's"),
            ('q5', 'Z'): ('q5', 'Z', 'R', "Verifica 'Z's"),
            ('q5', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Todo procesado - ACEPTADA"),
        }
        
        pasos = 0
        while (self.estado_actual not in [self.estado_aceptacion, self.estado_rechazo] 
               and pasos < self.max_pasos):
            
            simbolo_actual = self.leer_simbolo()
            clave = (self.estado_actual, simbolo_actual)
            
            if clave in transiciones:
                nuevo_estado, escribir, mover, descripcion = transiciones[clave]
                accion = f"δ({self.estado_actual}, {simbolo_actual}) → ({nuevo_estado}, {escribir}, {mover}): {descripcion}"
                
                self.estado_actual = nuevo_estado
                self.escribir_simbolo(escribir)
                self.mover_cabezal(mover)
                
                self.registrar_paso(accion)
                pasos += 1
            else:
                # No hay transición - rechazar
                self.estado_actual = self.estado_rechazo
                self.registrar_paso(f"No existe transición para ({self.estado_actual}, {simbolo_actual}) - RECHAZADA")
                break
        
        if pasos >= self.max_pasos:
            self.estado_actual = self.estado_rechazo
            self.registrar_paso("Excedido límite de pasos - RECHAZADA")
        
        aceptada = self.estado_actual == self.estado_aceptacion
        return aceptada, self.historial
    
    def reconocer_palindromo(self, cadena):
        """
        Reconoce palíndromos sobre {a, b}
        Ejemplos: aba, abba, aabbaa
        Estrategia: Comparar extremos y marcarlos hasta el centro
        """
        self.inicializar_cinta(cadena)
        self.registrar_paso("Inicio - Verificando palíndromo")
        
        # Tabla de transiciones para palíndromos
        transiciones = {
            # Estado q0: Leer símbolo izquierdo
            ('q0', 'a'): ('q1', 'X', 'R', "Marca 'a' izquierda, busca 'a' derecha"),
            ('q0', 'b'): ('q2', 'X', 'R', "Marca 'b' izquierda, busca 'b' derecha"),
            ('q0', 'X'): ('q5', 'X', 'R', "Ya procesado, verificar centro"),
            ('q0', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Cadena vacía - ACEPTADA"),
            
            # Estado q1: Buscar 'a' en el extremo derecho
            ('q1', 'a'): ('q1', 'a', 'R', "Avanza buscando extremo derecho"),
            ('q1', 'b'): ('q1', 'b', 'R', "Avanza buscando extremo derecho"),
            ('q1', 'X'): ('q1', 'X', 'R', "Salta marcas anteriores"),
            ('q1', self.simbolo_blanco): ('q3', self.simbolo_blanco, 'L', "Llegó al final, retrocede"),
            
            # Estado q2: Buscar 'b' en el extremo derecho
            ('q2', 'a'): ('q2', 'a', 'R', "Avanza buscando extremo derecho"),
            ('q2', 'b'): ('q2', 'b', 'R', "Avanza buscando extremo derecho"),
            ('q2', 'X'): ('q2', 'X', 'R', "Salta marcas anteriores"),
            ('q2', self.simbolo_blanco): ('q4', self.simbolo_blanco, 'L', "Llegó al final, retrocede"),
            
            # Estado q3: Verificar 'a' en extremo derecho
            ('q3', 'X'): ('q3', 'X', 'L', "Retrocede sobre marcas"),
            ('q3', 'a'): ('q6', 'X', 'L', "Encontró 'a' pareja, marca y regresa"),
            ('q3', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Centro con 'a' - ACEPTADA"),
            
            # Estado q4: Verificar 'b' en extremo derecho
            ('q4', 'X'): ('q4', 'X', 'L', "Retrocede sobre marcas"),
            ('q4', 'b'): ('q6', 'X', 'L', "Encontró 'b' pareja, marca y regresa"),
            ('q4', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Centro con 'b' - ACEPTADA"),
            
            # Estado q5: Verificación final
            ('q5', 'X'): ('q5', 'X', 'R', "Verifica que todo esté marcado"),
            ('q5', 'a'): (self.estado_aceptacion, 'a', '-', "Centro con 'a' - ACEPTADA"),
            ('q5', 'b'): (self.estado_aceptacion, 'b', '-', "Centro con 'b' - ACEPTADA"),
            ('q5', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Palíndromo válido - ACEPTADA"),
            
            # Estado q6: Regresar al inicio
            ('q6', 'a'): ('q6', 'a', 'L', "Retrocede al inicio"),
            ('q6', 'b'): ('q6', 'b', 'L', "Retrocede al inicio"),
            ('q6', 'X'): ('q0', 'X', 'R', "Llegó al inicio, siguiente par"),
            ('q6', self.simbolo_blanco): ('q0', self.simbolo_blanco, 'R', "Llegó al inicio, continuar"),
        }
        
        pasos = 0
        while (self.estado_actual not in [self.estado_aceptacion, self.estado_rechazo] 
               and pasos < self.max_pasos):
            
            simbolo_actual = self.leer_simbolo()
            clave = (self.estado_actual, simbolo_actual)
            
            if clave in transiciones:
                nuevo_estado, escribir, mover, descripcion = transiciones[clave]
                accion = f"δ({self.estado_actual}, {simbolo_actual}) → ({nuevo_estado}, {escribir}, {mover}): {descripcion}"
                
                self.estado_actual = nuevo_estado
                self.escribir_simbolo(escribir)
                self.mover_cabezal(mover)
                
                self.registrar_paso(accion)
                pasos += 1
            else:
                self.estado_actual = self.estado_rechazo
                self.registrar_paso(f"No es palíndromo - RECHAZADA")
                break
        
        if pasos >= self.max_pasos:
            self.estado_actual = self.estado_rechazo
            self.registrar_paso("Excedido límite de pasos - RECHAZADA")
        
        aceptada = self.estado_actual == self.estado_aceptacion
        return aceptada, self.historial
    
    def reconocer_anb2n(self, cadena):
        """
        Reconoce el lenguaje L = {a^n b^2n | n ≥ 1}
        Ejemplos: abb, aabbbb, aaabbbbbb
        Por cada 'a' debe haber exactamente 2 'b's
        """
        self.inicializar_cinta(cadena)
        self.registrar_paso("Inicio - Verificando a^n b^2n")
        
        # Tabla de transiciones para a^n b^2n
        transiciones = {
            # Estado q0: Marca 'a'
            ('q0', 'a'): ('q1', 'X', 'R', "Marca 'a', busca 2 'b's"),
            ('q0', 'Y'): ('q5', 'Y', 'R', "No hay más 'a's, verificar"),
            ('q0', 'X'): ('q0', 'X', 'R', "Salta 'X's marcadas"),
            
            # Estado q1: Busca primera 'b'
            ('q1', 'a'): ('q1', 'a', 'R', "Salta 'a's"),
            ('q1', 'Y'): ('q1', 'Y', 'R', "Salta 'b's marcadas"),
            ('q1', 'b'): ('q2', 'Y', 'R', "Marca primera 'b'"),
            
            # Estado q2: Busca segunda 'b'
            ('q2', 'Y'): ('q2', 'Y', 'R', "Salta 'b's marcadas"),
            ('q2', 'b'): ('q3', 'Y', 'L', "Marca segunda 'b', regresa"),
            
            # Estado q3: Regresa al inicio
            ('q3', 'Y'): ('q3', 'Y', 'L', "Retrocede"),
            ('q3', 'a'): ('q3', 'a', 'L', "Retrocede"),
            ('q3', 'X'): ('q3', 'X', 'L', "Retrocede sobre 'X's"),
            ('q3', self.simbolo_blanco): ('q0', self.simbolo_blanco, 'R', "Inicio, busca siguiente 'a'"),
            
            # Estado q5: Verificación final
            ('q5', 'Y'): ('q5', 'Y', 'R', "Verifica solo 'Y's"),
            ('q5', self.simbolo_blanco): (self.estado_aceptacion, self.simbolo_blanco, '-', "Patrón a^n b^2n válido - ACEPTADA"),
        }
        
        pasos = 0
        while (self.estado_actual not in [self.estado_aceptacion, self.estado_rechazo] 
               and pasos < self.max_pasos):
            
            simbolo_actual = self.leer_simbolo()
            clave = (self.estado_actual, simbolo_actual)
            
            if clave in transiciones:
                nuevo_estado, escribir, mover, descripcion = transiciones[clave]
                accion = f"δ({self.estado_actual}, {simbolo_actual}) → ({nuevo_estado}, {escribir}, {mover}): {descripcion}"
                
                self.estado_actual = nuevo_estado
                self.escribir_simbolo(escribir)
                self.mover_cabezal(mover)
                
                self.registrar_paso(accion)
                pasos += 1
            else:
                self.estado_actual = self.estado_rechazo
                self.registrar_paso(f"No cumple patrón a^n b^2n - RECHAZADA")
                break
        
        if pasos >= self.max_pasos:
            self.estado_actual = self.estado_rechazo
            self.registrar_paso("Excedido límite de pasos - RECHAZADA")
        
        aceptada = self.estado_actual == self.estado_aceptacion
        return aceptada, self.historial


class InterfazMTLenguajes:
    """Interfaz gráfica moderna para Máquina de Turing de lenguajes"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔤 Máquina de Turing - Reconocimiento de Lenguajes")
        self.root.geometry("1280x850")
        
        # Paleta de colores moderna
        self.bg_main = "#F8FAFC"
        self.bg_card = "#FFFFFF"
        self.primary = "#8B5CF6"  # Violeta
        self.secondary = "#10B981"  # Verde
        self.accent = "#F59E0B"  # Naranja
        self.danger = "#EF4444"  # Rojo
        self.text_dark = "#1E293B"
        self.text_light = "#64748B"
        
        self.root.configure(bg=self.bg_main)
        
        # Configurar estilos modernos
        self.configurar_estilos()
        
        self.maquina = MaquinaTuringLenguajes()
        
        self.crear_interfaz()
    
    def configurar_estilos(self):
        """Configurar estilos personalizados modernos"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Botón primario
        style.configure('Primary.TButton',
                       background=self.primary,
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 10, 'bold'),
                       padding=(15, 10))
        
        style.map('Primary.TButton',
                 background=[('active', '#7C3AED'), ('pressed', '#6D28D9')])
        
        # Botón secundario
        style.configure('Secondary.TButton',
                       background=self.secondary,
                       foreground='white',
                       borderwidth=0,
                       font=('Segoe UI', 10, 'bold'),
                       padding=(15, 10))
        
        # Botón de acento
        style.configure('Accent.TButton',
                       background=self.accent,
                       foreground='white',
                       borderwidth=0,
                       font=('Segoe UI', 10, 'bold'),
                       padding=(15, 10))
        
        # Combobox
        style.configure('Modern.TCombobox',
                       fieldbackground='white',
                       background=self.primary,
                       font=('Segoe UI', 10))
        
        # Frames
        style.configure('Card.TFrame',
                       background=self.bg_card)
        
        style.configure('Main.TFrame',
                       background=self.bg_main)
    
    def crear_interfaz(self):
        # Frame principal con padding
        main_container = tk.Frame(self.root, bg=self.bg_main)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        #  Header moderno con gradiente
        header_frame = tk.Frame(main_container, bg=self.primary, height=120)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        titulo = tk.Label(header_frame,
                         text="🔤 MÁQUINA DE TURING",
                         font=("Segoe UI", 26, "bold"),
                         bg=self.primary, fg="white")
        titulo.pack(pady=(15, 5))
        
        subtitulo = tk.Label(header_frame,
                            text="Reconocimiento de Lenguajes Formales",
                            font=("Segoe UI", 13),
                            bg=self.primary, fg="#E9D5FF")
        subtitulo.pack()
        
        autores = tk.Label(header_frame,
                          text="👨‍💻 Juan Esteban Cardozo Rivera • Juan Sebastián Gómez Usuga",
                          font=("Segoe UI", 9, "italic"),
                          bg=self.primary, fg="#DDD6FE")
        autores.pack(pady=(5, 10))
        
        # Contenido principal
        content_frame = tk.Frame(main_container, bg=self.bg_main, padx=25, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Card de configuración
        config_card = tk.Frame(content_frame, bg=self.bg_card, relief='flat', bd=0)
        config_card.pack(fill=tk.X, pady=(0, 20))
        
        # Agregar sombra simulada
        shadow_frame = tk.Frame(config_card, bg='#E2E8F0', height=2)
        shadow_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        config_inner = tk.Frame(config_card, bg=self.bg_card, padx=25, pady=20)
        config_inner.pack(fill=tk.X)
        
        tk.Label(config_inner,
                text="⚙️ Configuración",
                font=("Segoe UI", 14, "bold"),
                bg=self.bg_card, fg=self.text_dark).pack(anchor=tk.W, pady=(0, 15))
        
        input_frame = tk.Frame(config_inner, bg=self.bg_card)
        input_frame.pack(fill=tk.X)
        
        # Selección de lenguaje
        lang_frame = tk.Frame(input_frame, bg=self.bg_card)
        lang_frame.pack(side=tk.LEFT, padx=(0, 30))
        
        tk.Label(lang_frame, text="Tipo de Lenguaje:",
                font=("Segoe UI", 10, "bold"),
                bg=self.bg_card, fg=self.text_dark).pack(anchor=tk.W, pady=(0, 5))
        
        self.tipo_lenguaje = ttk.Combobox(lang_frame,
                                          values=["a^n b^n c^n", "Palíndromo", "a^n b^2n"],
                                          state="readonly",
                                          width=18,
                                          style='Modern.TCombobox',
                                          font=("Segoe UI", 11))
        self.tipo_lenguaje.set("a^n b^n c^n")
        self.tipo_lenguaje.pack()
        
        # Entrada de cadena
        string_frame = tk.Frame(input_frame, bg=self.bg_card)
        string_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(string_frame, text="Cadena de Entrada:",
                font=("Segoe UI", 10, "bold"),
                bg=self.bg_card, fg=self.text_dark).pack(anchor=tk.W, pady=(0, 5))
        
        self.entrada_cadena = ttk.Entry(string_frame,
                                        width=35,
                                        font=("Consolas", 12))
        self.entrada_cadena.insert(0, "aabbcc")
        self.entrada_cadena.pack(fill=tk.X)
        self.entrada_cadena.bind('<Return>', lambda e: self.verificar_cadena())
        
        # Botones de acción con estilo moderno
        buttons_frame = tk.Frame(content_frame, bg=self.bg_main)
        buttons_frame.pack(pady=(0, 20))
        
        ttk.Button(buttons_frame, text="▶️  Verificar Cadena",
                  command=self.verificar_cadena,
                  style='Primary.TButton',
                  width=20).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(buttons_frame, text="🔄  Limpiar",
                  command=self.limpiar,
                  width=18).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(buttons_frame, text="📚  Ver Ejemplos",
                  command=self.mostrar_ejemplos,
                  style='Accent.TButton',
                  width=18).pack(side=tk.LEFT, padx=8)
        
        # Notebook con tabs mejorados
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Crear pestañas
        self.crear_pestanas()
    
    def crear_pestanas(self):
        # Pestaña 1: Resultado con indicador visual
        resultado_frame = tk.Frame(self.notebook, bg=self.bg_card, padx=20, pady=20)
        self.notebook.add(resultado_frame, text="  ✅ Resultado  ")
        
        self.resultado_texto = scrolledtext.ScrolledText(resultado_frame,
                                                         width=110, height=20,
                                                         font=("Consolas", 10),
                                                         wrap=tk.WORD,
                                                         bg="#FAFAFA",
                                                         fg=self.text_dark,
                                                         relief='flat',
                                                         borderwidth=5,
                                                         padx=10, pady=10)
        self.resultado_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 2: Traza con formato
        traza_frame = tk.Frame(self.notebook, bg=self.bg_card, padx=20, pady=20)
        self.notebook.add(traza_frame, text="  🔄 Traza  ")
        
        self.traza_texto = scrolledtext.ScrolledText(traza_frame,
                                                     width=110, height=20,
                                                     font=("Consolas", 9),
                                                     wrap=tk.NONE,
                                                     bg="#FAFAFA",
                                                     fg=self.text_dark,
                                                     relief='flat',
                                                     borderwidth=5,
                                                     padx=10, pady=10)
        self.traza_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 3: Tabla de transiciones
        tabla_frame = tk.Frame(self.notebook, bg=self.bg_card, padx=20, pady=20)
        self.notebook.add(tabla_frame, text="  📋 Transiciones  ")
        
        self.tabla_texto = scrolledtext.ScrolledText(tabla_frame,
                                                     width=110, height=20,
                                                     font=("Consolas", 9),
                                                     wrap=tk.WORD,
                                                     bg="#FAFAFA",
                                                     fg=self.text_dark,
                                                     relief='flat',
                                                     borderwidth=5,
                                                     padx=10, pady=10)
        self.tabla_texto.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña 4: Teoría con diseño mejorado
        teoria_frame = tk.Frame(self.notebook, bg=self.bg_card, padx=20, pady=20)
        self.notebook.add(teoria_frame, text="  📚 Teoría  ")
        
        self.mostrar_teoria(teoria_frame)
    
    def verificar_cadena(self):
        """Verifica si la cadena pertenece al lenguaje"""
        cadena = self.entrada_cadena.get().strip()
        tipo = self.tipo_lenguaje.get()
        
        self.limpiar_resultados()
        
        # Ejecutar verificación según el tipo
        if tipo == "a^n b^n c^n":
            aceptada, historial = self.maquina.reconocer_anbn(cadena)
            lenguaje_desc = "L = {a^n b^n c^n | n ≥ 1}"
        elif tipo == "Palíndromo":
            aceptada, historial = self.maquina.reconocer_palindromo(cadena)
            lenguaje_desc = "L = {w | w = w^R, w ∈ {a,b}*}"
        else:  # a^n b^2n
            aceptada, historial = self.maquina.reconocer_anb2n(cadena)
            lenguaje_desc = "L = {a^n b^2n | n ≥ 1}"
        
        self.mostrar_resultado(cadena, tipo, aceptada, historial, lenguaje_desc)
        self.mostrar_traza(historial)
        self.mostrar_tabla_transiciones(tipo)
    
    def mostrar_resultado(self, cadena, tipo, aceptada, historial, lenguaje_desc):
        """Muestra el resultado de la verificación con colores"""
        # Configurar tags de colores
        self.resultado_texto.tag_config("header", foreground="#8B5CF6", font=("Consolas", 12, "bold"))
        self.resultado_texto.tag_config("success", foreground="#10B981", font=("Consolas", 11, "bold"))
        self.resultado_texto.tag_config("error", foreground="#EF4444", font=("Consolas", 11, "bold"))
        self.resultado_texto.tag_config("info", foreground="#3B82F6", font=("Consolas", 10))
        self.resultado_texto.tag_config("data", foreground="#64748B", font=("Consolas", 10))
        
        # Encabezado con diseño
        self.resultado_texto.insert(tk.END, "\n╔" + "═" * 88 + "╗\n")
        
        if aceptada:
            self.resultado_texto.insert(tk.END, "║    ✅ CADENA ACEPTADA    ║\n", "success")
            status_icon = "✓"
            status_color = "success"
        else:
            self.resultado_texto.insert(tk.END, "║    ❌ CADENA RECHAZADA    ║\n", "error")
            status_icon = "✗"
            status_color = "error"
        
        self.resultado_texto.insert(tk.END, "╚" + "═" * 88 + "╝\n\n")
        
        # Información del lenguaje
        self.resultado_texto.insert(tk.END, "📋 INFORMACIÓN DEL LENGUAJE\n", "header")
        self.resultado_texto.insert(tk.END, "─" * 90 + "\n")
        self.resultado_texto.insert(tk.END, f"  Tipo:       ", "info")
        self.resultado_texto.insert(tk.END, f"{tipo}\n", "data")
        self.resultado_texto.insert(tk.END, f"  Definición: ", "info")
        self.resultado_texto.insert(tk.END, f"{lenguaje_desc}\n\n", "data")
        
        # Cadena procesada
        self.resultado_texto.insert(tk.END, "🔤 CADENA PROCESADA\n", "header")
        self.resultado_texto.insert(tk.END, "─" * 90 + "\n")
        self.resultado_texto.insert(tk.END, f"  Entrada:  ", "info")
        if cadena:
            self.resultado_texto.insert(tk.END, f"'{cadena}'\n", "data")
        else:
            self.resultado_texto.insert(tk.END, "ε (cadena vacía)\n", "data")
        self.resultado_texto.insert(tk.END, f"  Longitud: ", "info")
        self.resultado_texto.insert(tk.END, f"{len(cadena)} símbolos\n\n", "data")
        
        # Estadísticas de ejecución
        self.resultado_texto.insert(tk.END, "📊 ESTADÍSTICAS\n", "header")
        self.resultado_texto.insert(tk.END, "─" * 90 + "\n")
        self.resultado_texto.insert(tk.END, f"  Pasos ejecutados: ", "info")
        self.resultado_texto.insert(tk.END, f"{len(historial)}\n", "data")
        self.resultado_texto.insert(tk.END, f"  Estado final:     ", "info")
        self.resultado_texto.insert(tk.END, f"{self.maquina.estado_actual}\n\n", "data")
        
        # Veredicto final
        self.resultado_texto.insert(tk.END, "🏁 VEREDICTO\n", "header")
        self.resultado_texto.insert(tk.END, "─" * 90 + "\n")
        
        if aceptada:
            self.resultado_texto.insert(tk.END, f"  {status_icon} La cadena SÍ pertenece al lenguaje {tipo}\n", status_color)
            self.resultado_texto.insert(tk.END, f"  {status_icon} Verificación EXITOSA - Máquina en estado de aceptación\n\n", status_color)
        else:
            self.resultado_texto.insert(tk.END, f"  {status_icon} La cadena NO pertenece al lenguaje {tipo}\n", status_color)
            self.resultado_texto.insert(tk.END, f"  {status_icon} Verificación FALLIDA - Máquina en estado de rechazo\n\n", status_color)
        
        # Timestamp
        self.resultado_texto.insert(tk.END, "─" * 90 + "\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.resultado_texto.insert(tk.END, f"⏰ Procesado: {timestamp}\n", "data")
    
    def mostrar_traza(self, historial):
        """Muestra la traza de ejecución"""
        self.traza_texto.insert(tk.END, "TRAZA DE EJECUCIÓN - MÁQUINA DE TURING\n")
        self.traza_texto.insert(tk.END, "=" * 110 + "\n\n")
        
        self.traza_texto.insert(tk.END, f"{'Paso':<6} {'Estado':<10} {'Cinta':<35} {'Pos':<5} {'Lee':<6} {'Acción':<50}\n")
        self.traza_texto.insert(tk.END, "─" * 110 + "\n")
        
        for paso in historial:
            paso_num = str(paso['paso'])
            estado = paso['estado']
            cinta = paso['cinta'][:30] + "..." if len(paso['cinta']) > 30 else paso['cinta']
            pos = str(paso['posicion'])
            simbolo = paso['simbolo']
            accion = paso['accion'][:45] + "..." if len(paso['accion']) > 45 else paso['accion']
            
            self.traza_texto.insert(tk.END, f"{paso_num:<6} {estado:<10} {cinta:<35} {pos:<5} {simbolo:<6} {accion:<50}\n")
        
        self.traza_texto.insert(tk.END, "\n" + "=" * 110 + "\n")
    
    def mostrar_tabla_transiciones(self, tipo):
        """Muestra la tabla de transiciones del lenguaje seleccionado"""
        self.tabla_texto.insert(tk.END, f"TABLA DE TRANSICIONES - {tipo}\n")
        self.tabla_texto.insert(tk.END, "=" * 90 + "\n\n")
        
        if tipo == "a^n b^n c^n":
            tabla = """Estado    Lee       Escribe   Mueve   Nuevo     Descripción
──────────────────────────────────────────────────────────────────────────
q0        a         X         R       q1        Marca 'a', busca 'b' pareja
q0        X         X         R       q0        Salta 'a's ya marcadas
q0        ∅         ∅         -       qaccept   Cadena vacía ε aceptada

q1        a         a         R       q1        Salta 'a's no marcadas
q1        Y         Y         R       q1        Salta 'b's ya marcadas
q1        b         Y         R       q2        Marca 'b' como Y, busca 'c'

q2        b         b         R       q2        Salta 'b's no marcadas
q2        Y/Z       Y/Z       R       q2        Salta 'b's y 'c's marcadas
q2        c         Z         L       q3        Marca 'c' como Z, regresa

q3        a/b/      a/b/      L       q3        Retrocede sobre todo
          X/Y/Z     X/Y/Z
q3        ∅         ∅         R       q4        Llegó al inicio

q4        X         X         R       q4        Salta 'X's
q4        a         a         -       q0        Hay más 'a's, repetir
q4        Y         Y         R       q5        Ya no hay 'a's, verificar

q5        Y/Z       Y/Z       R       q5        Verifica solo marcas
q5        ∅         ∅         -       qaccept   Todo procesado - ACEPTADA

Cualquier otra combinación → qreject (RECHAZADA)
"""
        elif tipo == "Palíndromo":
            tabla = """Estado    Lee       Escribe   Mueve   Nuevo     Descripción
──────────────────────────────────────────────────────────────────────────
q0        a         X         R       q1        Marca 'a' izq, busca 'a' der
q0        b         X         R       q2        Marca 'b' izq, busca 'b' der
q0        X         X         R       q5        Ya procesado, verificar centro
q0        ∅         ∅         -       qaccept   Cadena vacía aceptada

q1        a/b/X     a/b/X     R       q1        Avanza al extremo derecho
q1        ∅         ∅         L       q3        Llegó al final, retrocede

q2        a/b/X     a/b/X     R       q2        Avanza al extremo derecho
q2        ∅         ∅         L       q4        Llegó al final, retrocede

q3        X         X         L       q3        Retrocede sobre marcas
q3        a         X         L       q6        Encontró 'a' pareja

q4        X         X         L       q4        Retrocede sobre marcas
q4        b         X         L       q6        Encontró 'b' pareja

q5        X         X         R       q5        Verifica todo marcado
q5        ∅         ∅         -       qaccept   Palíndromo válido

q6        a/b       a/b       L       q6        Retrocede al inicio
q6        X         X         R       q0        Llegó al inicio

Cualquier otra combinación → qreject
"""
        else:  # a^n b^2n
            tabla = """Estado    Lee       Escribe   Mueve   Nuevo     Descripción
──────────────────────────────────────────────────────────────────────────
q0        a         X         R       q1        Marca 'a', busca 2 'b's
q0        Y         Y         R       q5        No hay más 'a's, verificar

q1        a         a         R       q1        Salta 'a's no marcadas
q1        Y         Y         R       q1        Salta 'b's ya marcadas
q1        b         Y         R       q2        Marca primera 'b'

q2        Y         Y         R       q2        Salta 'b's marcadas
q2        b         Y         L       q3        Marca segunda 'b', regresa

q3        Y/a       Y/a       L       q3        Retrocede
q3        X         X         L       q4        Pasó primera marca

q4        X/a       X/a       L       q4        Sigue retrocediendo
q4        ∅         ∅         R       q0        Al inicio, busca siguiente 'a'

q5        Y         Y         R       q5        Verifica solo 'Y's
q5        ∅         ∅         -       qaccept   Patrón a^n b^2n válido

Cualquier otra combinación → qreject
"""
        
        self.tabla_texto.insert(tk.END, tabla)
        self.tabla_texto.insert(tk.END, "\nNotación:\n")
        self.tabla_texto.insert(tk.END, "  X, Y = Símbolos de marcado\n")
        self.tabla_texto.insert(tk.END, "  ∅ = Símbolo blanco (fin de cinta)\n")
        self.tabla_texto.insert(tk.END, "  R = Derecha, L = Izquierda, - = No se mueve\n")
    
    def mostrar_teoria(self, frame):
        """Muestra teoría sobre lenguajes formales"""
        teoria_texto = scrolledtext.ScrolledText(frame, width=95, height=16,
                                                 font=("Consolas", 9), wrap=tk.WORD)
        teoria_texto.pack(fill=tk.BOTH, expand=True)
        
        info = """MÁQUINAS DE TURING - RECONOCIMIENTO DE LENGUAJES FORMALES
════════════════════════════════════════════════════════════════════════

LENGUAJES IMPLEMENTADOS:
────────────────────────

1. L = {a^n b^n c^n | n ≥ 1}
   ──────────────────────────
   • Cadenas con IGUAL número de 'a's, 'b's y 'c's
   • Deben aparecer en orden: a's, luego b's, luego c's
   • Ejemplos válidos: abc, aabbcc, aaabbbccc, aaaabbbbcccc
   • Ejemplos inválidos: ab, aabbc, abcabc, cba
   
   ⚠️ IMPORTANTE: Este es un lenguaje TIPO 1 (sensible al contexto)
   NO puede ser generado por una gramática libre de contexto (Tipo 2)
   
   Gramática Sensible al Contexto:
   S → aSBC | aBC
   CB → BC
   aB → ab
   bB → bb
   bC → bc
   cC → cc
   
   Estrategia de la MT:
   • Marcar tríos de 'a', 'b' y 'c' (X, Y y Z)
   • Por cada 'a' marcada, marcar una 'b' y luego una 'c'
   • Regresar al inicio y repetir
   • Si al final solo quedan marcas → ACEPTAR
   • Si sobran o faltan símbolos → RECHAZAR

2. L = {w | w = w^R, w ∈ {a,b}*}
   ──────────────────────────────
   • Palíndromos sobre el alfabeto {a, b}
   • La cadena es igual a su reverso
   • Ejemplos válidos: ε, a, b, aa, aba, abba, aabbaa
   • Ejemplos inválidos: ab, aab, abab
   
   Gramática Libre de Contexto:
   S → aSa | bSb | a | b | ε
   
   Estrategia de la MT:
   • Comparar símbolo izquierdo con derecho
   • Marcar ambos extremos
   • Avanzar hacia el centro
   • Si todos coinciden → ACEPTAR

3. L = {a^n b^2n | n ≥ 1}
   ──────────────────────
   • Por cada 'a' debe haber exactamente 2 'b's
   • Ejemplos válidos: abb, aabbbb, aaabbbbbb
   • Ejemplos inválidos: ab, aabbb, abbb
   
   Gramática Libre de Contexto:
   S → aSbb | abb
   
   Estrategia de la MT:
   • Por cada 'a', buscar y marcar 2 'b's
   • Si no hay suficientes 'b's → RECHAZAR
   • Si sobran 'b's → RECHAZAR
   • Si la proporción es exacta → ACEPTAR

JERARQUÍA DE CHOMSKY:
─────────────────────

Tipo 0: Lenguajes Recursivamente Enumerables (Máquinas de Turing)
  ↑
Tipo 1: Lenguajes Sensibles al Contexto
  ↑
Tipo 2: Lenguajes Libres de Contexto (GLC)  ← Los 3 lenguajes implementados
  ↑
Tipo 3: Lenguajes Regulares (Autómatas Finitos)

TESIS DE CHURCH-TURING:
───────────────────────
"Todo lo que es efectivamente calculable puede ser calculado por
una Máquina de Turing"

CARACTERÍSTICAS DE LA IMPLEMENTACIÓN:
─────────────────────────────────────
✓ Reconocimiento de lenguajes no regulares
✓ Uso de memoria ilimitada (cinta infinita)
✓ Marcado de símbolos para seguimiento
✓ Transiciones deterministas
✓ Estados de aceptación y rechazo claros

APLICACIONES:
─────────────
• Verificación de sintaxis en compiladores
• Análisis de patrones en procesamiento de texto
• Validación de estructuras de datos balanceadas
• Fundamento teórico de la computabilidad
• Demostración de límites de computación

PROPIEDADES:
────────────
• Decidibilidad: Estos lenguajes son decidibles
• Complejidad: Tiempo lineal O(n²) o O(n³)
• Memoria: Espacio lineal O(n)
• Determinismo: Transiciones únicas y predecibles
"""
        teoria_texto.insert(tk.END, info)
        teoria_texto.config(state=tk.DISABLED)
    
    def mostrar_ejemplos(self):
        """Muestra ejemplos predefinidos"""
        ejemplos_window = tk.Toplevel(self.root)
        ejemplos_window.title("Ejemplos de Lenguajes")
        ejemplos_window.geometry("600x500")
        
        ttk.Label(ejemplos_window, text="Seleccione un ejemplo:",
                 font=("Arial", 12, "bold")).pack(pady=15)
        
        ejemplos = [
            ("a^n b^n c^n", "abc", "abc (válido)", True),
            ("a^n b^n c^n", "aabbcc", "aabbcc (válido)", True),
            ("a^n b^n c^n", "aaabbbccc", "aaabbbccc (válido)", True),
            ("a^n b^n c^n", "aabbc", "aabbc (inválido - falta c)", False),
            ("a^n b^n c^n", "abcabc", "abcabc (inválido - intercalado)", False),
            ("Palíndromo", "aba", "aba (válido)", True),
            ("Palíndromo", "abba", "abba (válido)", True),
            ("Palíndromo", "aabbaa", "aabbaa (válido)", True),
            ("Palíndromo", "abab", "abab (inválido)", False),
            ("a^n b^2n", "abb", "abb (válido)", True),
            ("a^n b^2n", "aabbbb", "aabbbb (válido)", True),
            ("a^n b^2n", "aaabbbbbb", "aaabbbbbb (válido)", True),
            ("a^n b^2n", "aabbb", "aabbb (inválido)", False),
        ]
        
        canvas = tk.Canvas(ejemplos_window)
        scrollbar = ttk.Scrollbar(ejemplos_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for tipo, cadena, nombre, valido in ejemplos:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            icono = "✅" if valido else "❌"
            
            def hacer_lambda(t=tipo, c=cadena, w=ejemplos_window):
                self.tipo_lenguaje.set(t)
                self.entrada_cadena.delete(0, tk.END)
                self.entrada_cadena.insert(0, c)
                w.destroy()
                self.verificar_cadena()
            
            ttk.Button(frame, text=f"{icono} {tipo}: {nombre}", 
                      command=hacer_lambda, width=50).pack()
        
        canvas.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=(0, 10))
        scrollbar.pack(side="right", fill="y", pady=(0, 10), padx=(0, 10))
    
    def limpiar(self):
        """Limpia los campos"""
        self.entrada_cadena.delete(0, tk.END)
        self.limpiar_resultados()
    
    def limpiar_resultados(self):
        """Limpia los resultados"""
        self.resultado_texto.delete(1.0, tk.END)
        self.traza_texto.delete(1.0, tk.END)
        self.tabla_texto.delete(1.0, tk.END)


def main():
    root = tk.Tk()
    app = InterfazMTLenguajes(root)
    root.mainloop()


if __name__ == "__main__":
    main()
