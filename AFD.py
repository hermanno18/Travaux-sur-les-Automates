from Automate import Automate
import copy #pour la copie


class AFD(Automate):

    def __init__(self, alphabet):
        super().__init__(alphabet)
        self.type = "AFD"
  
    def add_transition(self, src_state, symbol, dest_state):

        if not self.valid_symbol(symbol):
            print("(ERREUR) :  le symbole '" + symbol + "' ne fait pas parti de l'alphabet '"+self.alphabet+"'.")
            return False
        if src_state not in self.states:
            print("(ERREUR) : l'etat '" + src_state + "' ne fait pas parti de la liste des etats de l'automate.")
            return False
        if dest_state not in self.states:
            print("(ERREUR) : l'etat '" + dest_state + "' ne fait pas parti de la liste des etats de l'automate.")
            return False
        if len(self.dest_state(src_state, symbol)) != 0:
            print("(ERREUR) : la transition (" + src_state + ", " + symbol + ", " + dest_state + " ...) existe deja.")
            return False
        self.transitions[src_state].append((symbol, dest_state))
        return True

    def get_complementry(self):
        if self.is_complete():
            complnt = AFD(self.alphabet)
            complnt.init = self.init
            complnt.states = self.states
            complnt.transitions = copy.deepcopy(self.transitions)
            for state in self.states:
                if(state  not in self.finals and state not in complnt.init):
                    complnt.finals.append(state)
            return complnt
        return 
   
    def clone(self):
        """ Returns a copy of the DFA."""
        a = AFD(self.alphabet)
        a.states = self.states.copy()
        a.init = self.init
        a.finals = self.finals
        a.transitions = copy.deepcopy(self.transitions)
        return a
   