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
        self.lbl_resultado_valor = tk.Label(
            form_container, 
            text="",                # Começa vazio
            bg="#DBA457", 
            fg="#333333",           # Cor do texto (escuro para destaque)
            font=("Inter", 14, "bold") 
        )
        self.lbl_resultado_valor.grid(row=8, column=1, sticky="w", padx=10)

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

        
        self.btn_salvar_banco = tk.Button(
            self.botoes_frame,
            text="SALVAR NO BANCO",
            bg="#006400", # Verde escuro para diferenciar
            fg="white", 
            font=("Inter", 10, "bold"),
            bd=0, padx=20, pady=8,
            command=self.salvar_no_banco # Nova função
        )


    def criar_tela_registro(self):
        self.tela_registro = tk.Frame(self.container, bg="#DBA457")
        self.tela_registro.grid(row=0, column=0, sticky='nsew')

        # --- CABEÇALHO ---
        cabeçalho_frame = tk.Frame(self.tela_registro, bg="#DBA457")
        cabeçalho_frame.pack(pady=20, padx=40, fill='x')
        ttk.Label(cabeçalho_frame, text="REGISTROS", font=("Inter", 28, "bold"), background="#DBA457").pack(anchor='w')

        # --- FILTROS ---
        frame_filtro = tk.Frame(self.tela_registro, bg="#DBA457")
        frame_filtro.pack(fill='x', padx=40, pady=10)
        
        # (Seus filtros continuam aqui...)
        ttk.Label(frame_filtro, text="CATEGORIA", font=("Inter", 10, "bold"), background="#DBA457").pack(anchor='w')
        linha_filtro = tk.Frame(frame_filtro, bg="#DBA457")
        linha_filtro.pack(fill='x', pady=5)
        
        self.combo_categoria = ttk.Combobox(linha_filtro, values=["GERAL", "FUTEBOL", "VOLEI", "BASQUETE", "CAPOEIRA"])
        self.combo_categoria.current(0) 
        self.combo_categoria.pack(side='left', ipadx=20)
        
        btn_filtrar = tk.Button(linha_filtro, text="FILTRAR", bg="#333333", fg="white", bd=0, padx=15, command=self.filtrar_lista)
        btn_filtrar.pack(side='left', padx=10)

        # --- ÁREA DE SCROLL (IMPORTANTE PARA LISTA) ---
        # Criamos um Canvas para poder rolar a página
        self.canvas_area = tk.Canvas(self.tela_registro, bg="#DBA457", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.tela_registro, orient="vertical", command=self.canvas_area.yview)
        
        # Frame que vai conter os cards (dentro do canvas)
        self.frame_lista_cards = tk.Frame(self.canvas_area, bg="#DBA457")
        
        # Configuração do Scroll
        self.canvas_area.create_window((0, 0), window=self.frame_lista_cards, anchor="nw")
        self.canvas_area.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas_area.pack(side="left", fill="both", expand=True, padx=40)
        self.scrollbar.pack(side="right", fill="y")

        # Atualiza o tamanho do scroll quando adicionamos coisas
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
        # Sempre que mostrar a tela, recarrega a lista do banco
        self.atualizar_lista_registros()
        self.tela_registro.tkraise()

    
    def atualizar_lista_registros(self, filtro=None):
        """
        1. Limpa a lista atual
        2. Busca no Controller
        3. Cria os Cards
        """
        # Limpar widgets antigos
        for widget in self.frame_lista_cards.winfo_children():
            widget.destroy()

        # Buscar dados (Se tiver filtro usa o filtrado, senão pega tudo)
        if filtro and filtro != "GERAL":
            registros = self.controller.listar_registros_filtrado_controller({"Classificacao": filtro})
        else:
            registros = self.controller.listar_registros_controller()

        if not registros:
            tk.Label(self.frame_lista_cards, text="Nenhum registro encontrado.", bg="#DBA457").pack(pady=20)
            return

        # Criar Cards
        for item in registros:
            self.criar_card_atleta(item)

    def criar_card_atleta(self, dados_atleta):
        """ Cria o visual do card branco """
        card = tk.Frame(self.frame_lista_cards, bg="white")
        card.pack(fill='x', pady=5, ipady=5)

        # Evento de Clique: Ao clicar no Frame, carrega o atleta
        # Usamos lambda para passar os dados desse atleta específico
        card.bind("<Button-1>", lambda e, d=dados_atleta: self.carregar_atleta_para_edicao(d))

        infos_card = tk.Frame(card, bg="white")
        infos_card.pack(side='left', padx=15, pady=5)
        
        # Precisamos propagar o clique para os labels também
        lbl_nome = tk.Label(infos_card, text=f"NOME : {dados_atleta.get('Nome', '--')}", bg="white", anchor="w", font=("Inter", 10, "bold"))
        lbl_nome.pack(fill='x')
        
        lbl_idade = tk.Label(infos_card, text=f"IDADE : {dados_atleta.get('Idade', '--')}", bg="white", anchor="w")
        lbl_idade.pack(fill='x')
        
        lbl_class = tk.Label(infos_card, text=f"CLASSIFICAÇÃO: {dados_atleta.get('Classificacao', '--')}", bg="white", anchor="w", fg="blue")
        lbl_class.pack(fill='x')

        # Bind no clique dos textos também
        for w in [infos_card, lbl_nome, lbl_idade, lbl_class]:
            w.bind("<Button-1>", lambda e, d=dados_atleta: self.carregar_atleta_para_edicao(d))

        # Botão Excluir (Funcional)
        btn_excluir = tk.Button(
            card, 
            text="EXCLUIR", 
            bg="#333333", fg="white", bd=0, padx=10, pady=5,
            command=lambda: self.deletar_atleta(dados_atleta.get('_id'))
        )
        btn_excluir.pack(side='right', padx=15)

    
    def carregar_atleta_para_edicao(self, dados):
        """
        Pega os dados do dicionário e preenche a tela de inserção
        """
        # 1. Muda para a tela de inserção
        self.mostrar_tela_insercao()
        
        # 2. Limpa os campos
        self.limpar_campos_insercao() # Crie essa função auxiliar ou faça linha a linha
        
        # 3. Preenche os campos
        # Dica: O MongoDB retorna números, converta para string se precisar
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
        
        # 4. Preenche a Classificação (usando a lógica do Entry Travado)
        self.entryClassificacao.config(state='normal')
        self.entryClassificacao.delete(0, 'end')
        self.entryClassificacao.insert(0, dados.get('Classificacao', ''))
        self.entryClassificacao.config(state='readonly')

        # 5. Guarda o ID para saber que é uma edição (se quiser implementar Update depois)
        self.id_atleta_em_edicao = dados.get('_id')
        
        # Mostra o botão salvar (talvez você queira mudar o texto para "ATUALIZAR" no futuro)
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
        """
        Recebe o resultado (ex: "BASQUETE") e coloca no Entry
        """
        # 1. Destrava o campo para o código poder escrever
        self.entryClassificacao.config(state='normal')
        
        # 2. Limpa o que tinha antes (caso já tivesse calculado outro)
        self.entryClassificacao.delete(0, tk.END)
        
        # 3. Escreve a nova classificação
        self.entryClassificacao.insert(0, classificacao)
        
        # 4. Trava de novo para o usuário não mexer
        self.entryClassificacao.config(state='readonly')
        
        # 5. Mostra o botão de salvar
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

        resultado = self.controller.calcular_classificacao(dados)

        if resultado and "Erro" in resultado:
            messagebox.showwarning("Atenção", resultado)

        elif resultado:
            # 4. Exibir o resultado na tela
            # Se você estiver usando o Entry Travado (Opção A):
            self.entryClassificacao.config(state='normal') # Destrava
            self.entryClassificacao.delete(0, 'end')       # Limpa
            self.entryClassificacao.insert(0, resultado)   # Escreve
            self.entryClassificacao.config(state='readonly') # Trava de novo

            self.btn_salvar_banco.pack(side="right", padx=10)

            messagebox.showinfo("Resultado", f"O atleta foi classificado como: {resultado}")
        
        else:
            messagebox.showerror("Erro", "Não foi possível calcular. Verifique os dados.")
        

    def salvar_registros(self):
        dados = {
            'nome': self.entryNome.get(),
            'idade': self.entryIdade.get(),
            'peso': self.entryPeso.get(),
            'altura': self.entryAltura.get(),
            'flexibilidade': self.entryFlexibilidade.get(),
            'abdominal': self.entryAbdominal.get(),
            'arremesso': self.entryArremesso.get(),
            'saltoHor': self.entrySaltoHor.get(),
            'saltoVert': self.entrySaltoVert.get(),
            'quadrado': self.entryQuadrado.get(),
            'classificacao': self.entryClassificacao.get()
        }

        sucesso = self.controller.salvar_registro_controller(
            dados['nome'], dados['idade'], dados['peso'], dados['altura'], dados['flexibilidade'],
            dados['abdominal'], dados['arremesso'], dados['saltoHor'],
            dados['saltoVert'], dados['quadrado'], dados['classificacao']
        )

        if sucesso:
            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
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
            self.entryQuadrado.classificacao(0, 'end')
        else:
            messagebox.showerror("Erro no Banco de Dados", "Não foi possível salvar o registro.")


if __name__ == "__main__":
    app = View()