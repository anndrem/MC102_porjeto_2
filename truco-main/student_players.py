### TODO: PREENCHA SUAS INFORMAÇÕES AQUI ###
# Nome #01 (quem entregou o código):    André de Almeida Maximiano 
# RA #01 (quem entregou o código):      306387
# Nome #02:                             [NOME COMPLETO #02]
# RA #02:                               [RA #02]
from basic_players import Player




# TODO: criar classe para tratar a verificacao das cartas e encapsular o codgio
DECISAO = {'encoberta': 0, 'normal': 1, 'truco': 2}
RESPOSTA = {'correr': 0, 'aceitar': 1, 'aumentar': 2}

ORDER_CARDS = ['4' ,'5' ,'6' ,'7' ,'Q' ,'J' ,'K' ,'A' ,'2' ,'3']
ORDER_NIPES = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

class SmartPlayer(Player):
    def __init__(self, ra, name):
        super().__init__(ra, name) 
        self._respond = RESPOSTA['aceitar']
        self._manilha = False
        self.my_manilhas = []

    def _theresIsManilha(self,top_card):
        idx = -1

        idx_c1, idx_n1 = ORDER_CARDS.index(self.cards[0][0]), ORDER_NIPES.index(self.cards[0][1])
        idx_c2, idx_n2 = ORDER_CARDS.index(self.cards[1][0]), ORDER_NIPES.index(self.cards[1][1])
        idx_c3, idx_n3 = ORDER_CARDS.index(self.cards[2][0]), ORDER_NIPES.index(self.cards[2][1])


        for key, value in [[idx_c1, idx_n1], [idx_c2, idx_n2], [idx_c3, idx_n3]]:
            if key == ORDER_CARDS.index(top_card[0]) + 1:
                idx = self.cards.index((ORDER_CARDS[key], ORDER_NIPES[value]))
                self.my_manilhas.append(idx)

        return True if idx != -1 else False
    
    def _sortCards(self):
        if len(self.cards) < 3:
            return None
        
        idx_c1, idx_n1 = ORDER_CARDS.index(self.cards[0][0]), ORDER_NIPES.index(self.cards[0][1])
        idx_c2, idx_n2 = ORDER_CARDS.index(self.cards[1][0]), ORDER_NIPES.index(self.cards[1][1])
        idx_c3, idx_n3 = ORDER_CARDS.index(self.cards[2][0]), ORDER_NIPES.index(self.cards[2][1])

        cards_idx = [[idx_c1, idx_n1], [idx_c2, idx_n2], [idx_c3, idx_n3]]
        cards_idx.sort(key= lambda x: x[0], reverse=True)
        
        sorted_cards = [(ORDER_CARDS[cards_idx[0][0]], ORDER_NIPES[cards_idx[0][1]]), (ORDER_CARDS[cards_idx[1][0]], ORDER_NIPES[cards_idx[1][1]]), (ORDER_CARDS[cards_idx[2][0]], ORDER_NIPES[cards_idx[2][1]])]
        return sorted_cards

    '''O JOGO ESTA DEFINIDO AQUI'''
    def play(self, top_card, play_hist, score_hist):
        if len(self.cards) == 3:
            self.cards = self._sortCards()
            self._manilha = self._theresIsManilha(top_card)

        if len(self.my_manilhas) == 0:
            self._manilha = False
        else: 
            self._manilha = True

        # TODO: arrumar o (index out of range) da manilha - acontece quando temos mais de uma manilha que carrega o index antigo da carta (sugestao: ao inves de usar o index, salvar a propria manilha como carta e depois procurar o index)
        if self._manilha:
            pedir_truco = True if score_hist[-1][-1] == 1 else False
            idx_manilha = self.my_manilhas[-1]
            self.my_manilhas.pop()
            return DECISAO['truco'] if pedir_truco else DECISAO['normal'], self.cards[idx_manilha]
        
        if self._cards:
            return DECISAO['normal'], self.cards[0]
            
        return 1, None

    def respond(self,top_card,play_hist, score_hist):
        current_score = score_hist[-1][-1]
        teams_score = score_hist[-1][-2]
        
        if current_score <= 9 and teams_score[0] <= 10 and teams_score[1] <= 10:
            self._respond = RESPOSTA['aumentar']

        return self._respond

def pair_name():
    return 'Butequeiros de CC' 


def create_pair():
    p1 = SmartPlayer(11, 'Stalin')
    p2 = SmartPlayer(12, 'Lenin')
    return (p1, p2)
