import json
import os

DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")

def ouvrir_inventaire(path=INVENTAIRE_PATH):
    os.makedirs(DATA_DIR, exist_ok = True)
    if not os.path.exists(path):
        inventaire_defaut = {
            "bananes" : 120,
            "mangues" : 85,
            "ananas" : 45,
            "nois de coco" : 60,
            "papayes" : 30
        }
        with open(path, 'w', encoding ='utf-8') as fichier:
            json.dump(inventaire_defaut, fichier, ensure_ascii=False, indent = 4)
    with open(path, 'r', encoding = 'utf-8') as fichier:
        inventaire = json.load(fichier)
    return inventaire

def ouvrir_tresorerie(path=TRESORERIE_PATH):
    os.makedirs(DATA_DIR, exist_ok = True)
    try:
        with open(path, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
    except FileNotFoundError:
        contenu = ""

    if contenu.strip():
        return json.loads(contenu)

    tresorerie = 1000.0
    ecrire_tresorerie(tresorerie, path)
    return tresorerie
    

def ouvrir_prix(path=PRIX_PATH):
    os.makedirs(DATA_DIR, exist_ok = True)
    if not os.path.exists(path):
        prix_defaut = {
            "bananes" : 2,
            "mangues" : 7,
            "ananas" : 5,
            "nois de coco" : 4,
            "papayes" : 3
        }
        with open(path, 'w', encoding ='utf-8') as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent = 4)
    with open(path, 'r', encoding = 'utf-8') as fichier:
        prix = json.load(fichier)
    return prix

def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, 'w', encoding = 'utf-8') as fichier:
        json.dump(inventaire, fichier, ensure_ascii = False, indent = 4)

def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, 'w', encoding = 'utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii = False, indent = 4)
        
def afficher_tresorerie(tresorerie):
    print(f"\n Trésorerie actuelle : {tresorerie:.2f} $")

def afficher_inventaire(inventaire):
    print("Inventaire actuel de la plantation :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")
        

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit,0) + quantite
    print(f"Récolté {quantite} {fruit} supplémentaires")
    
    
def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0)*quantite
        print(f"Vendu {quantite} {fruit} !")
    else:
        print(f"\n Pas assez de {fruit} pour vendre {quantite} unités")
    return inventaire, tresorerie
    
if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie, prix)
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)
