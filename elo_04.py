from elo import Elo

class Elo04(Elo):
    def processar(self, dados):
        campos_numericos = [
            "Idade", "Peso", "Altura", "Flexibilidade", "Abdominal", 
            "Arremesso", "SaltoHor", "SaltoVer", "Quadrado"
        ]
        try:
            for campo in campos_numericos:
                if campo in dados:
                    dados[campo] = float(dados[campo])
            return super().processar(dados)
        except ValueError:
            raise ValueError("Existem campos numéricos contendo letras ou símbolos inválidos.")