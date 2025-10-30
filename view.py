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

        ttk.Label(form_container, text="Nome").grid(row=0, column=0, sticky='w', pady=5)
        self.entryNome = ttk.Entry(form_container)
        self.entryNome.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(0,2))


        ttk.Label(form_container, text="Idade").grid(row=1, column=1)