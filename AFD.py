from Automate import Automate


class AFD(Automate):

    def __init__(self, alphabet):
        super().__init__(alphabet)
        self.type = "AFD"
  
    def add_transition(self, src_state, symbol, dest_state):

        if not self.valid_symbol(symbol):
            print("(ERREUR) :  le symbole '" + symbol + "' ne fait pas parti de l'alphabet '"+self.alphabet+"'.")
            return
        if src_state not in self.states:
            print("(ERREUR) : l'etat '" + src_state + "' ne fait pas parti de la liste des etats de l'automate.")
            return
        if dest_state not in self.states:
            print("(ERREUR) : l'etat '" + dest_state + "' ne fait pas parti de la liste des etats de l'automate.")
            return

        if len(self.dest_state(src_state, symbol)) is not 0:
            print("(ERREUR) : la transition (" + src_state + ", " + symbol + ", " + dest_state + " ...) existe deja.")
            return
        self.transitions[src_state].append((symbol, dest_state))
