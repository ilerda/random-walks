"""Contains all the necessary functions to generate
random walks from any input graph."""

from graph import Node, Graph
from random import randint


def parse_input(fname):

  with open(fname, "r") as fn:
    lines = fn.read()
  lines = lines.strip()
  lines_arr = lines.split("\n")
  return lines_arr


def convert_to_graph(lines):

  graph = Graph()
  all_nodes = {}
  for line in lines:
    if line[0] not in all_nodes:
      start_node = Node(line[0])
      graph.add_node(start_node)
      all_nodes[line[0]] = start_node
    else:
      start_node = all_nodes[line[0]]

    if line[5] not in all_nodes:
      end_node = Node(line[5])
      graph.add_node(end_node)
      all_nodes[line[5]] = end_node
    else:
      end_node = all_nodes[line[5]]

    start_node.add_neighbour(end_node)
  return graph

def generate_walk(graph, length):

  start_i = randint(0, len(graph.get_nodes())-1)
  curr_node = graph.get_nodes()[start_i]
  random_path = []
  for i in range(length):
    random_path.append(curr_node.data)
    # Potential edge case: we find a node that has no
    # outgoing nodes
    if len(curr_node.get_neighbours()) == 0:
      break
    new_i = randint(0, len(curr_node.get_neighbours())-1)
    curr_node = curr_node.get_neighbours()[new_i]
  if len(random_path) == length:
    return random_path
  return None


def generate_walk_string(walk):

  walk_string = ''
  for i in range(len(walk)):
    walk_string = walk_string + walk[i]
    if i < len(walk) - 1:
      walk_string = walk_string + ", "
  return walk_string


def generate_multiple_walks(graph, N, L):

  walks = []
  i = 0
  j = 0
  while i < N:
    new_walk = generate_walk(graph, L)
    if new_walk is not None:
      j = 0
      walk_string = generate_walk_string(new_walk)
      walks.append(walk_string)
      i += 1
    else:
      if j >= 5:
        raise Exception("Could not find valid path after five tries")
      j += 1
  return walks


def output_walks(walks, destination_path):

  with open(destination_path, "w+") as fn:
    for walk in walks:
      fn.write(walk+"\n")
  return


def main():
  """Debugging Code to test basic function output"""

  lines = parse_input("graph1.txt")
  print(lines)
  graph = convert_to_graph(lines)
  random_path = generate_walk(graph, 5)
  print(random_path)
  walk_string = generate_walk_string(random_path)
  print(walk_string)
  walks = generate_multiple_walks(graph, 3, 4)
  print(walks)
  output_walks(walks, "out1.txt")
  

if __name__ == "__main__":
  main()