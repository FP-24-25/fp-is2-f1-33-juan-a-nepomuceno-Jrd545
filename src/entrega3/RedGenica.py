'''
Created on 19 dic 2024

@author: joaqu
'''

from __future__ import annotations
from entrega3.E_grafo import E_grafo
from entrega3.Gen import Gen
from entrega3.RelacionGenAGen import RelacionGenAGen
from entrega3.E_grafo import Graph_type, Traverse_type
from us.lsi.tools.File import lineas_de_fichero, absolute_path

class RedGenica(E_grafo[Gen, RelacionGenAGen]):
    def __init__(self, tipo_grafo: Graph_type, tipo_recorrido: Traverse_type):
        super().__init__(tipo_grafo, lambda r: r.conexion, tipo_recorrido)  # El peso se pasa como el valor de conexión
        self.genes_por_nombre = {}

    @staticmethod
    def of() -> RedGenica:
        return RedGenica(Graph_type.UNDIRECTED, Traverse_type.FORWARD)

    @staticmethod
    def parse(fichero_genes: str, fichero_relaciones: str) -> RedGenica:
        red_genica = RedGenica.of()

        # Leer genes y añadirlos como vértices
        with open(fichero_genes, 'r') as f:
            for linea in f:
                gen = Gen.parse(linea.strip())
                red_genica.add_vertex(gen)
                red_genica.genes_por_nombre[gen.nombre] = gen

        # Leer relaciones y añadirlas como aristas
        with open(fichero_relaciones, 'r') as f:
            for linea in f:
                relacion = RelacionGenAGen.parse(linea.strip())
                gen1 = red_genica.genes_por_nombre.get(relacion.nombre_gen1)
                gen2 = red_genica.genes_por_nombre.get(relacion.nombre_gen2)

                if gen1 and gen2:  # Asegurarse de que ambos genes existen
                    red_genica.add_edge(gen1, gen2, relacion)

        return red_genica
    
    def __str__(self) -> str:
        # Utilizar los métodos vertex_set() y edge_set() de E_grafo para obtener vértices y aristas
        vertices = "\n".join(str(v) for v in self.vertex_set())
        aristas = "\n".join(
            f"RelacionGenAGen(nombre_gen1='{e.nombre_gen1}', nombre_gen2='{e.nombre_gen2}', conexion={e.conexion:.2f})"
            for e in self.edge_set()
            )
        return f"Vertices:\n{vertices}\n\nAristas:\n{aristas}"



if __name__ == "__main__":
    red_genica = RedGenica.parse(absolute_path('resources/genes.txt'), absolute_path('resources/red_genes.txt'))
    print(red_genica)

