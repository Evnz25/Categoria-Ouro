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

        self.criar_tela_inicial()
        self.criar_tela_insercao()
        self.criar_tela_registro()

        self.mostrar_tela_inicial()

        self.root.mainloop()

    def criar_tela_inicial(self):
        self.tela_inicial = tk.Frame(self.container, bg="#DBA457")
        self.tela_inicial.grid(row=0, column=0, sticky='nsew')

        cabecalho_frame = tk.Frame(self.tela_inicial, bg="#DBA457")
        cabecalho_frame.pack(padx=40, pady=20, fill='x')

        ttk.Label(cabecalho_frame, text="Categoria Ouro", font=("Inter", 28, "bold"), background="#DBA457").pack(anchor='w')

        botoes_frame = tk.Frame(cabecalho_frame, bg="#DBA457")
        botoes_frame.pack(anchor='w', pady=15)

        tk.Button(botoes_frame, 
            text="CALCULAR", 
            bg="#333333", 
            fg="white",
            font=("Inter", 10, "bold"),
            command=self.mostrar_tela_insercao,
            bd=0, padx=20, pady=8,).pack(side="left")
        
        tk.Button(botoes_frame,
            text="REGISTROS",
            bg="#333333", 
            fg="white",
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.mostrar_tela_registro).pack(side="left", padx=10)

        tk.Frame(self.tela_inicial, height=10, bg="black").pack(fill='x')

    def criar_tela_insercao(self):
        self.tela_insercao = tk.Frame(self.container, bg="#DBA457")
        self.tela_insercao.grid(row=0, column=0, sticky='nsew')

        form_container = tk.Frame(self.tela_insercao, bg="#DBA457")
        form_container.pack(padx=40, pady=20, fill='both', expand=True)

        lbl_config = {"bg": "#DBA457", "font": ("Inter", 10), "anchor": "w"}

        tk.Label(form_container, text="NOME :", **lbl_config).grid(row=0, column=0, sticky='w', pady=10)
        self.entryNome = ttk.Entry(form_container)
        self.entryNome.grid(row=0, column=1, sticky="ew", padx=10)
        
        form_container.grid_columnconfigure(1, weight=1)

        frame_medidas = tk.Frame(form_container, bg="#DBA457")
        frame_medidas.grid(row=1, column=0, columnspan=2, sticky='w', pady=10)

        tk.Label(frame_medidas, text="IDADE :", **lbl_config).pack(side="left")
        self.entryIdade = ttk.Entry(frame_medidas, width=5)
        self.entryIdade.pack(side="left", padx=(5, 20))

        tk.Label(frame_medidas, text="PESO :", **lbl_config).pack(side="left")
        self.entryPeso = ttk.Entry(frame_medidas, width=8)
        self.entryPeso.pack(side="left", padx=(5, 20))

        tk.Label(frame_medidas, text="ALTURA :", **lbl_config).pack(side="left")
        self.entryAltura = ttk.Entry(frame_medidas, width=8)
        self.entryAltura.pack(side="left", padx=(5, 0))

        tk.Label(form_container, text="FLEXIBILIDADE :", **lbl_config).grid(row=2, column=0, sticky='w', pady=10)
        self.entryFlexibilidade = ttk.Entry(form_container, width=15) # Menorzinha igual a foto
        self.entryFlexibilidade.grid(row=2, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="ABDOMINAL :", **lbl_config).grid(row=3, column=0, sticky='w', pady=10)
        self.entryAbdominal = ttk.Entry(form_container, width=10)
        self.entryAbdominal.grid(row=3, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="ARREMESSO (Medical Ball):", **lbl_config).grid(row=4, column=0, sticky='w', pady=10)
        self.entryArremesso = ttk.Entry(form_container, width=10)
        self.entryArremesso.grid(row=4, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="SALTO HORIZONTAL:", **lbl_config).grid(row=5, column=0, sticky='w', pady=10)
        self.entrySaltoHor = ttk.Entry(form_container, width=25)
        self.entrySaltoHor.grid(row=5, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="SALTO VERTICAL:", **lbl_config).grid(row=6, column=0, sticky='w', pady=10)
        self.entrySaltoVert = ttk.Entry(form_container, width=25)
        self.entrySaltoVert.grid(row=6, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="QUADRADO 4x4M :", **lbl_config).grid(row=7, column=0, sticky='w', pady=10)
        self.entryQuadrado = ttk.Entry(form_container, width=25)
        self.entryQuadrado.grid(row=7, column=1, sticky="w", padx=10)

        tk.Label(form_container, text="CLASSIFICAÇÃO:", **lbl_config).grid(row=8, column=0, sticky='w', pady=10)

        botoes_frame = tk.Frame(self.tela_insercao, bg="#DBA457")
        botoes_frame.pack(side="bottom", fill="x", padx=40, pady=30)

        btn_voltar = tk.Button(
            botoes_frame, 
            text="VOLTAR", 
            bg="#333333", 
            fg="white",   
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.mostrar_tela_inicial
        )
        btn_voltar.pack(side="left")
        
        self.btn_cadastrar = tk.Button(
            botoes_frame, 
            text="CALCULAR", 
            bg="#333333", 
            fg="white",
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.calcular
        )
        self.btn_cadastrar.pack(side="right") 

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

    def calcular(self):
        pass  # Implementar a lógica de cálculo aqui


if __name__ == "__main__":
    app = View()