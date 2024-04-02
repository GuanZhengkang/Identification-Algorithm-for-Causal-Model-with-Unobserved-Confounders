### Coming Soon
---
# Identification Algorithm for Causal Model with Unobserved Confounders (Semi-Markovian Causal Models)

## Tian, J., & Pearl, J. (2002, August). A general identification condition for causal effects. In Aaai/iaai (pp. 567-573).


### Semi-Markovian model
$$
M=\left\langle V, U, G_{V U}, P\left(v_i \mid p a_i, u^i\right), P(u)\right\rangle
$$

$$
P(v)=\sum_u \prod_i P\left(v_i \mid p a_i, u^i\right) P(u)
$$
$$
\begin{aligned}
& P_t(v) = \begin{cases}\sum_u \prod_{\left\{i \mid V_i \notin T\right\}} P\left(v_i \mid p a_i, u^i\right) P(u) & v \text { consistent with } t . \\
0 & v \text { inconsistent with } t .\end{cases}
\end{aligned}
$$

**bidirected path**: A path composed entirely of bidirected edges 

#### c-component (confounded component)
The set of variables $V$ can be partitioned into disjoint groups by assigning two variables to the same group if and only if they are connected by a bidirected path. Assume that $V$ is thus partitioned into $k$ groups $S_1, \ldots, S_k$, and denote by $N_j$ the set of $U$ variables that are parents of those variables in $S_j$. Clearly, the sets $N_1, \ldots, N_k$ form a partition of $U$. Define
$$
Q_j=\sum_{n_j} \prod_{\left\{i \mid V_i \in S_j\right\}} P\left(v_i \mid p a_i, u^i\right) P\left(n_j\right), j=1, \ldots, k .
$$
The disjointness of $N_1, \ldots, N_k$ implies that $P(v)$ can be decomposed into a product of $Q_j$ 's:
$$
P(v)=\prod_{j=1}^k Q_j .
$$
We will call each $S_j$ a c-component of $V$ in $G$ or a c-component of $G$, and $Q_j$ the $c$-factor corresponding to the c-component $S_j$.

### Identiﬁcation

##### Lemma 
Let a topological order over $V$ be $V_1<\ldots<$ $V_n$, and let $V^{(i)}=\left\{V_1, \ldots, V_i\right\}, i=1, \ldots, n$, and $V^{(0)}=$ $\emptyset$. For any set $C$, let $G_C$ denote the subgraph of $G$ composed only of variables in $C$. Then
(i) Each $c$-factor $Q_j, j=1, \ldots, k$, is identifiable and is given by
$$
Q_j=\prod_{\left\{i \mid V_i \in S_j\right\}} P\left(v_i \mid v^{(i-1)}\right) .
$$
(ii) Each factor $P\left(v_i \mid v^{(i-1)}\right)$ can be expressed as
$$
P\left(v_i \mid v^{(i-1)}\right)=P\left(v_i \mid p a\left(T_i\right) \backslash\left\{v_i\right\}\right),
$$
where $T_i$ is the c-component of $G_{V^{(i)}}$ that contains $V_i$.

#### Identification criterion for $P_x(v)$

Let $X$ belong to the c-component $S^X$ with corresponding c-factor $Q^X$.
Let $Q_x^X$ denote the c-factor $Q^X$ with the term $P\left(x \mid p a_x, u^x\right)$ removed, that is,
$$
Q_x^X=\sum_{n^X} \prod_{\left\{i \mid V_i \neq X, V_i \in S^X\right\}} P\left(v_i \mid p a_i, u^i\right) P\left(n^X\right) .
$$
We have
$$
\begin{gathered}
P(v)=Q^X \prod_i Q_i, \\
P_x(v)=Q_x^X \prod_i Q_i .
\end{gathered}
$$
Since all $Q_i$ 's are identifiable, $P_x(v)$ is identifiable if and only if $Q_x^X$ is identifiable, and we have the following theorem.

##### Theorem 

$P_x(v)$ is identifiable if and only if there is no bidirected path connecting $X$ to any of its children. When $P_x(v)$ is identifiable, it is given by
$$
P_x(v)=\frac{P(v)}{Q^X} \sum_x Q^X,
$$
where $Q^X$ is the c-factor corresponding to the c-component $S^X$ that contains $X$.







## Shpitser, I., & Pearl, J. (2006, July). Identification of joint interventional distributions in recursive semi-Markovian causal models. In AAAI (pp. 1219-1226).
