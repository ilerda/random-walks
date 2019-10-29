"""Two classes needed to implement a simple graph structure."""

class Node:
  
  def __init__(self, data):
    self.data = data
    self.neighbours = []

  def add_neighbour(self, n):
    self.neighbours.append(n)
  
  def get_neighbours(self):
    return self.neighbours


class Graph:

  def __init__(self):
    self.nodes = []
  
  def add_node(self,new_node):
    self.nodes.append(new_node)
  
  def get_nodes(self):
    return self.nodes
    