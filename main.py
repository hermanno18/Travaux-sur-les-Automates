from AFD import AFD
from AFND import AFND
import manipulations as manip

"""
a = AFD("ab")
a.add_state("1", True, False)
a.add_state("0", True, True)
a.add_transition("0", "a", "1")
a.add_transition("0", "b", "0")
a.add_transition("1", "a", "1")
a.add_transition("1", "b", "1")

"""
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
print(a)

mot ="bababbababbbabbbbabbababab"
print("Testons si cet autmate reconnait le mot '"+mot+"'\n")
print("  voici l'automate déterminisé corerspondant à votre automate \n")
print(a.determine())
print("déroulement de la vérification\n")
manip.reconnaitreMotAFD(a.determine(), mot)
# manip.reconnaitreMotAFD(a, mot)


