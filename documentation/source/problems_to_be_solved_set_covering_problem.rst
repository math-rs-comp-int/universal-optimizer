..  _Problem_Set_Covering:

Set Covering Problem
=========================

Set Covering Problem is the NP-hard problem often found in combinatoral optimization. The main goal is to find minimal number of subsets that cover initial set.

## Problem Definition

- **Instance:** An initial set U (called universe), and a set S = {S1, S2, ..., Sn} ⊆ U of subsets of U.

- **Solution:**  Find a set of subsets from S that cover entire set U.

- **Measure:** Minimize the number of sets found in a solution.

* Minimum Multi Cut Problem. Problem is represented with class :ref:`SetCoveringProblemProblem<py_set_covering_problem>`. 