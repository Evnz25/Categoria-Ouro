from model import Model

class Controller():
    def __init__(self, view):
        self.model = Model()
        self.view = view

    def salvar_registro_controller(self, salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao):
        return self.model.salvar_registro(salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao)

    def mostrar_registro_id_controller(self, registro_id):
        return self.model.mostrar_registro_id(registro_id)
    
    def listar_registros_controller(self):
        return self.model.listar_registros()
    
    def listar_registros_filtrado_controller(self, categoria_filtro):
        return self.model.listar_registros_filtrado(categoria_filtro)
    
    def atualizar_registro_controller(self, registro_id, salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao):
        return self.model.atualizar_registro(registro_id, salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao)
    
    def deletar_registro_controller(self, registro_id):
        return self.model.deletar_registro(registro_id)
    
    def calcular_classificacao(self, dados_dicionario):
        try:
            # 1. Passa pela cadeia de limpeza (Elos)
            dados_limpos = self.cadeia_processamento.processar(dados_dicionario)

            # 2. Prepara lista APENAS com o que a IA foi treinada
            # Ordem do script de treino: 
            # ['Peso', 'Altura', 'Flexibilidade', 'Abdominal', 'Arremesso', 'SaltoHor', 'SaltoVer', 'Quadrado']
            
            lista_para_ia = [
                dados_limpos["Peso"],
                dados_limpos["Altura"],
                dados_limpos["Flexibilidade"],
                dados_limpos["Abdominal"],
                dados_limpos["Arremesso"],
                dados_limpos["SaltoHor"],
                dados_limpos["SaltoVer"],
                dados_limpos["Quadrado"]
            ]

            # 3. Chama o Model
            resultado = self.model.calcular_classificacao_ia(lista_para_ia)
            
            return resultado, dados_limpos["Nome"]

        except Exception as e:
            return f"Erro: {e}", None