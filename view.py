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
        
        tk.Button(botoes_frame,
            text="RECALIBRAR IA",
            bg="#0056b3", # Azul
            fg="white", font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.acao_recalibrar).pack(side="left", padx=10)

        tk.Frame(self.tela_inicial, height=10, bg="black").pack(fill='x')


    def acao_recalibrar(self):
        resposta = messagebox.askyesno("Confirmar", "Deseja recalibrar a IA usando todos os dados salvos no banco?\nIsso pode melhorar a precisão se houver novos registros.")
        if resposta:
            mensagem = self.controller.recalibrar_ia_controller()
            messagebox.showinfo("Status da IA", mensagem)

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
        self.entryClassificacao = ttk.Entry(
            form_container, 
            font=("Inter", 10, "bold"),
            state="readonly" 
        )
        self.entryClassificacao.grid(row=8, column=1, sticky="ew", padx=10)

        self.botoes_frame = tk.Frame(self.tela_insercao, bg="#DBA457")
        self.botoes_frame.pack(side="bottom", fill="x", padx=40, pady=30)

        btn_voltar = tk.Button(
            self.botoes_frame, 
            text="VOLTAR", 
            bg="#333333", 
            fg="white",   
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.mostrar_tela_inicial
        )
        btn_voltar.pack(side="left")
        
        self.btn_cadastrar = tk.Button(
            self.botoes_frame, 
            text="CALCULAR", 
            bg="#333333", 
            fg="white",
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.calcular
        )
        self.btn_cadastrar.pack(side="right") 

        
        self.btn_salvar_banco = tk.Button(
            self.botoes_frame,
            text="SALVAR NO BANCO",
            bg="#006400", 
            fg="white", 
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.salvar_registros 
        )


    def criar_tela_registro(self):
        self.tela_registro = tk.Frame(self.container, bg="#DBA457")
        self.tela_registro.grid(row=0, column=0, sticky='nsew')

        cabeçalho_frame = tk.Frame(self.tela_registro, bg="#DBA457")
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
        
        btn_filtrar = tk.Button(linha_filtro, text="FILTRAR", bg="#333333", fg="white", bd=0, padx=15, command=self.filtrar_lista)
        btn_filtrar.pack(side='left', padx=10)

        self.canvas_area = tk.Canvas(self.tela_registro, bg="#DBA457", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.tela_registro, orient="vertical", command=self.canvas_area.yview)
        
        self.frame_lista_cards = tk.Frame(self.canvas_area, bg="#DBA457")
        
        self.canvas_area.create_window((0, 0), window=self.frame_lista_cards, anchor="nw")
        self.canvas_area.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas_area.pack(side="left", fill="both", expand=True, padx=40)
        self.scrollbar.pack(side="right", fill="y")

        self.frame_lista_cards.bind("<Configure>", lambda e: self.canvas_area.configure(scrollregion=self.canvas_area.bbox("all")))

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
        self.atualizar_lista_registros()
        self.tela_registro.tkraise()

    
    def atualizar_lista_registros(self, filtro=None):
        for widget in self.frame_lista_cards.winfo_children():
            widget.destroy()

        if filtro and filtro != "GERAL":
            registros = self.controller.listar_registros_filtrado_controller({"Classificacao": filtro})
        else:
            registros = self.controller.listar_registros_controller()

        if not registros:
            tk.Label(self.frame_lista_cards, text="Nenhum registro encontrado.", bg="#DBA457").pack(pady=20)
            return

        for item in registros:
            self.criar_card_atleta(item)

    def criar_card_atleta(self, dados_atleta):
        card = tk.Frame(self.frame_lista_cards, bg="white")
        card.pack(fill='x', pady=5, ipady=5)

        card.bind("<Button-1>", lambda e, d=dados_atleta: self.carregar_atleta_para_edicao(d))

        infos_card = tk.Frame(card, bg="white")
        infos_card.pack(side='left', padx=15, pady=5)
        
        lbl_nome = tk.Label(infos_card, text=f"NOME : {dados_atleta.get('Nome', '--')}", bg="white", anchor="w", font=("Inter", 10, "bold"))
        lbl_nome.pack(fill='x')
        
        lbl_idade = tk.Label(infos_card, text=f"IDADE : {dados_atleta.get('Idade', '--')}", bg="white", anchor="w")
        lbl_idade.pack(fill='x')
        
        lbl_class = tk.Label(infos_card, text=f"CLASSIFICAÇÃO: {dados_atleta.get('Classificacao', '--')}", bg="white", anchor="w", fg="blue")
        lbl_class.pack(fill='x')

        for w in [infos_card, lbl_nome, lbl_idade, lbl_class]:
            w.bind("<Button-1>", lambda e, d=dados_atleta: self.carregar_atleta_para_edicao(d))

        btn_excluir = tk.Button(
            card, 
            text="EXCLUIR", 
            bg="#333333", fg="white", bd=0, padx=10, pady=5,
            command=lambda: self.deletar_atleta(dados_atleta.get('_id'))
        )
        btn_excluir.pack(side='right', padx=15)

    
    def carregar_atleta_para_edicao(self, dados):
        self.mostrar_tela_insercao()
        
        self.limpar_campos_insercao()
        
        self.entryNome.insert(0, dados.get('Nome', ''))
        self.entryIdade.insert(0, str(dados.get('Idade', '')))
        self.entryPeso.insert(0, str(dados.get('Peso', '')))
        self.entryAltura.insert(0, str(dados.get('Altura', '')))
        self.entryFlexibilidade.insert(0, str(dados.get('Flexibilidade', '')))
        self.entryAbdominal.insert(0, str(dados.get('Abdominal', '')))
        self.entryArremesso.insert(0, str(dados.get('Arremesso', '')))
        self.entrySaltoHor.insert(0, str(dados.get('SaltoHor', '')))
        self.entrySaltoVert.insert(0, str(dados.get('SaltoVer', '')))
        self.entryQuadrado.insert(0, str(dados.get('Quadrado', '')))
        
        self.entryClassificacao.config(state='normal')
        self.entryClassificacao.delete(0, 'end')
        self.entryClassificacao.insert(0, dados.get('Classificacao', ''))
        self.entryClassificacao.config(state='readonly')

        self.id_atleta_em_edicao = dados.get('_id')
        
        self.btn_salvar_banco.pack(side="right", padx=10)

    
    def filtrar_lista(self):
        categoria = self.combo_categoria.get()
        self.atualizar_lista_registros(categoria)


    def deletar_atleta(self, id_atleta):
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este atleta?"):
            self.controller.deletar_registro_controller(id_atleta)
            self.atualizar_lista_registros(self.combo_categoria.get())


    def limpar_campos_insercao(self):
        self.entryNome.delete(0, 'end')
        self.entryIdade.delete(0, 'end')
        self.entryPeso.delete(0, 'end')
        self.entryAltura.delete(0, 'end')
        self.entryFlexibilidade.delete(0, 'end')
        self.entryAbdominal.delete(0, 'end')
        self.entryArremesso.delete(0, 'end')
        self.entrySaltoHor.delete(0, 'end')
        self.entrySaltoVert.delete(0, 'end')
        self.entryQuadrado.delete(0, 'end')
        
        self.entryClassificacao.config(state='normal')
        self.entryClassificacao.delete(0, 'end')
        self.entryClassificacao.config(state='readonly')
        
        self.id_atleta_em_edicao = None


    def exibir_resultado_na_tela(self, classificacao):
        self.entryClassificacao.config(state='normal')
        
        self.entryClassificacao.delete(0, tk.END)
        
        self.entryClassificacao.insert(0, classificacao)
        
        self.entryClassificacao.config(state='readonly')
        
        self.btn_salvar_banco.pack(side="right", padx=10)


    def calcular(self):
        dados = {
            'Nome': self.entryNome.get(),
            'Idade': self.entryIdade.get(),
            'Peso': self.entryPeso.get(),
            'Altura': self.entryAltura.get(),
            'Flexibilidade': self.entryFlexibilidade.get(),
            'Abdominal': self.entryAbdominal.get(),
            'Arremesso': self.entryArremesso.get(),
            'SaltoHor': self.entrySaltoHor.get(),
            'SaltoVer': self.entrySaltoVert.get(),
            'Quadrado': self.entryQuadrado.get()
        }

        retorno = self.controller.calcular_classificacao(dados)
        
        if not retorno or retorno[0] is None:
             messagebox.showerror("Erro", "Falha no cálculo.")
             return

        resultado_classificacao, nome_formatado = retorno

        if "Erro" in resultado_classificacao:
            messagebox.showwarning("Atenção", resultado_classificacao)
        else:
            if nome_formatado:
                self.entryNome.delete(0, 'end')
                self.entryNome.insert(0, nome_formatado)

            self.entryClassificacao.config(state='normal') # Destrava
            self.entryClassificacao.delete(0, 'end')
            self.entryClassificacao.insert(0, resultado_classificacao)
            self.entryClassificacao.config(state='readonly') # Trava

            self.btn_salvar_banco.pack(side="right", padx=10)

            messagebox.showinfo("Resultado", f"O atleta foi classificado como: {resultado_classificacao}")
        

    def salvar_registros(self):
        dados_brutos = {
            'Nome': self.entryNome.get(),
            'Idade': self.entryIdade.get(),
            'Peso': self.entryPeso.get(),
            'Altura': self.entryAltura.get(),
            'Flexibilidade': self.entryFlexibilidade.get(),
            'Abdominal': self.entryAbdominal.get(),
            'Arremesso': self.entryArremesso.get(),
            'SaltoHor': self.entrySaltoHor.get(),
            'SaltoVer': self.entrySaltoVert.get(),
            'Quadrado': self.entryQuadrado.get()
        }
        
        dados_limpos = self.controller.processar_dados_para_salvar(dados_brutos)
        
        if "erro" in dados_limpos:
            messagebox.showerror("Erro", dados_limpos['erro'])
            return

        sucesso = self.controller.salvar_registro_controller(
            dados_limpos['Nome'],  
            dados_limpos['Idade'],
            dados_limpos['Peso'],
            dados_limpos['Altura'],
            dados_limpos['Flexibilidade'],
            dados_limpos['Abdominal'],
            dados_limpos['Arremesso'],
            dados_limpos['SaltoHor'],
            dados_limpos['SaltoVer'],
            dados_limpos['Quadrado'],
            self.entryClassificacao.get() 
        )

        if sucesso:
            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
            self.limpar_campos_insercao()
            self.btn_salvar_banco.pack_forget()
        else:
            messagebox.showerror("Erro", "Não foi possível salvar.")


if __name__ == "__main__":
    app = View()