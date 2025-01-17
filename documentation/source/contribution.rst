How to Contribute
=================


This system is developed in `Python <https://www.python.org>`_ programming language, using `poetry <https://python-poetry.org>`_ as project and package manager, `unittest <https://docs.python.org/3/library/unitest.html>`_  library for unit testing and `Sphinx <https://www.sphinx-doc.org/en/master>`_ system for documentation generation. Same tool set should be use for contribution to the project.

Contribution is encouraged in following four domains:

a. Designing novel optimization methods. Requirements:

    1. Algorithms should be derived from the specified class.

        - Class that implements metaheuristic optimization should be derived either from the :class:`uo.algorithm.metaheuristic.single_solution_metaheuristic.SingleSolutionMetaheuristic` class, or from the :class:`uo.algorithm.metaheuristic.population_based_metaheuristic.PopulationBasedMetaheuristic`. It should be placed into separate directory within :file:`/uo/algorithm/metaheuristic/` directory.

        - Class that implements exact optimization should be derived from the :class:`uo.algorithm.Algorithm` class. That class should be placed into separate directory within :file:`/uo/algorithm/` directory.

    2. Type hints and documentation.

        - All programming objects (classes, functions, variables, parameters, optional parameters etc.) should be `type-hinted <https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html>`_
        
        - All programming objects (classes, functions, etc.) should be properly documented using the system `Sphinx`, reStructuredText and doc comments within the code.

        - Each of the implemented algorithm should have separate documentation web page, where that algorithm is described and documented. At least, there should be the link from doc comments within implemented functionality toward the web page that explains algorithm and vice versa.  

    3. Unit testing coverage.
    
        - Implemented programming code should be fully covered with unit tests.  
    
        - Here, `unittest` framework  used. 
        
        - Test should be placed into separate sub-directory under :file:`/uo/tests/` directory. Directory structure within :file:`/uo/tests/` directory should mirror directory structure of the :file:`/uo/` directory.  

        - All developed code should be covered with unit test, and test coverage rate should be not less than 80%. 


b. Building application for solving optimization problems. Requirements:

    1. Program code for specific problem should to be put into the respective directory.

        - Each of the problems should have its own directory, with name equals to problem name. 
        
        - Code for multi-objective optimization should be placed under :file:`/opt/multi_objective/` directory, while code for single-objective optimization should be placed under :file:`/opt/single_objective/` directory.

        - Code for single-objective combinatorial optimization should be placed under :file:`opt/single_objective/comb/` directory, for single-objective constraint optimization within the :file:`/opt/single_objective/constraint/` directory, and code for single-objective global optimization in :file:`/opt/single_objective/global/` directory.
        

    2. Implemented applications should have examples of use for every approach contained within application. 
    
        - Those examples should be placed in root :file:`/` directory, and file name for example should be :file:`<problem>_<algorithm>_<representation>_exec.py`.


    3. For each problem under consideration, the problem class for specific problem should have method that read textual file and create instance of that specific problem.

    4. For each problem under consideration, there should be one file (named :file:`solver.py`, within the respective problem directory). That file will be entry point for all the methods aimed at solving the specific problem. All parameters that governs methods execution should be accessible to user through command-line parameters. Command-line parameters should have sufficient and adequate help system.


    5. Type hints and documentation.

        - All programming objects (classes, functions, variables, parameters, optional parameters etc.) should be `type-hinted <https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html>`_
        
        - All programming objects (classes, functions, etc.) should be properly documented using the system `Sphinx`, reStructuredText and doc comments within the code.

        - Problem that is solved should have separate documentation web page, where that problem is described and documented. At least, there should be the link from problem web page toward the web page that explains method that is used and vice versa.  


    6. Unit testing coverage.
    
        - Implemented programming code should be fully covered with unit tests, and `unittest` framework is used. 
        
        - Test should be placed into separate sub-directory under :file:`/opt/tests/` directory. Directory structure within :file:`/opt/tests/` directory should mirror directory structure of the :file:`/opt/` directory.  

        - All developed code should be covered with unit test, and test coverage rate should be not less than 80%. 

c. Designing and executing comparison experiments, using previously builded applications. Requirements: 

    1. Experiments should use only previously developed applications, not Python programming constructs. Comparison experiments should be invoked by batch/command file.

    2. Comparison experiments should be placed under :file:`/comparison/` directory.

d. Visualizing experimentally obtained data (either data about comparison, either data about algorithm execution). Requirements:

    1. Developed solution for the problems under consideration should be visualized. Visualizations should be invoked by batch/command file.

    2. Visualization efforts should be placed under :file:`/visualization/` directory.

Contributors
============

Contribution domains
--------------------

a. Contribution in the designing novel **optimization methods**:

    a.1. Library and application:
    
        1. Initial overall structure and organization - [VladimirFilipovic]_

    a.2. Total Enumeration (TE) exact algorithm: 
    
        2. Structure, organization and main loop implementation - [VladimirFilipovic]_ 

        3. Implementation with bit-array based complex counters (class :class:`~uo.utils.ComplexCounterBitArrayFull`, using `bitstring.BitArray` class) - [VladimirFilipovic]_

        4. Implementation with int based complex counters (classes :class:`~uo.utils.ComplexCounterUniformFull` and :class:`~uo.utils.ComplexCounterUniformAscending`, using `int` values) - [VladimirFilipovic]_

    a.3. Variable Neighborhood Search :ref:`Algorithm_Variable_Neighborhood_Search` (VNS) metaheuristics:
        
        5. Structure, organization and main loop implementation - [VladimirFilipovic]_ 

        6. Implementation of shaking and local searches with binary representation  (in class :class:`~uo.algorithm.variable_neighborhood_search.VnsShakingSupportStandardInt`, using `int` predefined type) - [VladimirFilipovic]_ 

        7. Implementation of shaking and local searches with binary representation (in class :class:`~uo.algorithm.variable_neighborhood_search.VnsShakingSupportStandardBitArray`,using :class:`bitstring.BitArray` class) - [VladimirFilipovic]_ 

    a.4. Genetic Algorithms :ref:`Algorithm_Genetic_Algorithm` (GA) metaheuristics:
        
        8. Structure, organization and main loop implementation - [MarkoRadosavljevic]_, [VladimirFilipovic]_ 

        9. Making class :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizer` to be abstract and dividing its functionality into non-abstract classes :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerGenerational` and :class:`uo.algorithm.metaheuristic.genetic_algorithm.GaOptimizerSteadyState` - [VladimirFilipovic]_ 

        10. Implementation of GA selection methods (in classes: :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaSelectionIdle`, :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaSelectionRoulette`)  - [MarkoRadosavljevic]_

        11. Implementation of GA crossover one point method (contained within class: :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaCrossoverSupportOnePointBitArray`), with binary representation (using `bitstring.BitArray` class) - [MarkoRadosavljevic]_ 

        12. Implementation of GA mutation one point method (contained within class: :class:`~uo.algorithm.metaheuristic.genetic_algorithm.GaMutationSupportOnePointBitArray`), with binary representation (using `bitstring.BitArray` class) - [MarkoRadosavljevic]_ 

    a.4. Electromagnetism-like :ref:`Algorithm_Electromagnetism_Like_Metaheuristic` (EM) metaheuristics:
        
        13. Structure, organization and main loop implementation - [AndjelaDamnjanovic]_


b. Contribution in solving **combinatorial** optimization problems:

    b.1. Ones Count Max Problem :ref:`Problem_Ones_Count_Max`:

        1. Representation of the problem (in class :class:`~opt.single_objective.comb.ones_count_max.MaxOnesCountProblem`) and solution (`BitArray`-based in class :class:`~opt.single_objective.comb.ones_count_max.MaxOnesCountProblemBitArraySolution` and `int`-based in class :class:`~opt.single_objective.comb.ones_count_max.MaxOnesCountProblemIntSolution`) - [VladimirFilipovic]_
        
        2. Integer Linear Programming method (using `linopy` library) - [VladimirFilipovic]_  

        3. Total Enumeration method, with solution that has binary `BitArray` representation - [VladimirFilipovic]_  

        4. Variable Neighborhood Search method, with solution that has binary `BitArray` representation - [VladimirFilipovic]_  

        5. Variable Neighborhood Search method, with solution that has binary `int` representation - [VladimirFilipovic]_  

        6. Genetic Algorithm method, with solution that has binary `BitArray` representation - [VladimirFilipovic]_  

        7. Entry point of the all methods for solving this problem, in file :file:`/opt/single_objective/comb/ones_count_max_problem/solver.py`. All parameters that governs method execution are accessible to user through command-line.  - [VladimirFilipovic]_  

    b.2. Minimum Multi Cut Problem :ref:`Problem_Minimum_Multi_Cut`:

        8. Representation of the problem (in class :class:`~opt.single_objective.comb.minimum_multi_cut_problem.MinMultiCutProblem`, that uses `ng.Graph` class for class representation) and solution with `BitArray`-based representation (in class :class:`~opt.single_objective.comb.minimum_multi_cut_problem.MinMultiCutProblemBitArraySolution`) - [MarkoRadosavljevic]_
        
        9. Variable Neighborhood Search method, with solution that has binary `BitArray` representation - [MarkoRadosavljevic]_  

        10. Genetic Algorithm method, with solution that has binary `BitArray` representation - [MarkoRadosavljevic]_  

    b.3. Set Covering Problem :ref:`Problem_Set_Covering`:

        11. Representation of the problem (in class :class:`~opt.single_objective.comb.set_covering_problem.set_covering_problem.MinSetCoverProblem`and solution with `BitArray`-based representation (in class :class:`~~opt.single_objective.comb.set_covering_problem.set_covering_problem_bit_array_solution.MinSetCoverProblemBitArraySolution`) - [AndjelaDamnjanovic]_
        
        12. Electromagnetism-like Metaheuristic method, with solution that has binary `BitArray` representation - [AndjelaDamnjanovic]_  

        13. ILP model, with `linopy` library and `Gurobi` solver - [AndjelaDamnjanovic]_  


c. Contribution in solving **global** optimization problems:


    c.1. Max Function One Variable Problem:

        1. Variable Neighborhood Search method, with solution that has binary `BitArray` representation - [VladimirFilipovic]_  

        2. Variable Neighborhood Search method, with solution that has binary `int` representation - [VladimirFilipovic]_  

        3. Entry point of the all methods for solving this problem, in file :file:`/opt/single_objective/glob/max_function_one_variable_problem/solver.py`. All parameters that governs method execution are accessible to user through command-line.  - [VladimirFilipovic]_  

Contributor List
----------------

.. [VladimirFilipovic] Vladimir Filipović, `<https://github.com/vladofilipovic>`_ e-mail: vladofilipovic@hotmail.com

.. [MarkoRadosavljevic] Marko Radosavljević, `<https://github.com/Markic01>`_ e-mail: mi20079@alas.matf.bg.ac.rs

.. [AndjelaDamnjanovic] Anđela Damjanović, `<https://github.com/AndjelaDamnjanovic>`_ e-mail: mi19059@alas.matf.bg.ac.rs
