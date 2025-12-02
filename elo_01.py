from elo import Elo

class VerificarPreenchimentoElo(Elo):
    def processar(self, dados):
        for chave, valor in dados.items():
            if valor == "" or valor is None:
                raise ValueError(f"O campo '{chave}' não pode estar vazio.")
        return super().processar(dados)