import networkx as nx
def get_distances(num_nodes):
    distances={}
    for i in range (1,num_nodes+1):
        for j in range (i+1,num_nodes+1):
            distance = float(input("Enter the distance between node {i} and node {j} : "))
            distances[(i,j)]=distance
            distances[(j,i)]=distance
    return distances

def tsp_optimal_drilling(distance):
    G=nx.Graph()
    G.add_weighted_edges_from((i,j,distance) for(i,j),distance in distances.items())
    optimal_order=nx.approximation.traveling_salesman_problem(G,cycle=True)
    return optimal_order

def calculate_optimal_cost(drill_order,distances):
    total_cost=sum(distances[(drill_order[i],drill_order[i+1])] for i in range (len(drill_order)-1))
    return total_cost

if __name__ == "__main__":
    while True:
        num_nodes =  int(input("Enter the no of drill holes (nodes) :"))
        distances = get_distances(num_nodes)
        optimal_order = tsp_optimal_drilling(distances)
        optimal_cost = calculate_optimal_cost(optimal_order,distances)
        print("Optimal drilling order : ",optimal_order)
        print("Total optinal cost : ",optimal_cost)
        try_again=input("Do yo want yo try again with different no of nodes ? (y/n) : ").lower()
        if try_again != "y":
            break

# Enter the no of drill holes (nodes) :4
# Enter the distance between node {i} and node {j} : 4
# Enter the distance between node {i} and node {j} : 7
# Enter the distance between node {i} and node {j} : 6
# Enter the distance between node {i} and node {j} : 8
# Enter the distance between node {i} and node {j} : 1
# Enter the distance between node {i} and node {j} : 5
# Optimal drilling order :  [1, 3, 4, 2, 1]
# Total optinal cost :  17.0
# Do yo want yo try again with different no of nodes ? (y/n) : n