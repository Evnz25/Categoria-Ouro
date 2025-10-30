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