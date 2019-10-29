"""Testing Script for the random walk application"""

from RandomWalk import parse_input, convert_to_graph, generate_multiple_walks, output_walks


def main():

  # Change these parameters to get desired output:
  N = 3
  L = 3
  graphname = "graph1.txt"
  outputname = "out1.txt"

  lines = parse_input(graphname)
  graph = convert_to_graph(lines)
  walks = generate_multiple_walks(graph, N, L)
  output_walks(walks, outputname)


if __name__ == "__main__":
  main()
