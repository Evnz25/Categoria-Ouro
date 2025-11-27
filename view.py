import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from controller import Controller

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Categoria Ouro")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        self.registro_id = None

        self.controller = Controller(self)

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def criar_tela_inicial(self):
        self.tela_inicial = tk.Frame(self.container, bg="#DBA457")
        self.tela_inicial.grid(row=0, column=0, sticky='nsew')

        cabecalho_frame = tk.Frame(self.tela_inicial, bg="#DBA457")
        cabecalho_frame.pack(padx=40, pady=20, fill='x')

        ttk.Label(cabecalho_frame, text="Categoria Ouro", font=("Inter", 28, "bold"), background="#DBA457").pack(anchor='w')

        botoes_frame = tk.Frame(cabecalho_frame, bg="#DBA457")
        botoes_frame.pack(anchor='w', pady=15)

        ttk.Button(botoes_frame, text="CALCULAR", command=self.mostrar).pack(side="left")
        ttk.Button(botoes_frame, text="REGISTROS", command=self.mostrar).pack(side="left", padx=10)

        tk.Frame(self.tela_inicial, height=10, bg="black").pack(fill='x')

    def criar_tela_insercao(self):
        self.tela_insercao = tk.Frame(self.container, bg="#DBA457")
        self.tela_insercao.grid(row=0, column=0, sticky='nsew')

        form_container = ttk.Frame(self.tela_insercao)
        form_container.pack(padx=40, pady=20, fill='x')

        ttk.Label(form_container, text="NOME").grid(row=0, column=0, sticky='w', pady=5)
        self.entryNome = ttk.Entry(form_container)
        self.entryNome.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="IDADE").grid(row=1, column=1, sticky='w', pady=5)
        self.entryIdade = ttk.Entry(form_container)
        self.entryIdade.grid(row=2, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="PESO").grid(row=1, column=1, sticky='w', pady=5)
        self.entryPeso = ttk.Entry(form_container)
        self.entryPeso.grid(row=2, column=2, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="ALTURA").grid(row=1, column=1, sticky='w', pady=5)
        self.entryAltura = ttk.Entry(form_container)
        self.entryAltura.grid(row=2, column=3, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="FLEXIBILIDADE").grid(row=1, column=1, sticky='w', pady=5)
        self.entryFlexibilidade = ttk.Entry(form_container)
        self.entryFlexibilidade.grid(row=3, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="ABDOMINAL").grid(row=1, column=1, sticky='w', pady=5)
        self.entryAbdominal = ttk.Entry(form_container)
        self.entryAbdominal.grid(row=4, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="ARREMESSO").grid(row=1, column=1, sticky='w', pady=5)
        self.entryArremesso = ttk.Entry(form_container)
        self.entryArremesso.grid(row=5, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="SALTO HORIZONTAL").grid(row=1, column=1, sticky='w', pady=5)
        self.entrySaltoHor = ttk.Entry(form_container)
        self.entrySaltoHor.grid(row=6, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="SALTO VERTICAL").grid(row=1, column=1, sticky='w', pady=5)
        self.entrySaltoVert = ttk.Entry(form_container)
        self.entrySaltoVert.grid(row=7, column=1, columnspan=2, sticky="ew", padx=(0,2))

        ttk.Label(form_container, text="QUADRADO 4x4").grid(row=1, column=1, sticky='w', pady=5)
        self.entryQuadrado = ttk.Entry(form_container)
        self.entryQuadrado.grid(row=8, column=1, columnspan=2, sticky="ew", padx=(0,2))

        btn_voltar = ttk.Button(
            self.tela_anotacao, 
            text="Voltar para o Início", 
            command=self.mostrar_tela_inicial)
        btn_voltar.pack(side="bottom", pady=20)

        self.btn_cadastrar = ttk.Button(
            self.tela_anotacao, 
            text="Calcular", 
            command=self.calcular)
        self.btn_cadastrar.pack(side="bottom", pady=20)

        #btn de salvar

    def criar_tela_registro(self):
        self.tela_registro = tk.Frame(self.container, bg="#DBA457")
        self.tela_registro.grid(row=0, column=0, sticky='nsew')

        cabeçalho_frame = tk.Frame(self.tela_inicial, bg="#DBA457")
        cabeçalho_frame.pack(pady=20, padx=40, fill='x')
        
        ttk.Label(cabeçalho_frame, text="REGISTROS", font=("Inter", 28, "bold"), background="#DBA457").pack(anchor='w')

        frame_filtro = tk.Frame(self.tela_registro, bg="#DBA457")
        frame_filtro.pack(fill='x', padx=40, pady=10)

        ttk.Label(frame_filtro, text="CATEGORIA", font=("Inter", 10, "bold"), background="#DBA457").pack(anchor='w')

        linha_filtro = tk.Frame(frame_filtro, bg="#DBA457")
        linha_filtro.pack(fill='x', pady=5)

        self.combo_categoria = ttk.Combobox(linha_filtro, values=["GERAL", "FUTEBOL", "VOLEI", "BASQUETE", "CAPOEIRA"])
        self.combo_categoria.current(0) 
        self.combo_categoria.pack(side='left', ipadx=20)

        btn_filtrar = tk.Button(
            linha_filtro, 
            text="FILTRAR", 
            bg="#333333", 
            fg="white", 
            bd=0,
            padx=15
        )
        btn_filtrar.pack(side='left', padx=10)

        self.area_resultados = tk.Frame(self.tela_registro, bg="#DBA457")
        self.area_resultados.pack(fill='both', expand=True, padx=40, pady=20)

        card = tk.Frame(self.area_resultados, bg="white")
        card.pack(fill='x', pady=5) 

        infos_card = tk.Frame(card, bg="white")
        infos_card.pack(side='left', padx=15, pady=10)

        tk.Label(infos_card, text="NOME : EVANDRO NICOLAU ZANELLI", bg="white", anchor="w").pack(fill='x')
        tk.Label(infos_card, text="IDADE : 19", bg="white", anchor="w").pack(fill='x')
        tk.Label(infos_card, text="CLASSIFICAÇÃO: FUTEBOL", bg="white", anchor="w").pack(fill='x')

        btn_excluir = tk.Button(
            card, 
            text="EXCLUIR", 
            bg="#333333", 
            fg="white",
            bd=0,
            padx=10,
            pady=5
        )
        btn_excluir.pack(side='right', padx=15)

        btn_voltar = tk.Button(
            self.tela_registro, 
            text="VOLTAR", 
            bg="#333333", 
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.criar_tela_inicial 
        )
        btn_voltar.pack(side='bottom', anchor='w', padx=40, pady=40)

        def mostrar_tela_inicial(self):
            self.tela_inicial.tkraise()

        def mostrar_tela_insercao(self):
            self.tela_insercao.tkraise()

        def mostrar_tela_registro(self):
            self.tela_registro.tkraise() 