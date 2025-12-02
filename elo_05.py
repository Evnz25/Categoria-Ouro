from elo import Elo

class RegularDistanciaElo(Elo):
    def processar(self, dados):
        campos_distancia = ["Flexibilidade","Altura", "SaltoHor", "SaltoVer"]

        for campo in campos_distancia:
            if campo in dados:
                valor = dados[campo]
                if valor > 5:
                    dados[campo] = valor / 100.0
        
        return super().processar(dados)