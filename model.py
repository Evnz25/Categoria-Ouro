import pymongo
from bson.objectid import ObjectId
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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

            self.registros.insert_one(insercao)
            return True

        except Exception as e: 
            print(f"Erro ao inserir os dados {e}")
            return None


    def mostrar_registro_id(self, registro_id):
        try:
            obj_id = ObjectId(registro_id)
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
            obj_id = ObjectId(registro_id)
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
            obj_id = ObjectId(registro_id)
            exclusao = self.registro.delete_one({"_id": obj_id})
            return exclusao
        except Exception as e:
            print(f"Erro ao deletar o registro: {e}")
            return None 
        
        
    def calcular_classificacao_ia(self, dados_novos_lista):
        try:
            cursor = self.registros.find({}, {"_id": 0, "Nome": 0, "Classificacao": 0})
            dados_treino = list(cursor)
            
            if len(dados_treino) < 3:
                return "Dados insuficientes (Mínimo 3 alunos cadastrados)"

            colunas = ["Idade", "Peso", "Altura", "Flexibilidade", "Abdominal", "Arremesso", "SaltoHor", "SaltoVer", "Quadrado"]
            df = pd.DataFrame(dados_treino)[colunas]

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(df)

            # 4. Aplicar PESOS (Sua customização!)
            # [Idade, Peso, Altura, Flex, Abd, Arr, SaltoH, SaltoV, Quad]
            pesos = [1.0, 1.0, 3.0, 1.0, 0.5, 1.0, 1.5, 1.5, 1.0]
            X_scaled = X_scaled * pesos

            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            kmeans.fit(X_scaled)

            centroides = kmeans.cluster_centers_
            indice_altura = 2 
            
            centroides_real = scaler.inverse_transform(centroides / pesos) 
            
            grupos = []
            for i in range(3):
                grupos.append((i, centroides_real[i][indice_altura]))
            
            grupos.sort(key=lambda x: x[1])
            
            mapa_nomes = {
                grupos[0][0]: "CAPOEIRA",  
                grupos[1][0]: "FUTEBOL",   
                grupos[2][0]: "BASQUETE"   
            }

            dados_novos_scaled = scaler.transform([dados_novos_lista])
            dados_novos_scaled = dados_novos_scaled * pesos 
            
            cluster_predito = kmeans.predict(dados_novos_scaled)[0]
            
            return mapa_nomes[cluster_predito]

        except Exception as e:
            print(f"Erro IA: {e}")
            return "Erro no Cálculo"



