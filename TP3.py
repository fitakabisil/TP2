import time
import random
# la variable est déja défini comme true (y) audébut du code.
refaire = 'y'

refaire_c = 1

# si la variable refaire est true (y), le jeu va commencer.
while refaire == 'y':

    # la variable est défini par 1 pour ne pas avoir de message 'tu a réussi avec 0 essais!'.
    nombre_essai = 1

    prenom = input('Quel est ton prénom?')

    print('bonjour', prenom, 'veux-tu jouer à un petit jeu? Bien sûr que oui!')

    time.sleep(1)

    born_minimal = input('Quel est la born minimal?')

    born_maximal = input('Quel est la born maximal?')

    print('je vais choisir un nombre entre', born_minimal, 'et', born_maximal)

    # un nombre aléatoire va ête choisie entre les deux limites (les bornes sont transformer en integer).
    value = random.randint(int(born_minimal), int(born_maximal))

    # dans cette boucle, l'utilisateur doit trouver le nombre aléatoire.
    while refaire_c == 1:

        if refaire_c == 1:

            # la variable d,essai est transformer en integer.
            essai = int(input('quel est ton essai?'))

            # cette boucle va être activer si le la variable essai est égale au nombre mistère.
            if value == essai:

                print("bravo, tu as réussi avec", nombre_essai, "essais!")

                refaire = input("veux-tu réessayer? y ou n?")

                # ce code va transformé la valeur de la varable en false (n) et met fin au jeu.
                if refaire == 'n':

                    print('meci de jouer.')

                    break

                else:

                    # essentiellement, ce code va recommencer le jeu.
                    refaire_c = 0
                    continue

            #  cette boucle va augmenter la valeur du nombre d'éssai
            # elle va aussi indiquer si l'essai est plus grand au plus petit que value
            else:
                if essai > value:

                    print('ton essai est plus grand que le nombre mistère, essai encore.')

                    nombre_essai = nombre_essai + 1

                else:

                    print('ton essai est plus petit que le nombre mistère, essai encore.')

                    nombre_essai = nombre_essai + 1

        else:
            continue
