""" 
.. _py_max_ones_problem_int_solution_vns_support:

The :mod:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution_vns_support` contains 
class :class:`~opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution_vns_support.MaxOnesProblemBinaryIntSolutionVnsSupport`, 
that represents solution of the :ref:`Problem_Max_Ones`, where `int` representation of the problem has been used.
"""

import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)

from copy import deepcopy
from random import choice
from random import randint

from uo.utils.logger import logger
from uo.target_solution.target_solution import ObjectiveFitnessFeasibility
from uo.algorithm.algorithm import Algorithm
from uo.algorithm.metaheuristic.variable_neighborhood_search.problem_solution_vns_support import ProblemSolutionVnsSupport

from opt.single_objective.trivial.max_ones_problem.max_ones_problem import MaxOnesProblem
from opt.single_objective.trivial.max_ones_problem.max_ones_problem_binary_int_solution import MaxOnesProblemBinaryIntSolution

class MaxOnesProblemBinaryIntSolutionVnsSupport(ProblemSolutionVnsSupport[int]):
    
    def __init__(self)->None:
        """
        Create new `MaxOnesProblemBinaryIntSolutionVnsSupport` instance
        """
        return

    def __copy__(self):
        """
        Internal copy of the `MaxOnesProblemBinaryIntSolutionVnsSupport`

        :return: new `MaxOnesProblemBinaryIntSolutionVnsSupport` instance with the same properties
        :rtype: MaxOnesProblemBinaryIntSolutionVnsSupport
        """
        sup = deepcopy(self)
        return sup

    def copy(self):
        """
        Copy the `MaxOnesProblemBinaryIntSolutionVnsSupport`
        
        :return: new `MaxOnesProblemBinaryIntSolutionVnsSupport` instance with the same properties
        :rtype: `MaxOnesProblemBinaryIntSolutionVnsSupport`
        """        
        return self.__copy__()
        
    def shaking(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer:Algorithm)->bool:
        """
        Random VNS shaking of k parts such that new solution code does not differ more than k from all solution codes 
        inside shakingPoints 

        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: if shaking is successful
        :rtype: bool
        """    
        if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for i in range(0,k):
                positions.append(choice(range(problem.dimension)))
            mask:int = 0
            for p in positions:
                mask |= 1 << p
            solution.representation ^= mask
            all_ok:bool = True
            if solution.representation.bit_count() > problem.dimension:
                all_ok = False
            if all_ok:
                break
        if tries < limit:
            optimizer.evaluation += 1
            if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
                return solution
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
            return False 

    def local_search_best_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryIntSolution:
        """
        Executes "best improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: MaxOnesProblemBinaryIntSolution
        """
        if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
            return solution
        if k < 1 or k > problem.dimension:
            return solution
        if k==1:
            best_rep:int = None
            best_triplet:ObjectiveFitnessFeasibility =  ObjectiveFitnessFeasibility(solution.objective_value,
                    solution.fitness_value, solution.is_feasible)
            for i in range(0, problem.dimension):
                mask:int = 1 << i
                solution.representation ^= mask 
                optimizer.evaluation += 1
                if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
                    return solution
                optimizer.write_output_values_if_needed("before_evaluation", "b_e")
                new_triplet = solution.calculate_objective_fitness_feasibility(problem)
                optimizer.write_output_values_if_needed("after_evaluation", "a_e")
                if new_triplet.fitness_value > best_triplet.fitness_value:
                    best_triplet = new_triplet
                    best_rep = solution.representation
                solution.representation ^= mask 
            if best_rep is not None:
                solution.representation = best_rep
                solution.objective_value = best_triplet.objective_value
                solution.fitness_value = best_triplet.fitness_value
                solution.is_feasible = best_triplet.is_feasible
                return solution
            return solution
        else:
            best_ind:int = None
            best_fv:float = solution.fitness_value
            # initialize indexes
            indexes:list[int] = []
            for i in range(1,k):
                indexes.append(i)
            is_over:boolean = False
            while not is_over:
                # collect positions for inversion from indexes
                # invert and compare, switch of new is better
                # increment indexes and set is_over on True when indexes are exhausted
                is_over = True
            return solution

    def local_search_first_improvement(self, k:int, problem:MaxOnesProblem, solution:MaxOnesProblemBinaryIntSolution, 
            optimizer: Algorithm)->MaxOnesProblemBinaryIntSolution:
        """
        Executes "first improvement" variant of the local search procedure 
        
        :param int k: int parameter for VNS
        :param `MaxOnesProblem` problem: problem that is solved
        :param `MaxOnesProblemBinaryIntSolution` solution: solution used for the problem that is solved
        :param `Algorithm` optimizer: optimizer that is executed
        :return: result of the local search procedure 
        :rtype: MaxOnesProblemBinaryIntSolution
        """
        if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
            return solution
        if k < 1 or k > problem.dimension:
            return solution
        if k==1:
            best_fv:float = solution.fitness_value
            for i in range(0, problem.dimension):
                mask:int = 1 << i
                solution.representation ^= mask 
                optimizer.evaluation += 1
                if optimizer.evaluations_max > 0 and optimizer.evaluation > optimizer.evaluations_max:
                    return solution
                optimizer.write_output_values_if_needed("before_evaluation", "b_e")
                new_triplet = solution.calculate_objective_fitness_feasibility(problem)
                optimizer.write_output_values_if_needed("after_evaluation", "a_e")
                if new_triplet.fitness_value > best_fv:
                    solution.fitness_value = new_triplet.fitness_value
                    solution.objective_value = new_triplet.objective_value
                    solution.is_feasible = new_triplet.is_feasible
                    return solution
                solution.representation ^= mask
            return solution
        else:
            best_fv:float = solution.fitness_value
            # initialize indexes
            indexes:list[int] = []
            for i in range(1,k):
                indexes.append(i)
            is_over:boolean = False
            while not is_over:
                # collect positions for inversion from indexes
                # invert and compare, switch and exit if new is better
                # increment indexes and set is_over on True when indexes are exhausted
                is_over = True
            return solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the vns support instance

        :param delimiter: delimiter between fields
        :type delimiter: str
        :param indentation: level of indentation
        :type indentation: int, optional, default value 0
        :param indentation_symbol: indentation symbol
        :type indentation_symbol: str, optional, default value ''
        :param group_start: group start string 
        :type group_start: str, optional, default value '{'
        :param group_end: group end string 
        :type group_end: str, optional, default value '}'
        :return: string representation of vns support instance
        :rtype: str
        """        
        return 'MaxOnesProblemBinaryIntSolutionVnsSupport'

    def __str__(self)->str:
        """
        String representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the vns support instance

        :return: string representation of the vns support instance
        :rtype: str
        """
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        """
        Formatted the vns support instance

        :param str spec: format specification
        :return: formatted vns support instance
        :rtype: str
        """
        return self.string_rep('|')
