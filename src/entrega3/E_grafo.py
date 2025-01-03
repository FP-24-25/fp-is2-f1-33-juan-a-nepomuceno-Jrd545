'''
Created on 17 nov 2024

@author: Joaquín Ramos Díaz
'''
from __future__ import annotations
from typing import TypeVar, Callable
from enum import Enum
from entrega3.Grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt

V = TypeVar('V')
E = TypeVar('E')

class Graph_type(Enum):
    UNDIRECTED = 1
    DIRECTED = 2
    

#===============================================================================
# Traverse_type -> Tipo de recorrido del grafo
#===============================================================================
class Traverse_type(Enum):
    FORWARD = 1
    BACK = 2

class E_grafo(Grafo[V,E]):
    
    def __init__(self,graph_type:Graph_type,weight:Callable[[E],float],traverse_type:Traverse_type=Traverse_type.FORWARD)->None:
        self._vertex_set:set[V] = set() # Conjunto de vértices del grafo (nodos)
        self._edge_set:set[E] = set() # Conjunto de aristas (relaciones entre nodos)
        self._edges_dict:dict[tuple[V,V],E] = {}  # Diccionario que mapea las parejas de vértices a las aristas
        self._neighbors:dict[V,set[V]] = {} # Diccionario que guarda los vecinos de cada vértice
        self._predecessors:dict[V,set[V]] = {} # Diccionario que guarda los predecesores (vértices anteriores) de cada vértice
        self._sources:dict[E,V] = {} # Diccionario que mapea las aristas a sus vértices de origen
        self._targets:dict[E,V] = {} # Diccionario que mapea las aristas a sus vértices de origen
        self._graph_type = graph_type # Tipo de grafo (dirigido o no dirigido)
        self._weight = weight  # Función que calcula el peso de una arista
        self._traverse_type = traverse_type # Tipo de recorrido: hacia adelante (FORWARD) o hacia atrás (BACK)
     
    def __add_neighbors(self, source:V, target:V)->None:
        if source not in self._neighbors:
            self._neighbors[source] = set()
        self._neighbors[source].add(target)
        
            
    def __add_predecessors(self, source:V, target:V)->None:
        if target not in self._predecessors:
            self._predecessors[target] = set()
        self._predecessors[target].add(source)

    def add_edge(self,source:V,target:V,e:E)->None:
        if source == target:
            raise ValueError("No se permiten bucles: el vértice de origen y destino no pueden ser iguales.")
    
        # Asegurarse de que los vértices existan en el grafo
        self.add_vertex(source)
        self.add_vertex(target)
    
        # No permitir aristas duplicadas
        if self.contains_edge(source, target):
            raise ValueError(f"La arista entre {source} y {target} ya existe.")
    
        # Añadir la arista en el grafo
        self._edges_dict[(source, target)] = e
        self._edge_set.add(e)
    
        # Si es un grafo dirigido, añadimos solo de source a target
        if self._graph_type == Graph_type.DIRECTED:
            self.__add_neighbors(source, target)  # Añadir vecino de source
            self.__add_predecessors(target, source)  # Añadir predecesor de target
        else:
            self.__add_neighbors(source, target)  # En un grafo no dirigido, añadimos los dos vértices
            self.__add_neighbors(target, source)

            # Almacenar los vértices de origen y destino
            self._sources[e] = source
            self._targets[e] = target
    
    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float:
        return self._weight(self._edges_dict.get((sourceVertex, targetVertex)))
        
        # Asegurarse de que los vértices existan en el grafo
        self.add_vertex(source)
        self.add_vertex(target)
        
        # No permitir aristas duplicadas
        if self.contains_edge(source, target):
            raise ValueError(f"La arista entre {source} y {target} ya existe.")
        
        # Añadir la arista en el grafo
        self._edges_dict[(source, target)] = edge
        self._edge_set.add(edge)
        # Si es un grafo dirigido, añadimos solo de source a target
        # Si es no dirigido, también añadimos de target a source
        if self._graph_type == Graph_type.DIRECTED:
            self.__add_neighbors(source, target)  # Añadir vecino de source
            self.__add_predecessors(target, source)  # Añadir predecesor de target
        else:
            self.__add_neighbors(source, target)  # En un grafo no dirigido, añadimos los dos vértices
            self.__add_neighbors(target, source)

        # Almacenar los vértices de origen y destino
        self._sources[edge] = source
        self._targets[edge] = target
    
    def add_vertex(self,vertex:V)->bool:
        if vertex not in self._vertex_set:
            self._vertex_set.add(vertex)
            return True
        return False

    
    def edge_source(self,edge:E)->V:
        # Verifica que `edge` es una clave válida en `_sources`
        if edge in self._sources:
            return self._sources[edge]
        else:
            raise KeyError(f"Edge {edge} not found in sources") 
                    
    def edge_target(self,edge:E)->V:
        if edge in self._targets:
            return self._targets[edge]
        else:
            raise KeyError(f"Edge {edge} not found in targets")
        
    def vertex_set(self)->set[V]:
        return self._vertex_set
     
    def edge_set(self)->set[E]:
        return self._edge_set
    
    def contains_edge(self,sourceVertex:V, targetVertex:V)->bool:
        return (sourceVertex, targetVertex) in self._edges_dict
     
    def neighbors(self,vertex:V)->set[V]:
        return self._neighbors.get(vertex,set())
    
    def predecessors(self,vertex:V)->set[V]:
        if self._graph_type == Graph_type.DIRECTED:
            return self._predecessors.get(vertex, set())
        else:
            return self._neighbors.get(vertex, set())
        
    def successors(self,vertex:V)->set[V]:
        if self._traverse_type == Traverse_type.FORWARD:
            return self._neighbors.get(vertex, set())
        elif self._traverse_type == Traverse_type.BACK:
            return self.predecessors(vertex)
        else:
            raise ValueError("Tipo de recorrido no válido, use 'FORWARD' o 'BACK'.")
    
    def edge(self,sourceVertex:V, targetVertex:V) -> E:
        return self._edges_dict[(sourceVertex,targetVertex)]
            
    def vertex_list(self)->list[V]:
        return list(self._vertex_set)
    
    def graph_type(self)->Graph_type:
        return self._graph_type
    
    def traverse_type(self)->Traverse_type:
        return self._traverse_type
    
    def weight(self)->Callable[[E],float]:
        return self._weight
    
    def inverse_graph(self)->E_grafo[V,E]:
        inverted_graph = E_grafo(self._graph_type, self._weight, self._traverse_type)
        
        for edge in self._edges_dict:
            source, target = edge
            edge_weight = self._edges_dict[edge]
            inverted_graph.add_edge(target, source, edge_weight)  # Invertir las aristas
        
        return inverted_graph
    
    def subgraph(self,vertices:set[V]) -> Grafo[V,E]:
        g:E_grafo[V,E] = E_grafo(self.graph_type(),self.weight(),self.traverse_type())
        for v in vertices:
            g.add_vertex(v)
        for e in self.edge_set():
            s = self.edge_source(e)
            t = self.edge_target(e)
            if s in vertices and t in vertices:
                g.add_edge(s,t,e)
        return g
    
    def plot_graph(self):
        # Create an empty networkx graph
        G = nx.DiGraph() if self._graph_type == Graph_type.DIRECTED else nx.Graph()
    
        # Add vertices to the graph
        for vertex in self._vertex_set:
            G.add_node(vertex)
    
        # Add edges to the graph
        edge_labels: dict = {}
        for edge in self._edge_set:
                # Asegúrate de que `edge` sea válido y pase a los métodos correctamente
                source = self.edge_source(edge)  # Aquí `edge` se pasa al método
                target = self.edge_target(edge)
                G.add_edge(source, target)
                edge_labels[(source, target)] = self._weight(edge)  # Usa el método _weight para calcular

    
        # Plot the graph using matplotlib
        plt.figure(figsize=(8, 8))  # You can adjust the size
        pos = nx.spring_layout(G, seed=42)  # Layout for node positioning
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color="red")
        # Show the plot
        plt.title("Graph Visualization")
        plt.show()
            
    def __str__(self):
        sep = '\n'
        return f'Vertices: \n{sep.join(str(x) for x in self._vertex_set)} \nAristas: \n{sep.join(str(x) for x in self._edge_set)}'

if __name__ == '__main__':
    pass

