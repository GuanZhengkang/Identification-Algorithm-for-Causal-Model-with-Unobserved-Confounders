import numpy as np


class SMCMID():
    """
    Identification Algorithm for Causal Model with Unobserved Confounders (Semi-Markovian Causal Models)

    Attributes:
        G (np.nparray): DAG Graph
        P (): Conditional probability of variables
        c_components (list[set[int]]): 每个set是一个C-component包含的节点序号
    """
    def __init__(self, G, P):
        """
        邻接矩阵G要满足:
         1. 已完成拓扑排序 
         2. '3'表示有不可观测confounder, '+/-2'表示有向边同时有confounder

        Args:
            G: Initial DAG Graph (可能没有投影或拓扑排序)
            P: Conditional probability of variables
        """
        self.G = self.topological_sort(G)
        self.P = P
        if len(G.shape)!=2 or G.shape[0]!=G.shape[1]:
            raise KeyError("Graph matrix error")
        self.c_components = self.c_separate(self.G)


    @staticmethod
    def topological_sort(G):
        """
        对G进行拓扑排序

        Args:
            G: 原始DAG
        Returns:
            拓扑排序后DAG
        """
        topological_order = list(range(len(G)))
        for i in range(len(topological_order)):
            done = 0
            while done == 0:
                done = 1
                for j in range(i+1,len(topological_order)):
                    if G[topological_order[j]][topological_order[i]]==1 or G[topological_order[j]][topological_order[i]]==2:
                        topological_order[i],topological_order[j] = topological_order[j],topological_order[i]
                        done = 0
                        break
                    
        num_nodes = len(G)
        ts_G = [[0] * num_nodes for _ in range(num_nodes)]

        for i in range(num_nodes):
            for j in range(num_nodes):
                ts_G[i][j] = G[topological_order[i]][topological_order[j]]

        print("topological_order:", topological_order)
        return np.array(ts_G)


    @staticmethod
    def adjmatrix_projection(G, unobconflst:list):
        """
        普通邻接矩阵转换：
            不可观测节点直接删除
            '3'表示有不可观测confounder
            '+/-2'表示有向边同时有confounder

        Args:
            G: 原始DAG
            unobconflst: 不可观测节点序号
        Returns:
            投影后后DAG
        """
        pass


    @staticmethod
    def c_separate(G) -> list[set[int]]:
        """
        分割图G的C-components

        Args:
            G: 原始DAG
        Returns:
            List[Set[int]]: 每个set是一个C-component包含的节点序号
        """
        c_components = []
        visited = set()

        def dfs(node, c_component):
            visited.add(node)
            c_component.add(node)
            for ch in range(len(G)):
                if abs(G[node][ch]) > 1 and ch not in visited:
                    dfs(ch, c_component)

        for node in range(len(G)):
            if node not in visited:
                c_component = set()
                dfs(node, c_component)
                c_components.append(c_component)
        return c_components
    


    def c_factor_ident(self, c_component:set[int]) -> str:
        """
        依据self的原始DAG，给出C-component的识别公式

        Args:
            c_component: C-component set
        """
        express = ''
        
        for node in reversed(list(c_component)): #让输出好看一点
            express+='P(v_{}'.format(node)
            Gvi = [row[:node+1] for row in self.G[:node+1]]
            Gvi_c_components = self.c_separate(Gvi)
            for Gvi_c_component in Gvi_c_components:
                if node in Gvi_c_component: Ti = Gvi_c_component
            
            paTi = Ti.copy()
            for Ti_node in Ti:
                for Gvi_node in range(len(Gvi)):
                    if Gvi[Gvi_node][Ti_node] == 1: paTi.add(Gvi_node)
            paTi.discard(node)
            express+='|'
            for paTi_node in paTi: #reversed(list(paTi)):
                express+='v_{},'.format(paTi_node)
            express = express[:-1]+')'
        return express
    

    def do(self, x:int, s=None) -> str:
        """
        do单节点x下节点集合s的联合概率识别

        Args:
            x: do的节点
        """
        G = self.G.copy()
        if s == None:
            an_s = list(range(len(G)))
        else:
            an_s = []
            visited = set()

            def dfs(node, an_s):
                visited.add(node)
                an_s.append(node)
                for pa in range(len(G)):
                    if G[node][pa] < 0 and pa not in visited:
                        dfs(pa, an_s)

            for node in s:
                if node not in visited:
                    dfs(node, an_s)
            
            an_s = sorted(an_s)

        if x not in an_s:
            raise ValueError("x不是y的An节点，do(x)不影响y")
        
        ch_x = []
        for i in an_s:
            if G[x][i] == 1 or G[x][i] == 2:
                ch_x.append(i)
        for j in ch_x:
            if abs(G[x][j])>1:
                raise ValueError("不可识别")
        
        expresses = ''
        for c_component in self.c_components:
            if x in c_component:
                express = '\\sum_v{} '.format(x) + self.c_factor_ident(c_component)
            else:
                expresses += self.c_factor_ident(c_component) + " "
        expresses += express
        return expresses



G1 = np.array(
    [[ 0, 1, 3, 0, 0],
     [-1, 0, 1, 3, 0],
     [ 3,-1, 0, 1, 3],
     [ 0, 3,-1, 0, 1],
     [ 0, 0, 3,-1, 0]]
) 

a = SMCMID(G1,None)
a.c_components
a.c_factor_ident(a.c_components[0])
a.do(0)