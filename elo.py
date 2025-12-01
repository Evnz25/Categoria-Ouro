from abc import ABC, abstractmethod

class Elo:
    def __init__(self, model):
        self.next = None
    
    def set_next(self, next):
        self.next = next

    @abstractmethod
    def processar(self, dados):
        if self.next:
            return self.next.processar(dados)
        return dados