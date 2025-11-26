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
    """Interfaz gráfica para Máquina de Turing de lenguajes"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Reconocimiento de Lenguajes")
        self.root.geometry("1100x750")
        
        self.maquina = MaquinaTuringLenguajes()
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, 
                          text="Máquina de Turing - Reconocimiento de Lenguajes Formales",
                          font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 5))
        
        # Autores
        autores = ttk.Label(main_frame,
                           text="👨‍💻 Juan Esteban Cardozo Rivera  •  Juan Sebastián Gómez Usuga",
                           font=("Arial", 10))
        autores.grid(row=1, column=0, columnspan=2, pady=(0, 15))
        
        # Frame de entrada
        entrada_frame = ttk.LabelFrame(main_frame, text=" Configuración ", padding="12")
        entrada_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Selección de lenguaje
        ttk.Label(entrada_frame, text="Lenguaje:", 
                 font=("Arial", 9, "bold")).grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        
        self.tipo_lenguaje = ttk.Combobox(entrada_frame,
                                          values=["a^n b^n c^n", "Palíndromo", "a^n b^2n"],
                                          state="readonly",
                                          width=15)
        self.tipo_lenguaje.set("a^n b^n c^n")
        self.tipo_lenguaje.grid(row=0, column=1, padx=5)
        
        # Cadena de entrada
        ttk.Label(entrada_frame, text="Cadena:", 
                 font=("Arial", 9, "bold")).grid(row=0, column=2, sticky=tk.W, padx=(20, 8))
        
        self.entrada_cadena = ttk.Entry(entrada_frame, width=25, font=("Consolas", 10))
        self.entrada_cadena.insert(0, "aabbcc")
        self.entrada_cadena.grid(row=0, column=3)
        self.entrada_cadena.bind('<Return>', lambda e: self.verificar_cadena())
        
        # Botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        
        ttk.Button(botones_frame, text="▶️ Verificar",
                  command=self.verificar_cadena, width=15).pack(side=tk.LEFT, padx=3)
        ttk.Button(botones_frame, text="🗑️ Limpiar",
                  command=self.limpiar, width=15).pack(side=tk.LEFT, padx=3)
        ttk.Button(botones_frame, text="📚 Ejemplos",
                  command=self.mostrar_ejemplos, width=15).pack(side=tk.LEFT, padx=3)
        
        # Notebook
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        main_frame.rowconfigure(4, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Crear pestañas
        self.crear_pestanas()
    
    def crear_pestanas(self):
        # Pestaña: Resultado
        resultado_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(resultado_frame, text="📊 Resultado")
        
        self.texto_resultado = scrolledtext.ScrolledText(resultado_frame,
                                                         height=22,
                                                         font=("Consolas", 9),
                                                         wrap=tk.WORD)
        self.texto_resultado.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña: Transiciones
        trans_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(trans_frame, text="🔄 Transiciones")
        
        self.texto_transiciones = scrolledtext.ScrolledText(trans_frame,
                                                            height=22,
                                                            font=("Consolas", 8),
                                                            wrap=tk.NONE)
        self.texto_transiciones.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña: Información
        info_frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(info_frame, text="ℹ️ Info")
        
        info_text = """
LENGUAJES IMPLEMENTADOS

📚 a^n b^n c^n (Tipo 1 - Sensible al Contexto)
   Reconoce cadenas con igual cantidad de a's, b's y c's consecutivas.
   Ejemplos válidos: abc, aabbcc, aaabbbccc
   
📚 Palíndromo (Tipo 2 - Libre de Contexto)
   Reconoce cadenas que se leen igual en ambas direcciones.
   Ejemplos válidos: aba, abba, aabbaa
   
📚 a^n b^2n (Tipo 2 - Libre de Contexto)  
   Reconoce cadenas con el doble de b's que de a's.
   Ejemplos válidos: abb, aabbbb, aaabbbbbb

USO:
1. Seleccione el lenguaje a verificar
2. Ingrese la cadena
3. Presione "Verificar" o Enter
4. Revise el resultado y las transiciones
        """
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT, font=("Consolas", 9))
        info_label.pack(anchor=tk.W)
    
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
        self.texto_resultado.tag_config("header", foreground="#0066CC", font=("Consolas", 11, "bold"))
        self.texto_resultado.tag_config("success", foreground="#00AA00", font=("Consolas", 10, "bold"))
        self.texto_resultado.tag_config("error", foreground="#CC0000", font=("Consolas", 10, "bold"))
        self.texto_resultado.tag_config("info", foreground="#0066CC", font=("Consolas", 9))
        
        # Encabezado
        self.texto_resultado.insert(tk.END, "\n╔" + "═" * 70 + "╗\n")
        
        if aceptada:
            self.texto_resultado.insert(tk.END, "║          ✅ CADENA ACEPTADA          ║\n", "success")
        else:
            self.texto_resultado.insert(tk.END, "║          ❌ CADENA RECHAZADA          ║\n", "error")
        
        self.texto_resultado.insert(tk.END, "╚" + "═" * 70 + "╝\n\n")
        
        # Información
        self.texto_resultado.insert(tk.END, "📋 Lenguaje: ", "info")
        self.texto_resultado.insert(tk.END, f"{tipo}\n")
        self.texto_resultado.insert(tk.END, "📋 Definición: ", "info")
        self.texto_resultado.insert(tk.END, f"{lenguaje_desc}\n\n")
        
        # Cadena
        self.texto_resultado.insert(tk.END, "🔤 Cadena: ", "info")
        if cadena:
            self.texto_resultado.insert(tk.END, f"'{cadena}'\n")
        else:
            self.texto_resultado.insert(tk.END, "ε (vacía)\n")
        
        # Estadísticas
        self.texto_resultado.insert(tk.END, "📊 Pasos: ", "info")
        self.texto_resultado.insert(tk.END, f"{len(historial)}\n")
        self.texto_resultado.insert(tk.END, "📊 Estado final: ", "info")
        self.texto_resultado.insert(tk.END, f"{self.maquina.estado_actual}\n\n")
        
        # Veredicto
        if aceptada:
            self.texto_resultado.insert(tk.END, f"✓ La cadena pertenece al lenguaje {tipo}\n", "success")
        else:
            self.texto_resultado.insert(tk.END, f"✗ La cadena NO pertenece al lenguaje {tipo}\n", "error")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.texto_resultado.insert(tk.END, f"\n⏰ {timestamp}\n")
    
    def mostrar_traza(self, historial):
        """Muestra la traza de ejecución"""
        # Configurar tags para colores
        self.texto_transiciones.tag_configure("header", foreground="#2C5F7C", font=("Arial", 10, "bold"))
        self.texto_transiciones.tag_configure("paso", foreground="#1E4D6B", font=("Consolas", 9))
        self.texto_transiciones.tag_configure("estado", foreground="#6A1B9A", font=("Consolas", 9, "bold"))
        self.texto_transiciones.tag_configure("cinta", foreground="#D32F2F", font=("Consolas", 9))
        self.texto_transiciones.tag_configure("normal", foreground="#424242", font=("Consolas", 9))
        
        self.texto_transiciones.insert(tk.END, "🎬 TRAZA DE EJECUCIÓN\n", "header")
        self.texto_transiciones.insert(tk.END, "═" * 100 + "\n\n", "header")
        
        # Encabezado de tabla con mejor formato
        self.texto_transiciones.insert(tk.END, "┌" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┬" + "─" * 12, "normal")
        self.texto_transiciones.insert(tk.END, "┬" + "─" * 32, "normal")
        self.texto_transiciones.insert(tk.END, "┬" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┬" + "─" * 8, "normal")
        self.texto_transiciones.insert(tk.END, "┬" + "─" * 30 + "┐\n", "normal")
        
        self.texto_transiciones.insert(tk.END, f"│{'Paso':^6}│{'Estado':^12}│{'Cinta':^32}│{'Pos':^6}│{'Lee':^8}│{'Acción':^30}│\n", "header")
        
        self.texto_transiciones.insert(tk.END, "├" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┼" + "─" * 12, "normal")
        self.texto_transiciones.insert(tk.END, "┼" + "─" * 32, "normal")
        self.texto_transiciones.insert(tk.END, "┼" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┼" + "─" * 8, "normal")
        self.texto_transiciones.insert(tk.END, "┼" + "─" * 30 + "┤\n", "normal")
        
        # Mostrar cada paso con colores alternados
        for i, paso in enumerate(historial):
            paso_num = str(paso['paso'])
            estado = paso['estado']
            cinta_completa = paso['cinta']
            
            # Truncar cinta si es muy larga, mostrando posición del cabezal
            pos = paso['posicion']
            if len(cinta_completa) > 30:
                inicio = max(0, pos - 15)
                fin = min(len(cinta_completa), pos + 16)
                cinta = cinta_completa[inicio:fin]
                if inicio > 0:
                    cinta = "..." + cinta
                if fin < len(cinta_completa):
                    cinta = cinta + "..."
            else:
                cinta = cinta_completa
                
            simbolo = paso['simbolo']
            accion = paso['accion']
            if len(accion) > 28:
                accion = accion[:25] + "..."
            
            tag = "paso" if i % 2 == 0 else "normal"
            
            self.texto_transiciones.insert(tk.END, f"│{paso_num:^6}│", tag)
            self.texto_transiciones.insert(tk.END, f"{estado:^12}│", "estado")
            self.texto_transiciones.insert(tk.END, f"{cinta:^32}│", "cinta")
            self.texto_transiciones.insert(tk.END, f"{str(pos):^6}│", tag)
            self.texto_transiciones.insert(tk.END, f"{simbolo:^8}│", tag)
            self.texto_transiciones.insert(tk.END, f"{accion:^30}│\n", tag)
        
        self.texto_transiciones.insert(tk.END, "└" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┴" + "─" * 12, "normal")
        self.texto_transiciones.insert(tk.END, "┴" + "─" * 32, "normal")
        self.texto_transiciones.insert(tk.END, "┴" + "─" * 6, "normal")
        self.texto_transiciones.insert(tk.END, "┴" + "─" * 8, "normal")
        self.texto_transiciones.insert(tk.END, "┴" + "─" * 30 + "┘\n", "normal")
        
        self.texto_transiciones.insert(tk.END, f"\n📊 Total de pasos: {len(historial)}\n", "header")
    
    def mostrar_tabla_transiciones(self, tipo):
        """Muestra información sobre las transiciones (eliminada para simplificar)"""
        pass
    
    def limpiar_resultados(self):
        """Limpia los textos de resultado"""
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_transiciones.delete(1.0, tk.END)
    
    def limpiar_resultados(self):
        """Limpia los textos de resultado"""
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_transiciones.delete(1.0, tk.END)
    
    def limpiar(self):
        """Limpia todos los campos"""
        self.entrada_cadena.delete(0, tk.END)
        self.limpiar_resultados()
    
    def mostrar_ejemplos(self):
        """Muestra ejemplos predefinidos"""
        ejemplos_window = tk.Toplevel(self.root)
        ejemplos_window.title("Ejemplos de Lenguajes")
        ejemplos_window.geometry("600x450")
        
        ttk.Label(ejemplos_window, text="Seleccione un ejemplo:",
                 font=("Arial", 11, "bold")).pack(pady=12)
        
        ejemplos = [
            ("a^n b^n c^n", "abc"),
            ("a^n b^n c^n", "aabbcc"),
            ("a^n b^n c^n", "aaabbbccc"),
            ("Palíndromo", "aba"),
            ("Palíndromo", "abba"),
            ("Palíndromo", "aabbaa"),
            ("a^n b^2n", "abb"),
            ("a^n b^2n", "aabbbb"),
            ("a^n b^2n", "aaabbbbbb"),
        ]
        
        for tipo, cadena in ejemplos:
            def hacer_lambda(t=tipo, c=cadena, w=ejemplos_window):
                self.tipo_lenguaje.set(t)
                self.entrada_cadena.delete(0, tk.END)
                self.entrada_cadena.insert(0, c)
                w.destroy()
                self.verificar_cadena()
            
            ttk.Button(ejemplos_window, text=f"{tipo}: {cadena}", 
                      command=hacer_lambda, width=35).pack(pady=3)


def main():
    root = tk.Tk()
    app = InterfazMTLenguajes(root)
    root.mainloop()


if __name__ == "__main__":
    main()
