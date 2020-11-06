import pandas as pd
import random
from collections import Counter

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

def premier_tirage(deck):
    
    tirage = []
    for i in range(5):
        tirage.append(deck.pop(random.randint(0, len(deck) - 1)))
    return tirage

def choix_carte(tirage):

    #     Affichage des instructions et du tirage à l'utilisateur
    print("Choisissez les cartes que vous voulez garder (Entrer le numéro correspondant à la carte que vous voulez garder)")
    print("0: Ca sera tout merci !")
    for i, carte in enumerate(tirage):
        print(str(i+1) + ": " + carte)

    #     Enregistrement des cartes choisi dans un nouveau tableau
    carteChoisi = []
    for carte in tirage:
        choix = input()
        if (choix != 0):
            carteChoisi.append(tirage[choix-1])
        else:
            break

    #     Affichage du récapitulatif des cartes choisi
    print("Vos choix sont :")
    for carte in carteChoisi:
        print(carte)
    
    return carteChoisi

def deuxieme_tirage(carteChoisi):
    for i in range(5 - len(carteChoisi)):
        carteChoisi.append(deck.pop(random.randint(0, len(deck) - 1)))
    
    return carteChoisi

def machine(deck):
    tirage = premier_tirage(deck)
    print(tirage)
    carteChoisi = choix_carte(tirage)
    jeu = deuxieme_tirage(carteChoisi)
    print(jeu)
    return jeu

def decompose_jeu(tirage):
    dic = {}
    keys = [1,2,3,4,5]
    valeur = []
    couleur = []
    for i,k in zip(tirage,keys):
        dic[k] = i.split('-')
    for key in dic.keys():
        valeur.append(dic[key][0]) 
        couleur.append(dic[key][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip(liste, range(0, 5)):
        try:
            liste[i] = int(e)
        except:
            if e == "J":
                liste[i] = 11
            elif e == "Q":
                liste[i] = 12
            elif e == "K":
                liste[i] = 13
            elif e == "A":
                liste[i] = 14
            else:
                continue
    return liste

def isPair(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 2:
            return True
    return False


def isTwoPair(valeur):
    cpt = 0
    counter = Counter(valeur)
    for i in counter.values():
        if i == 2:
            cpt += 1
    
    if cpt == 2:
        return True
    else:
        return False


def isBrelan(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 3:
            return True
    return False


def isQuinte(valeur):
    liste = sorted(valeur)
    if int(liste[0]) + 4 == int(liste[4]):
        return True
    else:
        return False

def isFlush(couleur):
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False


def isFull(valeur):
    if (isPair(valeur) and isBrelan(valeur)):
        return True
    else:
        return False
    

def isCarre(valeur):
    counter = Counter(valeur)
    for i in counter.values():
        if i == 4:
            return True
    return False


def isQuinteFull(valeur, couleur):
    if isQuinte(valeur) and isFlush(couleur):
        return True
    else:
        return False


def isQuinteFlushRoyale(valeur, couleur):
    if isQuinteFull(valeur, couleur) and valeur == [10, 11, 12, 13, 14]:
        return True
    else:
        return False

def gains(mise, jeu):
    valeur, couleur = decompose_jeu(jeu)
    
    valeur = convert_carte(valeur)
    
    if isQuinteFlushRoyale(valeur, couleur):
        gain = mise * 250
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isQuinteFull(valeur, couleur):
        gain = mise * 50
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isCarre(valeur):
        gain = mise * 25
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isFull(valeur):
        gain = mise * 9
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isFlush(couleur):
        gain = mise * 6
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isQuinte(valeur):
        gain = mise * 4
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isBrelan(valeur):
        gain = mise * 3
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isTwoPair(valeur):
        gain = mise * 2
        print("Vous avez gangnez " + str(gain))
        return gain
    elif isPair(valeur):
        print("Vous récupérez votre mise")
        return mise
    else:
        print("Vous avez perdu")
        return 0

def partie(mise, bankroll):
    if bankroll >= mise:
        bankroll -= mise
        jeu = machine(deck)
        total = gains(mise, jeu)
        bankroll += total
        return bankroll
    else:
        print("Mise trop élevé")
        return

def video_poker():
    print("Insérer de l'argent :")
    bankroll = int(input())
    while bankroll > 0:
        print("Combien voulez vous miser :")
        mise = int(input())
        bankroll = partie(mise, bankroll)
        print(str(bankroll))
    print("Vous n'avez plus d'argent")
video_poker()