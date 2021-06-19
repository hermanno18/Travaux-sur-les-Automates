from graphviz import Digraph
import Automate
import uuid # pour generer les valeurs au hasard
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
            return False
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)
        if init:
            if self.type=='AFD':
                if len(self.init) != 0:
                    print("(ERREUR) : l'etat initial a séja été défini, l'AFD ne peut avoir plusieurs etats initiaux")
                    return False
            self.init.append(state) # pour definir une fois l'etat initial
        return True
 
    def valid_symbol(self, symbol):
        """ verifier si un symbole appartient à un language"""
        if symbol not in self.alphabet: return False
        return True

    def is_complete(self) :
        for state in self.states:    
            sym_for_state = []
            for symbol in self.alphabet:
                for (sym, dest) in self.transitions[state]:
                    sym_for_state.append(sym)
                if symbol  not in sym_for_state:
                        return False
        return True

    def complete(self) :
        if self.is_complete():
            return True
        state_puit = "Puit"
        self_clone = self.clone()
        self_clone.add_state(state_puit)
        for state in self_clone.states: 
            sym_for_state = []
            for symbol in self_clone.alphabet:
                for (sym, dest) in self_clone.transitions[state]:
                    sym_for_state.append(sym)
                if symbol  not in sym_for_state:
                    self_clone.add_transition(state, symbol, state_puit)
                    self_clone.add_transition(state_puit, symbol, state_puit)
            
        return self_clone

    def display(self):
        visualisationAutomate=Digraph(format="pdf")

        for etat  in self.states:
            if etat in self.init:
                visualisationAutomate.node(str(etat),label=str(etat),color='green')
            if etat in self.finals:
                visualisationAutomate.node(str(etat),label=str(etat),shape='doublecircle')
            else:
                visualisationAutomate.node(str(etat),label=str(etat))

        for source in self.transitions:
            for (sym, dest) in self.transitions[source]:
                visualisationAutomate.edge(str(source),str(dest),label=sym)

        visualisationAutomate.render(filename="Output/"+self.type+"/Automate '"+self.type+"'_Alphabet '"+self.alphabet+"'"+str(uuid.uuid1()), view=True)    

    def has_state(self, state):
        if state in self.states:
            return True
        return False
