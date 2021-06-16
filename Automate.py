import copy #pour la copie


class Automate():
    """ Cette classe représente un Automate FIni Déyterministe"""
    def __init__(self, alphabet):
        """ Initialise the finite automaton.
            @param the alphabet of the automaton."""

        """ List of string corresponding to states name.
            States are always identificated by name."""
        self.states = []
        """ Dictionary using src state as key and mapping it to a list of
            pair (dest_state, symbol)."""
        self.transitions = {}
        """ The string corresponding to the name of the initial state."""
        self.init = []
        """ A list containing the name of the final states."""
        self.finals = []
        """ A string containing all symbols in the alphabet."""
        self.alphabet = ""
        for s in alphabet:
            if s not in self.alphabet:
                self.alphabet += s
    
    def __str__(self):
        ret = "   - alphabet   : '" + self.alphabet + "'\n"
        if self.type=='AFD':
            ret += '   - type : Automate Fini Déterministe\n' 
            ret += "   - état initial       : " + self.init[0] + "\n"
        else:
            ret += '   - type : Automate Fini Non Déterministe\n' 
            ret += "   - états initiaux       : " + str(self.init) + "\n"

        ret += "   - états finaux     : " + str(self.finals) + "\n"
        ret += "   - liste des états (%d) : %s \n" % (len(self.states), str(self.states))
        ret += "   - transitions par états (%d) :\n" % len(self.transitions)
        for state in self.states:
            ret += "       - (%s)" % (state)
            if len(self.transitions[state]) == 0:
                ret += ".\n"
            else:
                ret += ":\n"
                for (sym, dest) in self.transitions[state]:
                    ret +=  "          --(%s)--> (%s)\n" % (sym, dest)
        return ret

    def dest_state(self, src_state, symbol):
        """ recherche la transition correspondante à un source et un symoble."""
        retour = []
        if src_state not in self.states:
            print("erreur : l'etat : '" + src_state + "' n'existe pas dans la  liste d'etats de l'automate.")
            return
        for (s, dest_state) in self.transitions[src_state]:
            if s == symbol:
                if self.type=='AFD':
                    return dest_state
                else:
                    retour.append(dest_state)
        return retour

    def add_state(self, state, final = False, init= False):
        if state in self.states:
            print("(ERREUR) : l'etat'" + state + "' existe deja.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)
        if init:
            if self.type=='AFD':
                if len(self.init) != 0:
                    print("(ERREUR) : l'etat initial a séja été défini, l'AFD ne peut avoir plusieurs etats initiaux")
                    return
            self.init.append(state) # pour definir une fois l'etat initial
        return
 
    def valid_symbol(self, symbol):
        """ verifier si un symbole appartient à un language"""
        if symbol not in self.alphabet: return False
        return True

    def is_complet(self):
        pass

    def clone(self):
        """ Returns a copy of the DFA."""
        a = Automate(self.alphabet)
        a.states = self.states.copy()
        a.init = self.init
        a.finals = self.finals
        a.transitions = copy.deepcopy(self.transitions)
        return a
    