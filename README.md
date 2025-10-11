# Grothendieck Groups of Leavitt Path Algebras over Power Graphs

This repository contains computational tools developed for the study of **Leavitt path algebras (LPAs)** defined over **directed power graphs** of finite groups.  
The scripts are mainly designed to compute the **Grothendieck group** \( K_0(L_K(E)) \) of an LPA using the **Smith Normal Form (SNF)** of matrices derived from the graph.

These codes were created as part of my master’s research, *“Grothendieck group of the Leavitt path algebra over power graphs of prime-power cyclic groups.”*

---

### Features
- Construction of **directed power graphs** of finite groups (especially cyclic and dihedral groups)
- Generation of adjacency and incidence matrices of the graph
- Computation of **Smith Normal Form (SNF)** to determine  
  \[
  K_0(L_K(E)) \cong \mathbb{Z}^r \oplus \bigoplus_i \mathbb{Z}_{n_i}
  \]
- Automatic verification of properties such as:
  - Simplicity  
  - Purely infinite simplicity  
  - IBN (Invariant Basis Number) property

---

### Mathematical Background
For a finite directed graph \( E \), the Grothendieck group of its Leavitt path algebra is
\[
K_0(L_K(E)) \cong \operatorname{coker}(I - A_E^T),
\]
where \( A_E \) is the adjacency matrix of \( E \).  
Thus, the Smith Normal Form of \( I - A_E^T \) determines the invariant factors of \( K_0(L_K(E)) \).

The directed power graph approach leverages the combinatorial structure of finite groups to analyze the algebraic invariants of their corresponding Leavitt path algebras.

---

### Usage
Example (inside SageMath):
```python
# Load the main file
load("SNF_computation.sage")

# Compute the Grothendieck group for directed power graph of Z_9
result = grothendieck_group_pow(9)
print(result)
