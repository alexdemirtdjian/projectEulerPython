# -*- coding: utf-8 -*-

"""
Les graphes sont représentés sous la forme d'un dictionnaire avec deux clés:
- vertices est la liste de tous les sommets du graphe
- edges est la liste des tous les arcs du graphe, un arc étant un couple de sommets

"""

def remove(l,e):
        if l ==[]:
                return []
        elif l[0] == e:
                return l[1:]
        else:
                return remove(l[1:],e)
        


def initGraph(vertices=[],edges=[]):
        """
        Initialise un graphe orienté ou non sous forme de dictionnaire, par défaut vide de tout sommet et tout arc
        """
        return {"vertices":vertices,"edges":edges}


def vertices(graph):
        """
        Renvoie la liste des sommets du graphe
        """
        return graph["vertices"]


def edges(graph):
        """
        Renvoie la liste des arcs du graphe
        """
        return graph["edges"]


def verifGraph(graph):
        """
        Vérifie que les extrémités des arcs sont bien des sommets.
        Renvoie True ou False
        """
        for edge in edges(graph): 
                if edge[0] not in vertices(graph) or edge[1] not in vertices(graph):
                        return False
        return True


def printGraph(graph):
        print("Vertices: " + str(graph["vertices"]))
        print("Edges:")
        for edge in edges(graph):
                print("  "+str(edge[0])+"->"+str(edge[1]))


def nbVertices(graph):
        """
        Renvoie le nombre de sommets du graphe
        """
        return len(vertices(graph))

def nbEdges(graph):
        """
        Renvoie le nombre d'arcs du graphe
        """
        return len(edges(graph))


def addVertex(graph,vertex):
        """ 
        Ajoute un sommet au graphe (s'il n'est pas déjà présent)
        """
        if vertex not in vertices(graph):
                graph["vertices"]= graph["vertices"] + [vertex]
        return graph

def addEdge(graph,vertex1,vertex2):
        """
        Ajoute un arc au graphe (s'il n'est pas déjà présent).
        Si les extrémités de l'arcs n'existent pas dans le graphe, les sommets correspondant sont créés.
        """
        if (vertex1,vertex2) not in edges(graph):
                graph["edges"]= graph["edges"] + [(vertex1,vertex2)]
        if vertex1 not in vertices(graph):
                graph = addVertex(graph,vertex1)
        if vertex2 not in vertices(graph):
                graph= addVertex(graph,vertex2)
        return graph
                

def delEdge(graph,vertex1,vertex2):
        """
        Supprime un arc du graphe s'il est présent, sinon pas d'effet.
        """
        if (vertex1,vertex2) in edges(graph):
                graph["edges"]= remove(graph["edges"],(vertex1,vertex2))
        return graph


def delVertex(graph,vertex):
        """
        Supprime un sommet du graphe.
        Tous les arcs adjacents au sommet supprimé sont supprimés.
        """
        if vertex in vertices(graph):
                graph["vertices"]= remove(graph["vertices"],vertex)
                for edge in edges(graph):
                        if edge[0]==vertex or edge[1]==vertex:
                                delEdge(graph,edge[0],edge[1])
        return graph



def predecessors(graph,vertex):
        """
        Renvoie une liste contenant les prédécesseurs du sommet.
        """
        l = []
        if vertex in vertices(graph):
                for edge in edges(graph):
                        if edge[1]==vertex:
                                l=l+[edge[0]]
        return l
       

def successors(graph,vertex):
        """
        Renvoie une liste contenant les successeurs du sommet.
        """
        l = []
        if vertex in vertices(graph):
                for edge in edges(graph):
                        if edge[0]==vertex:
                                l=l+[edge[1]]
        return l
        
        
