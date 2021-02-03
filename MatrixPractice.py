
#1st PART: COURTESY OF STACK OVERFLOW
import networkx as nx
import numpy as np
from datetime import datetime, time
from networkx.algorithms import community as nc

def main():

    #read matrix without head.
    #open the final output file and write the matrix information ot it
    a = np.loadtxt('LFR_Matrix_for_N1000_mu03_seed1.csv', delimiter=',', dtype=float)  
    outfile= open('MatrixPractice_Output.txt', 'w')
    outfile.write ("Matrix:\n")
    outfile.write (str(a))
    outfile.write ('\n\nMatrix shape:'+ str(a.shape[0]) + "*" + str(a.shape[1]))
    #Shape Function Def: Numpy function. The shape is a tuple of integers. 
    #These numbers denote the lengths of the corresponding array dimension



    num_edge = 0 #record counter for number of edges found
    edgeSet = set() #data structure that will store all edges -> random and unordered


    #LOGIC: two for-loops that iterate by the dimension of the numpy array in search of 1, 
    #       if found and the edge is not already in the edgelist then it will be added to 
    #       the set() created and the counter increases by one.
    for row in range(a.shape[0]): #shape[0] = 1000
        for column in range(a.shape[1]): #shape[0]= 1000
            if a.item(row,column) == 1 and (column,row) not in edgeSet: #get rid of repeat edge
                num_edge += 1
                edgeSet.add((row,column))

    #Write number of edges and list of edges to the output file
    outfile.write  ('\nNum_edge:'+ str(num_edge))
    outfile.write  ('\nEdge Set:'+ str(edgeSet))
    outfile.write  ('\n')
    
    #1/28/2021 Open the Edgelist file in write mode and sends every edgelist pair 1 by 1 
    #to the file each on a new line 
    outfile2= open('MatrixEdgelist.txt','w')
    for edge in edgeSet:
        outfile2.write (str(edge[0]) +' '+ str(edge[1])+ '\n')
    outfile2.close() #close edglist file in write mode
    

    #12/29/2021 Graph Construction and read matrix from csv file
    #   later altered to use the new edglist file not matrix
    G = nx.Graph() 
    infile= open('MatrixEdgelist.txt', 'r', encoding='utf-8-sig') 
    G= nx.read_edgelist(infile)



    #12/28/2020 Record CPU time and output of Breadth First operation and write it to the output file
    start = datetime.now()
    bSearch= list(nx.edge_bfs(G,'5'))
    end = datetime.now() 
    outfile.write('\nBreadth First Search from Matrix 5:\n\t' + str(bSearch))
    time_taken = end - start
    print("Seconds for Breadth First Search: ", (time_taken).total_seconds()*1000, " ms")
    outfile.write("Seconds for Breadth First Search: "+ str((time_taken).total_seconds()*1000) + " ms")


    #12/28/2020 Record CPU time and output of Depth First operation and write it to the output file
    start = datetime.now()
    DList=list(nx.edge_dfs(G,'5'))
    end = datetime.now() 
    outfile.write('\n\nDepth First Search on 5 with no depth limit:\n\t' + str(DList))
    time_taken = end - start
    print("Seconds for Depth First Search: ", (time_taken).total_seconds()*1000, " ms")
    outfile.write("Seconds for Depth First Search: "+ str((time_taken).total_seconds()*1000) + " ms")

    #1/08/2021 Record CPU time and output of Dijkstra operations and write it to the output file
    start = datetime.now()
    dijpath= nx.dijkstra_path(G,'5','777') 
    end = datetime.now()
    outfile.write('\n\nShortest path from node 5 to node 777:\n\t' + str(dijpath))
    time_taken = end - start
    #print('Time: ',time_taken)
    print("Seconds for Dijkstra Search: ", (time_taken).total_seconds()*1000, " ms")
    outfile.write("Seconds for Dijkstra Search: "+ str((time_taken).total_seconds()*1000) + " ms")

    #1/14/2021 ALL Output is still an issue. sending an empty list to the output file
    #   SOLVED: 1/27/2021 Stackoverflow to correctly create the graph

    # Return Approximated average clustering coefficient.
    avgC= nx.average_clustering(G)
    print('Average Clustering of this matrix is:', avgC)
    outfile.write('Average Clustering of this matrix is:'+ str(avgC))

    #Find communities in a graph using the Girvan–Newman method.
    #RETURNS: Iterator over tuples of sets of nodes in G. Each set of node is a community, each tuple is a 
    #sequence of communities at a particular level of the algorithm.

    #2/3/2021 locate time complexity NOTES
    comp = nc.girvan_newman(G)
    for c in next(comp):
        tuple(sorted(c))

    print('Sequence of communities:\n',c)
    outfile.write('Sequence of communities:\n'+ str(c))

main()
