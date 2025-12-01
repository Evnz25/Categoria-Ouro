from elo import Elo

class Elo03(Elo):
    def processar(self, dados):
        campos_numericos = [
            "Idade", "Peso", "Altura", "Flexibilidade", "Abdominal", 
            "Arremesso", "SaltoHor", "SaltoVer", "Quadrado"
        ]
        for campo in campos_numericos:
            if campo in dados:
                dados[campo] = str(dados[campo]).replace(",", ".")
        return super().processar(dados)