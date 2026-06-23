### TODO: PREENCHA SUAS INFORMAÇÕES AQUI ###
# Nome #01 (quem entregou o código):    [NOME COMPLETO #01] 
# RA #01 (quem entregou o código):      [RA #01]
# Nome #02:                             Vinicius Brasil Turibio da Silva
# RA #02:                               306565
from basic_players import Player

# Implemente neste arquivo seus jogadores para Truco

# Jogador que não faz nada. Substitua esta classe para criar as suas, devem herdar da classe Player
class NonePlayer(Player):
    # Se estiver dúvida sobre como começar olhe os players prontos em basic_players.py e o ReadMe
    def __init__(self, ra, name):
        super().__init__(ra, name) # Nome do Jogador

    # Função para retornar o que você vai jogar em determinada mão
    def play(self, top_card, play_hist, score_hist):
        if self._cards:
            return 1, self._cards[0]
        return 1, None

    # Função para retornar o que você vai dar de resposta a trucos
    def respond(self,top_card,play_hist, score_hist):
        return 0


# Função que define o nome da dupla:
def pair_name():
    return "Butequeiros de CC"  # Defina aqui o nome da sua dupla


# Função que cria a dupla:
def create_pair():
    p1 = NonePlayer(11, "Stalin")
    p2 = NonePlayer(12, "Lenin")
    return (p1,p2)  # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.
