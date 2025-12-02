import pymongo
from bson.objectid import ObjectId
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
import os
from itertools import permutations

from elo_01 import VerificarPreenchimentoElo
from elo_02 import NomeMaiusculoElo
from elo_03 import SubstituirVirgulaElo
from elo_04 import TransformaFloatElo
from elo_05 import RegularDistanciaElo

PERFIS_ALVO = {
    "BASQUETE": { "Arremesso": 1, "SaltoHor": 1, "SaltoVer": 1, "Altura": 1, "Quadrado": 2 },
    "FUTEBOL":  { "Quadrado": 1, "Abdominal": 1, "SaltoHor": 2, "Arremesso": 2, "Flexibilidade": 3 },
    "CAPOEIRA": { "Flexibilidade": 1, "Quadrado": 3, "Arremesso": 3, "SaltoVer": 3, "Peso": 3 }
}

class Model():
    def __init__(self):
        self.meucliente = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.meucliente["ClassificacaoOuro"]
        self.registros = self.db["registros"]

        self.e0 = VerificarPreenchimentoElo(self) #valida vazio
        self.e1 = NomeMaiusculoElo(self) #Nome maiusculo
        self.e2 = SubstituirVirgulaElo(self) #Virgula para ponto  
        self.e3 = TransformaFloatElo(self) #texto -> float
        self.e4 = RegularDistanciaElo(self) #ajuste de escala

        self.e0.set_next(self.e1)
        self.e1.set_next(self.e2)
        self.e2.set_next(self.e3)
        self.e3.set_next(self.e4)

        self.carregar_ia_do_disco()

    def carregar_ia_do_disco(self):
        self.ia_carregada = False
        if os.path.exists("cerebro_ia.pkl"):
            try:
                pacote = joblib.load("cerebro_ia.pkl")
                self.kmeans = pacote["kmeans"]
                self.scaler = pacote["scaler"]
                self.pesos = pacote["pesos"]
                self.mapa_nomes = pacote["mapa_nomes"]
                self.ia_carregada = True
                print("IA Carregada com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar IA: {e}")
        else:
            print("AVISO: Arquivo .pkl não encontrado.")


    def processar_dados(self, dados):
        try:
            dados_limpos = self.e0.processar(dados)
            return dados_limpos
        except Exception as e:
            return {"erro": str(e)}


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
            exclusao = self.registros.delete_one({"_id": obj_id})
            return exclusao
        except Exception as e:
            print(f"Erro ao deletar o registro: {e}")
            return None 
        
        
    def retreinar_ia(self):
        try:
            cursor = self.registros.find({}, {
                "Peso": 1, "Altura": 1, "Flexibilidade": 1, "Abdominal": 1, 
                "Arremesso": 1, "SaltoHor": 1, "SaltoVer": 1, "Quadrado": 1, "_id": 0
            })
            dados_db = list(cursor)

            if len(dados_db) < 3:
                return "Erro: Precisa de pelo menos 3 registros no banco para calibrar."

            colunas_treino = ['Peso', 'Altura', 'Flexibilidade', 'Abdominal', 'Arremesso', 'SaltoHor', 'SaltoVer', 'Quadrado']
            df = pd.DataFrame(dados_db)
            
            df = df[colunas_treino].apply(pd.to_numeric, errors='coerce').dropna()

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(df)

            pesos = np.array([0.5, 1.0, 2.0, 1.0, 3.0, 3.0, 3.0, 2.0])
            X_pond = X_scaled * pesos

            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            kmeans.fit(X_pond)

            mapa_nomes = self._identificar_perfis_logica(kmeans, scaler, pesos, colunas_treino)

            pacote_ia = {
                "kmeans": kmeans,
                "scaler": scaler,
                "pesos": pesos,
                "mapa_nomes": mapa_nomes,
                "colunas": colunas_treino
            }
            joblib.dump(pacote_ia, "cerebro_ia.pkl")
            
            self.carregar_ia_do_disco()
            
        except Exception as e:
            return f"Erro no retreino: {e}"
        
    def _gerar_ranking(self, df_medias):
        ranks = df_medias.copy()
        for col in df_medias.columns:
            asc = (col == 'Quadrado')
            ranks[col] = df_medias[col].rank(ascending=asc, method='min').astype(int)
        return ranks
    
    def _identificar_perfis_logica(self, kmeans, scaler, pesos, colunas):
        centroides = kmeans.cluster_centers_
        centroides_real = scaler.inverse_transform(centroides / pesos)
        df_medias = pd.DataFrame(centroides_real, columns=colunas)
        df_rankings = self._gerar_ranking(df_medias)
        
        nomes = list(PERFIS_ALVO.keys())
        melhor_mapa = None
        menor_erro = float('inf')

        for tentativa in permutations(nomes):
            erro_atual = 0
            for id_grupo, nome_esporte in enumerate(tentativa):
                perfil_desejado = PERFIS_ALVO[nome_esporte]
                for col, rank_ideal in perfil_desejado.items():
                    if col in df_rankings.columns:
                        rank_real = df_rankings.iloc[id_grupo][col]
                        peso_erro = 1
                        if col in ['Arremesso', 'SaltoHor', 'SaltoVer', 'Flexibilidade']: peso_erro = 2
                        erro_atual += abs(rank_ideal - rank_real) * peso_erro
            
            if erro_atual < menor_erro:
                menor_erro = erro_atual
                melhor_mapa = {i: nome for i, nome in enumerate(tentativa)}
        return melhor_mapa


    def calcular_classificacao_ia(self, dados_novos_lista):
        if not self.ia_carregada:
            return "Erro: IA não treinada"

        try:
            colunas = ['Peso', 'Altura', 'Flexibilidade', 'Abdominal', 'Arremesso', 'SaltoHor', 'SaltoVer', 'Quadrado']
            dados_df = pd.DataFrame([dados_novos_lista], columns=colunas)

            dados_scaled = self.scaler.transform(dados_df)

            dados_pond = dados_scaled * self.pesos

            cluster_id = self.kmeans.predict(dados_pond)[0]

            return self.mapa_nomes[cluster_id]

        except Exception as e:
            print(f"Erro na predição: {e}")
            return "Erro no Cálculo"

