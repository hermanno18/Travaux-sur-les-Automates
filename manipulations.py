from E_AFND import E_AFND
from AFND import AFND
from logging import currentframe
from AFD import AFD


def reconnaitreMotAFD(dfa, word):

    if dfa.init == []:
        print("\t(ERREUR) : L'autmate entré n'a pas d'Etat initial.")
        return False
    if len(dfa.finals) == 0:
        print("\t(ERREUR) : L'autmate entré n'a pas d'Etat final.")
        return False

    initial = dfa.init[0]
    current_state = initial
    i = 0
    for symbol in word:
        print(" (Etat actuel : '" + current_state + "' \t Symboles à reconnaitre : '" + word[i:] + "')")
        if not dfa.valid_symbol(symbol):
            print("\t(ERREUR) :  le symbole '" + symbol + "' ne fait pas parti de l'alphabet '"+dfa.alphabet+"'.")

        next_state = dfa.dest_state(current_state, symbol)
        if next_state is None:
            print("\t(ERREUR) : il n'y a pas de transition pour le symbole '" + symbol  + "' sur l'etat  '" + current_state + "' .")
            return False

        current_state = next_state
        i = i+1

    if current_state in dfa.finals:
        print("(SUCCES) :le parcourt de l'automate s'est terminé sur l'etat '"+current_state+"' qui est un etat final \n          l'autmate reconnait le mot "+word)
        return True
    print("(FIN) : le parcourt est terminé, et aucun etat final n'est atteint; l'autmate  ne reconnait pas le mot "+word )
    return False

def reconnaitreMotAFND(ndfa, word):
    return reconnaitreMotAFD(ndfa.determine(), word)

def union(afd1, afd2):
    """
    prends en paramettre deux AFD complets et retourne leur union qui est déterministe complet aussi 
    """
    if not afd1.is_complete():
        print("le premier paramettre n'est pas un automate complet ")
        return
    if not afd2.is_complete():
        print("le second paramettre n'est pas un automate complet ")
        return
    #on vérifie qu"il n'ont pas de même nom d'états (sinon ça risque de creer un bug)
    for state in afd1.states:
        if state in afd2.states:
            print("les automates passés en paramettre ont un nom d'etat en commun. ")
            return 
    alphabet = afd1.alphabet
    for sym in afd2.alphabet:
        if sym not in alphabet:
            alphabet.append(sym)
    u = AFD(alphabet)
    if afd2.init[0] in afd2.finals or afd1.init[0] in afd1.finals:
        u.add_state(state=str(afd1.init + afd2.init),final= True, init= True)
    else:
        u.add_state(state=str(afd1.init + afd2.init),final= False, init= True)
    for current_state in u.states:
        for symbol in u.alphabet:
            state = []
            for sub_state in current_state:
                if sub_state in afd1.transitions:
                    for (sym, dest) in afd1.transitions[sub_state]:
                        if(sym == symbol):
                            state.append(dest)
                if sub_state in afd2.transitions:
                    for (sym, dest) in afd2.transitions[sub_state]:
                        if(sym == symbol):
                            state.append(dest)
            if str(state) not in u.states :
                is_final = False
                for added_sub_state in state:
                    if added_sub_state in str(afd1.finals) or added_sub_state in str(afd2.finals):
                        is_final = True
                        break
                if is_final:
                    u.add_state(str(state), True, False)
                else:
                    u.add_state(str(state))
            u.add_transition(str(current_state), symbol, str(state))
    return u        

def intersection(afd1, afd2):
    """
    prends en paramettre deux AFD complets et retourne leur intersection qui est déterministe complet aussi 
    """
    if not afd1.is_complete():
        print("le premier paramettre n'est pas un automate complet ")
        return
    if not afd2.is_complete():
        print("le second paramettre n'est pas un automate complet ")
        return
    #on vérifie qu"il n'ont pas de même nom d'états (sinon ça risque de creer un bug)
    for state in afd1.states:
        if state in afd2.states:
            print("les automates passés en paramettre ont un nom d'etat en commun. ")
            return 
    alphabet = afd1.alphabet
    for sym in afd2.alphabet:
        if sym not in alphabet:
            alphabet.append(sym)
    u = AFD(alphabet)
    if afd2.init[0] in afd2.finals and afd1.init[0] in afd1.finals:
        u.add_state(state=str(afd1.init + afd2.init),final= True, init= True)
    else:
        u.add_state(state=str(afd1.init + afd2.init),final= False, init= True)
    for current_state in u.states:
        for symbol in u.alphabet:
            state = []
            for sub_state in current_state:
                if sub_state in afd1.transitions:
                    for (sym, dest) in afd1.transitions[sub_state]:
                        if(sym == symbol):
                            state.append(dest)
                if sub_state in afd2.transitions:
                    for (sym, dest) in afd2.transitions[sub_state]:
                        if(sym == symbol):
                            state.append(dest)
            if str(state) not in u.states :
                is_final = False
                for added_sub_state in state:
                    if added_sub_state in str(afd1.finals) and added_sub_state in str(afd2.finals):
                        is_final = True
                        break
                if is_final:
                    u.add_state(str(state), True, False)
                else:
                    u.add_state(str(state))
            u.add_transition(str(current_state), symbol, str(state))
    return u        
    
def concatenation(automate1, automate2):
    pass

def thomson(automate):
    thms = E_AFND(automate.alphabet)
    return thms

def glushkov(automate):
    return