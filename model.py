import pymongo
from bson.objectid import Objectid

class Model():
    def __init__(self):
        self.meucliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.meucliente["ClassificacaoOuro"]
        self.registros = self.db["registros"]


    def salvar_registro(self, salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao):
        try: 
            insercao = {
                "Nome": salvar_nome,
                "Idade": salvar_idade,
                "Peso": salvar_peso,
                "Altura": salvar_altura,
                "Flexibilidade": salvar_flexibiliade,
                "Abdominal": salvar_abdominal,
                "Arremesso": salvar_arremesso,
                "SaltoHor": salvar_salto_horizontal,
                "SaltoVer": salvar_salto_vertical,
                "Quadrado": salvar_quadrado,
                "Classificacao": salvar_classificacao
            }

            self.registro.insert_one(insercao)
            return True

        except Exception as e: 
            print(f"Erro ao inserir os dados {e}")
            return None


    def mostrar_registro_id(self, registro_id):
        try:
            obj_id = Objectid(registro_id)
            registro = self.registros.find_one({"_id": obj_id})
            return registro
        except Exception as e:
            print(f"Erro ao buscar dados pelo ID: {e}")
            return None


    def listar_registros(self):
        try:
            return list(self.registros.find().sort("Idade", -1))
        except Exception as e:
            print(f"Erro ao buscar dados dos registros: {e}")
            return None
        
    
    def listar_registros_filtrado(self, categoria_filtro):
        try:
            return list(self.registros.find(categoria_filtro).sort("Idade", -1))
        except Exception as e:
            print(f"Erro ao filtrar os dados {e}")
            return None
    

    def atualizar_registro(self, registro_id, salvar_nome, salvar_idade, salvar_peso, salvar_altura, salvar_flexibiliade, salvar_abdominal, salvar_arremesso, salvar_salto_horizontal, salvar_salto_vertical, salvar_quadrado, salvar_classificacao):
        try: 
            obj_id = Objectid(registro_id)
            filtro = {"_id": obj_id}
            atualizar_dados = {"$set": {"Nome": salvar_nome,
                "Idade": salvar_idade,
                "Peso": salvar_peso,
                "Altura": salvar_altura,
                "Flexibilidade": salvar_flexibiliade,
                "Abdominal": salvar_abdominal,
                "Arremesso": salvar_arremesso,
                "SaltoHor": salvar_salto_horizontal,
                "SaltoVer": salvar_salto_vertical,
                "Quadrado": salvar_quadrado,
                "Classificacao": salvar_classificacao}}
            atualizacao = self.registros.update_one(filtro, atualizar_dados)
            return atualizacao
        except Exception as e:
            print(f"Erro ao atulizar o registro: {e}")
            return None


    def deletar_registro(self, registro_id):
        try:
            obj_id = Objectid(registro_id)
            exclusao = self.registro.delete_one({"_id": obj_id})
            return exclusao
        except Exception as e:
            print(f"Erro ao deletar o registro: {e}")
            return None 



