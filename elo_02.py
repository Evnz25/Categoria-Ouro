from elo import Elo

class NomeMaiusculoElo(Elo):
    def processar(self, dados):
        if "Nome" in dados:
            dados["Nome"] = str(dados["Nome"]).upper().strip()
        return super().processar(dados)