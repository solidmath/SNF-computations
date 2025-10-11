def DPow(G):
    M=[]
    N=[]
    A=DiGraph()
    for g in G:
        o=g.order()
        if o!=1:    
            for k in range(2,o):
                A.add_edge((g, g^(k)))
    return(A)

def c(m):
    return CyclicPermutationGroup(m)

def ordered_adjacency_matrix(G):
    elements = [(g, g.order()) for g in G if g.order() != 1]
    elements.sort(key=lambda x: x[1])  
    
    n = len(elements)
    A = matrix(ZZ, n, n)
    
    element_to_index = {elem[0]: i for i, elem in enumerate(elements)}
    
    for i, (g, _) in enumerate(elements):
        for k in range(2, g.order()):
            j = element_to_index[g^k]
            A[i, j] = 1
    
    return A

def adj(n):
    G = DPow(c(n))
    A = ordered_adjacency_matrix(G)  
    
    
    rows_to_delete = [i for i in range(A.nrows()) if all(A[i, j] == 0 for j in range(A.ncols()))]
    A = A.delete_rows(rows_to_delete)
    I = identity_matrix(n-1) 
    I = I.delete_rows(rows_to_delete)
    I_minus_A_transpose = (I - A).transpose()
    
    return I_minus_A_transpose


from sage.homology.matrix_utils import dhsw_snf

def circulant_matrix(n):
    first_row = [1] + [-1] * (n - 1)
    return matrix([[first_row[(i - j) % n] for j in range(n)] for i in range(n)])



def Pow(S):
    G=DiGraph(multiedges=True, loops= False)
    G.add_vertices(list(S))
    N=S.order()
    for s in S: G.add_edges([(s,s**k) for k in range(2,s.order()+1)])
    G.relabel({x for x in range(N)})
    return G