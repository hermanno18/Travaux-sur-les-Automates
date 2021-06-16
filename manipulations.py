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
    pass


