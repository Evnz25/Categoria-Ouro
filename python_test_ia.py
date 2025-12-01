import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from itertools import permutations
import joblib

# --- CONFIGURAÇÕES ---
ARQUIVO_CSV = "Dados_do_projeto_CAOO.csv"
ARQUIVO_SAIDA = "cerebro_ia.pkl"

PERFIS_ALVO = {
    "BASQUETE": { "Arremesso": 1, "SaltoHor": 1, "SaltoVer": 1, "Altura": 1, "Quadrado": 2 },
    "FUTEBOL":  { "Quadrado": 1, "Abdominal": 1, "SaltoHor": 2, "Arremesso": 2, "Flexibilidade": 3 },
    "CAPOEIRA": { "Flexibilidade": 1, "Quadrado": 3, "Arremesso": 3, "SaltoVer": 3, "Peso": 3 }
}

def limpar_numero(valor):
    if pd.isna(valor) or valor == "": return np.nan
    if isinstance(valor, str):
        valor = valor.replace('"', '').replace(',', '.')
        if valor.strip() == "": return np.nan
    try: return float(valor)
    except: return np.nan

def gerar_ranking_customizado(df_medias):
    ranks = df_medias.copy()
    colunas_maior_melhor = ['Peso', 'Altura', 'Flexibilidade', 'Abdominal', 'Arremesso', 'SaltoHor', 'SaltoVer']
    for col in colunas_maior_melhor:
        if col in df_medias.columns:
            ranks[col] = df_medias[col].rank(ascending=False, method='min').astype(int)
    if 'Quadrado' in df_medias.columns:
        ranks['Quadrado'] = df_medias['Quadrado'].rank(ascending=True, method='min').astype(int)
    return ranks

def identificar_perfis(kmeans, scaler, pesos, colunas_usadas):
    centroides = kmeans.cluster_centers_
    centroides_real = scaler.inverse_transform(centroides / pesos)
    df_medias = pd.DataFrame(centroides_real, columns=colunas_usadas)
    df_rankings = gerar_ranking_customizado(df_medias)
    
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
                    if col in ['Arremesso', 'SaltoHor', 'SaltoVer', 'Flexibilidade']: 
                        peso_erro = 2
                    erro_atual += abs(rank_ideal - rank_real) * peso_erro
        
        if erro_atual < menor_erro:
            menor_erro = erro_atual
            melhor_mapa = {i: nome for i, nome in enumerate(tentativa)}
    return melhor_mapa

def treinar_e_salvar():
    print("--- TREINANDO MODELO (SEM IDADE, SEM IMPUTER) ---")
    
    df = pd.read_csv(ARQUIVO_CSV, sep=',', encoding='latin1')
    df = df.rename(columns={
        'peso': 'Peso', 'estatura': 'Altura', 'flexibilidade': 'Flexibilidade',
        'abdominal': 'Abdominal', 'arremessoMB': 'Arremesso',
        'S. horizontal': 'SaltoHor', 'S.vertical': 'SaltoVer', 'Quadrado 4x4': 'Quadrado'
    })
    
    # Lista EXATA de colunas que seu programa vai usar
    colunas_treino = ['Peso', 'Altura', 'Flexibilidade', 'Abdominal', 'Arremesso', 'SaltoHor', 'SaltoVer', 'Quadrado']
    
    for c in colunas_treino: 
        if c in df.columns: df[c] = df[c].apply(limpar_numero)

    X = df[colunas_treino].copy()
    
    # Remove qualquer linha com dados faltando (treino apenas com dados perfeitos)
    X = X.dropna()
    print(f"Alunos usados no treino: {len(X)}")
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Pesos ajustados para as 8 colunas (removido peso da idade)
    # Ordem: [Peso, Altura, Flex, Abd, Arr, SaltoH, SaltoV, Quad]
    pesos = np.array([0.5, 1.0, 2.0, 1.0, 3.0, 3.0, 3.0, 2.0])
    
    X_pond = X_scaled * pesos
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(X_pond)

    mapa_nomes = identificar_perfis(kmeans, scaler, pesos, colunas_treino)
    print(f"Mapa Identificado: {mapa_nomes}")

    pacote_ia = {
        "kmeans": kmeans,
        "scaler": scaler,
        "pesos": pesos,
        "mapa_nomes": mapa_nomes,
        "colunas": colunas_treino
        # Note: Removi 'imputer' daqui
    }
    
    joblib.dump(pacote_ia, ARQUIVO_SAIDA)
    print(f"Cérebro salvo em: {ARQUIVO_SAIDA}")

if __name__ == "__main__":
    treinar_e_salvar()