from graph1 import *
from files import *

#Exercice 1
#La complexité du parcours en largeur est en O(n+m) où n est le nombre de sommets
#et m le nombre d'arcs
def largeur(graph,v0): 
    Visited = [] #liste dans laquelle on va mettre les sommets dans l'ordre du parcours en largeur
    File = enqueue(v0,emptyQueue()) #j'oblige mon parcours à commencer par v0
    while len(Visited) < nbVertices(graph): #tant que je n'ai pas visité tous les noeuds
        if isEmpty(File): 
            for v in vertices(graph): 
                if v not in Visited:  
                    File = enqueue(File, v)
                    break                  #je mets dans ma file le premier sommet non visité s'il existe
        while not isEmpty(File):      #cette boucle parcours en largeur un sous-graphe de G dont les noeuds sont accessibles depuis l'origine du parcours
            current = first(File)
            File = dequeue(File)
            Visited = Visited + [current]
                
            for v in successors(graph,current):
                if v not in Visited:
                    File = enqueue(File, v)
 
    return Visited


#La complexité du parcours en largeur est en O(n+m) où n est le nombre de sommets
#et m le nombre d'arcs
def prof_aux(G, v, Visited): #Cette fonction exécute un parcours en profondeur à partir de v
    Visited = Visited + [v]
    
    for s in successors(G,v):
        if s not in Visited:
            Visited = prof_aux(G, s, Visited)
        
    return Visited

def prof(G, v):
    Visited = prof_aux(G, v, [])

    #je relance le parcours à partir de noeuds qui n'ont pas été visités
    for s in vertices(G):
        if s not in Visited:
            Visited = prof_aux(G, s, Visited)
        
    return Visited



#Exercice 2
#Q1
#Prenons G un graphe avec un puits p.
#Aucun arc ne part de p pour aller dans un autre noeud.
#Pour qu'il y ait un autre puits p2, il faudrait que tous les noeuds
#autre que p2 pointent vers lui. Or il existe au moins un p qui ne pointe pas
#vers p2: il s'agit de p qui est un puits.
#Donc un puits est unique.

#Q2
def puits(G):
    """Retourne le puit de G s'il existe"""
    E = {} #E va contenir les degrés entrant pour chaque sommet
    S = {} #S va contenir les degrés sortant pour chaque sommet
    
    for arc in edges(G):  #on parcourt tous les arcs de G
        if arc[0] in S:
            S[arc[0]] = S[arc[0]] + 1
        else:
            S[arc[0]] = 1

        if arc[1] in E:
            E[arc[1]] = E[arc[1]] + 1
        else:
            E[arc[1]] = 1

    for n in E:
        if E[n] == nbVertices(G)-1 and n not in S:
            return n
    return None

def puits(G):
    """Retourne le puit de G s'il existe"""
    #sans compter les degrés
    for s in vertices(g):
        if len(predecessors(g, s))==nbVertices(g) and len(successors(g, s))==0:
            return s
    return None

#Exercice 3
#Supposons que les individus v1...vn soient donnés par ordre croissant
#de nombre d'amis et que tous les utilisateurs ont un nombre d'amis di
#différent.
#Or di appartient nécessairement à l’intervalle [0; n-1] : en effet,
#chaque sommet a entre 0 et n-1 voisins
#Comme tous les di sont distincts, on a : di = i - 1
#(toutes les valeurs de l’intervalle [0; n - 1] sont utilisées)
#Ce qui signifie en particulier que l'individu vn est relié à tous les autres
#individus, en particulier avec v1. Ce qui contredit l’affirmation d1 = 0.
#
#Si on considère qu'une personne a forcément au moins un ami,
#c'est encore plus simple:
#les di ont une valeur entre 0 et n-1 et il y a n individus, donc pas assez de valeurs pour tous les di.
#
#Donc l'hypothèse "il n'existe pas 2 personnes ayant le même nombre d'amis"
#est fausse.



#Exercice 4
def diviseurs(k):
    """Construit le graphe des diviseurs"""
    G = initGraph(list(range(1,k+1)), [])
    for s in range(1,k+1):
        for i in range(1,s+1): #on peut optimiser ici, l'avantage c'est qu'on fera la boucle s->s
            if s%i==0:
                G = addEdge(G, i, s)
    return G
        
