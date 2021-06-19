from AFD import AFD
from Automate import Automate
import copy #pour la copie


class AFND(Automate):
    
    def __init__(self, alphabet):
        super().__init__(alphabet)
        self.type = 'AFND'
    
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
        if dest_state in  self.dest_state(src_state, symbol):
            print("(ERREUR) : la trasition (" + src_state + ", " + symbol + ", " + dest_state + " ...) existe deja.")
            return False
        self.transitions[src_state].append((symbol, dest_state))
        return True
    
    def determine(self):
        afd = AFD(self.alphabet)
        afd.add_state(state=str(self.init), final=False, init=True)
        for current_state in afd.states:
            for symbol in self.alphabet:
                state = []
                for sub_state in current_state:
                    print(sub_state)
                    if sub_state in self.transitions:
                        for (sym, dest) in self.transitions[sub_state]:
                            if(sym == symbol):
                                state.append(dest)
                if str(state) not in afd.states:
                    is_final = False
                    for final_state in self.finals:
                        if final_state in state:
                            is_final = True
                            break
                    if is_final :
                        afd.add_state(str(state), True, False)
                    else:     
                        afd.add_state(str(state))
                
                afd.add_transition(str(current_state), symbol, str(state))

        
        return afd

    def clone(self):
        """ Returns a copy of the DFA."""
        a = AFND(self.alphabet)
        a.states = self.states.copy()
        a.init = self.init
        a.finals = self.finals
        a.transitions = copy.deepcopy(self.transitions)
        return a
   