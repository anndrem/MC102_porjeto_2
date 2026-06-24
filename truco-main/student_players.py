### TODO: PREENCHA SUAS INFORMAÇÕES AQUI ###
# Nome #01 (quem entregou o código):    André de Almeida Maximiano 
# RA #01 (quem entregou o código):      306387
# Nome #02:                             [NOME COMPLETO #02]
# RA #02:                               [RA #02]
from basic_players import Player

DECISAO = {"encoberta": 0, "normal": 1, "truco": 2}
RESPOSTA = {"correr": 0, "aceitar": 1, "aumentar": 2}
# Jogador que não faz nada. Substitua esta classe para criar as suas, devem herdar da classe Player
class SmartPlayer(Player):
    def __init__(self, ra, name):
        super().__init__(ra, name) # Nome do Jogador

    """O JOGO ESTA DEFINIDO AQUI"""
    # Função para retornar o que você vai jogar em determinada mão
    def play(self, top_card, play_hist, score_hist):
        if self._cards:
            # retorna (jogar carta, primeira carta)
            return DECISAO["normal"], self._cards[0]
        return 1, None

    # Função para retornar o que você vai dar de resposta a trucos
    def respond(self,top_card,play_hist, score_hist):
        return RESPOSTA["correr"]

def pair_name():
    return "Butequeiros de CC" 


def create_pair():
    p1 = SmartPlayer(11, "Stalin")
    p2 = SmartPlayer(12, "Lenin")
    return (p1, p2)
