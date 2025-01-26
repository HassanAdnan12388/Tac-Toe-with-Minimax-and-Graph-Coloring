# Importing modules and libraries
import networkx as nx
import matplotlib.pyplot as plt
import argparse
import sys
# You may add some imports here

# Define the graph
edges = [
    ("PL", "GE"), ("PL", "CZ"), ("GE", "CZ"), ("CZ", "AU"),
    ("CZ", "SK"), ("AU", "SK"), ("SK", "HU"), ("AU", "HU"),
    ("AU", "SL"), ("HU", "SL"), ("SL", "CR"), ("HU", "CR"),
    ("CR", "BH"), ("HU", "SE"), ("HU", "RO"), ("SE", "RO"),
    ("BH", "SE"), ("CR", "SE"), ("RO", "BG"), ("BG", "GR")
]

# Create the graph
G = nx.Graph()
G.add_edges_from(edges)

# Constraints
colors = ["red", "green", "blue"]
domain = {node: colors for node in G.nodes()}
domain["PL"] = ["red"]  
domain["GR"] = ["green"]
domain["SL"] = ["red"]
domain["HU"] = ["green"]

# /////////////////////////////////////////////////////////////////////////////////////////////// #
# Arc consistency algorithm


def arc_consistency(G, domain):
    domain = {node: sorted(colors) for node, colors in domain.items()}
    # print (domain)
    for node in G.nodes:
        # print("NODE: ", node, domain[node])
        noden = [neighbor for edge in edges for neighbor in edge if node in edge and neighbor != node]
        nodeneighbours = list(set(noden))
        for neighbour in nodeneighbours:
            # print(neighbour, domain[neighbour])
            if len(domain[node])==1:
                if len(domain[neighbour]) > 1 and neighbour not in ["PL", "GR", "SL", "HU"]:
                    colortoremove = domain[node][0] 
                    # print("color of node: ",color)
                    domain[neighbour] = [color for color in domain[neighbour] if color != colortoremove]
                    # print(neighbour, domain[neighbour])
            else:
                for xi in domain[node]:
                    colortoremove = xi 
                    if len(domain[neighbour]) > 1 and neighbour not in ["PL", "GR", "SL", "HU"]:
                        # print("color to remove: ",xi)
                        domain[neighbour] = [color for color in domain[neighbour] if color != colortoremove]
                        # print("new: ", neighbour, domain[neighbour])

        # print("-----")
    # return a dictionary of the form {node: color} for the solution e.g. {"PL": "red", "HU": "green", ...}
    return {node: domain[node][0] for node in G.nodes }



# /////////////////////////////////////////////////////////////////////////////////////////////// #
# Backtracking algorithm
def dfs_util(node, G, domain, solution):
    if node == None:  
        return True
    for color in domain[node]:
        if all(color != solution[neighbor] for neighbor in G.neighbors(node) if neighbor in solution):
            solution[node] = color
            next_node = None
            for n in G.nodes:
                if n not in solution:
                    next_node = n
                    break
            if dfs_util(next_node, G, domain, solution):
                return True
            del solution[node]
    return False

def dfs_backtracking(G, domain):
    solution = {node: domain[node][0] for node in G.nodes if len(domain[node]) == 1}
    if dfs_util(next(iter(G.nodes)), G, domain, solution):
        return solution
    else :
        return {}




# /////////////////////////////////////////////////////////////////////////////////////////////// #

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--arc", help="Run Arc Consistency algorithm", action="store_true")
    parser.add_argument("-d", "--dfs", help="Run DFS with backtracking algorithm", action="store_true")
    parser.add_argument("-g", "--graph", help="Display the graph", action="store_true")

    args = parser.parse_args()

    # Generate fixed positions using spring_layout with a fixed seed
    pos = nx.spring_layout(G, seed=42)

    if args.graph:
        nx.draw(G, pos, with_labels=True, node_color="yellow")
        plt.show()

    elif args.arc:
        solution = arc_consistency(G, domain)
        print(solution)
        try:
            nx.draw(G, pos, with_labels=True, node_color=[solution[node] for node in G.nodes()])
        except:
            print("No / incorrect solution found.")
            nx.draw(G, pos, with_labels=True, node_color="yellow")
        plt.show()

    elif args.dfs:
        solution = dfs_backtracking(G, domain)
        print(solution)
        try:
            nx.draw(G, pos, with_labels=True, node_color=[solution[node] for node in G.nodes()])
        except:
            print("No / incorrect solution found.")
            nx.draw(G, pos, with_labels=True, node_color="yellow")
        plt.show()

    else:
        print("No algorithm specified. See help below.")
        parser.print_help()
        sys.exit()

if __name__ == "__main__":
    main()
