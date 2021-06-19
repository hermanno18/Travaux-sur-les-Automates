from graphviz import dot
from E_AFND import E_AFND
from AFD import AFD
from AFND import AFND
import manipulations as manip




def enregisterAutomate():
    print("\tLe type de votre automate : \n \t\t 1) AUtomate fini déterministe \n \t\t 2) AUtomate Fini Non Déterministe (AFND) \n \t\t 3) AUtomate Fini Non Déterministe  à Epsilon transition (E_AFND) ")
    a_type = int(input(""))
    while (a_type !=1) and (a_type !=2) and (a_type !=3) : 
        a_type = int(input("Choix incorrect, veuillez reéssayer :     "))
    alphabet = str(input("Entrez les élements votre Alphabet...... (exemple: abcde) :     ")).lower()
    while alphabet == "":
        alphabet = str(input("Erreur votre alphabet ne peut etre vide...... (exemple: abcde):     "))    
    if a_type==1:
        automaton = AFD(alphabet)
    elif a_type ==2 :
        automaton = AFND(alphabet)
    else:
        automaton = E_AFND(alphabet)
    print("\nA - enregistrez vos etats (pour des souscis de lisibilité entrez des valeurs différentes de celles reservées pour votre alphabet")
    entry = int(input("Quel est le nombre d'etats de votre automate ?...     "))
    compteur = 1
    while compteur <= entry:
        name = input('Entrez un etat...     ')
        final = None
        while final != "o" and final != "n":
            final = input("L'etat '"+name+"' est il un etat final ?  (O/N) :     ").lower()
        if(final == "o"): final = True
        else: final = False
        init = None
        while init != "o" and init != "n":
            init = input("L'etat '"+name+"' est il un etat initial ? (O/N) :     ").lower()
        if(init == "o"): init = True
        else: init = False
        if automaton.add_state(name, final, init) :
            compteur+=1
    print("\nB - enregistrez les transistions de votre automate : ")
    entry = int(input("Quel est le nombre de transistions  de votre automate ?...     "))
    compteur = 1
    while compteur <= entry:
        if compteur == 1:
            print ('\t {}-iere transition...'.format(compteur))
        else:
            print ('\t {}-ieme transtion...'.format(compteur))
        src_state =  input("\nEntrez  l'etat source (l'etat de départ)...     ")
        while not automaton.has_state(src_state):
            src_state = input("L'etat '"+src_state+"' n'est pas dans la liste des etats de l'automate, veuillez  entrer de nouveau   ").lower()

        symbol =  input("\nle symbole de la transytion...     ")
        while symbol not in automaton.alphabet:
            symbol = input("Le symbole '"+symbol+"' n'est pas dans l'alphabet de l'automate, veuillez  entrer de nouveau   ").lower()

        dest_state =  input("\nEntrez  l'etat destination...     ")
        while not automaton.has_state(dest_state):
            dest_state = input("L'etat '"+dest_state+"' n'est pas dans la liste des etats de l'automate, veuillez  entrer de nouveau   ").lower()
        
        if automaton.add_transition(src_state,symbol, dest_state):
            compteur+=1

    return automaton
    print("l'aphabet :")

def askBeforeDisplay(automaton):
    choix = input('**Automate enregistré, voulez vous y jetter un oeil en interface (desinné dans un graphe), en plus de la représentation dans le terminale? [O/N]...     ' ).lower()
    while choix not in ["o","n"]:
        choix = input('choix non repertorié, veuillez recommencer......').lower()
    print(automaton)
    if choix in 'o':
        automaton.display()

def operations(automaton):
    print("OPERATIONS :\n\t 1) modifier l'automate\n\t2)reconnaitre un mot \n\t3)déterminiser \n\t4) trouver le complémentaire\n\t5)faire l'union (avec un autre automate)\n\t6)faire l'intersection (avec un autre automate) \n\t7)faire la concaténation (avec un autre automate) \n\t8)Thomson \n\t9)glushkov   ")
    choix = input("quels opérations voulez vous effectuer sur votre automate?...      ").lower()

def menu_principal(a = None):
    print(" \t\t ***********Bienvenue sur notre programme de manipuylation des automates*********** ")
    print("NOTES : \n\t -> vous pouvez arretez une action et revenir à ce menu à partir de n'importe-quelle entrée, en saisissant le charactere '$' \n\t ->  le mot vide est '&' il s'agit de notre facon de représenter le caractere epsilon ")
    print("\n")
    print("\nOPERATIONS DE BASES (elles sont indispensables pour les autres) :\n\t 1)Enregistrer un automate.\n\t 2) Utiliser les valeurs par défaut . \n\t 3)Utiliser l'automate que vous avez précedement enregistré.")
    choix = int(input(""))
    while choix not in [1,2,3]:
        choix = int(input('choix non repertorié, veuillez recommencer......'))
    if(choix == 2):
        choix = int(input('utiliser un : \n\t 1) AFD \n\t 1) AFND \n\t 1) E-AFND\n'))
        while(choix not in [1,2,3]):
            choix = int(input('choix non repertorié, veuillez recommencer......'))
        if choix == 1:
            a = AFD("ab")
            a.add_state("1", True, False)
            a.add_state("0", True, True)
            a.add_transition("0", "a", "1")
            a.add_transition("0", "b", "0")
            a.add_transition("1", "b", "1")
            automaton = a.clone()
        elif(choix == 2):
            a = AFND("ab")
            a.add_state("1", False, True)
            a.add_state("2", False, False)
            a.add_state("3", True, False)
            a.add_state("4", False, True)
            a.add_state("5", False, True)
            a.add_state("6", True, False)
            a.add_transition("1", "a", "1")
            a.add_transition("1", "a", "2")
            a.add_transition("1", "b", "1")
            a.add_transition("2", "b", "3")
            a.add_transition("4", "b", "5")
            a.add_transition("5", "a", "6")
            a.add_transition("6", "a", "6")
            a.add_transition("6", "b", "6")
            automaton = a.clone()
        else:
            a = E_AFND('ab')
            automaton = a.clone()
    elif(choix == 1):
        automaton = enregisterAutomate()
    else:
        automaton = a

    askBeforeDisplay(automaton) # on demande si il veut l'affichage graphique
    operations(automaton)  # on affiche le menu des opérations possible 


menu_principal()



















#il faut :
# - demander avec quels type d'automate il veut travailler : 
#   - deterministe ?
#   - non déterministe ?
# - demander le nombre d'etas et les récuperer
# - demander le nombre de transitions et les récuperer
# - demander l'etat intial et le configurer
# - demander les etat finax et les configuerer
# - afficher l'autmate 
# - demander ce qu'il veut faire de son automate :
#   - déterminiser ? (ssi l'automate n'est pas déterministe)
#   - reconnaitre un mot ? 
#   - etc...

"""
a=AFD("ab")
b=AFD("ab")
a.add_state('0', True, True)
a.add_state('1')
a.add_transition('0', "b", "0")
a.add_transition('0', "a", "1")
a.add_transition('1', "a", "0")
a.add_transition('1', "b", "1")

b.add_state('2', True, True)
b.add_state('3')
b.add_transition('2', "a", "2")
b.add_transition('2', "b", "3")
b.add_transition('3', "b", "2")
b.add_transition('3', "a", "3")
"""
#manip.intersection(a,b).display()
"""
a.complete().get_complementry().display()
print(a.is_complete()) 
print(a.complete().is_complete())
a.display() # affiche l'automate en image
a.determine().display()
mot ="bababbababbbabbbbabbababab"
print("Testons si cet autmate reconnait le mot '"+mot+"'\n")
print("  voici l'automate déterminisé corerspondant à votre automate \n")
print(a.determine())
print("déroulement de la vérification\n")
manip.reconnaitreMotAFD(a.determine(), mot)
# manip.reconnaitreMotAFD(a, mot)
"""

