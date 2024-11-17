""" 
..  _py_MonteCarlo_optimizer:

The :mod:`~uo.algorithm.metaheuristic.variable_neighborhood_search.variable_neighborhood_search` contains class :class:`~.uo.metaheuristic.variable_neighborhood_search.variable_neighborhood_search.MonteCarloOptimizer`, that represents implements algorithm :ref:`MonteCarlo<Algorithm_Variable_Neighborhood_Search>`.
"""

from pathlib import Path

from uo.solution.quality_of_solution import QualityOfSolution
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from random import choice
from random import random

from dataclasses import dataclass

from uo.utils.logger import logger

from typing import Optional

from uo.problem.problem import Problem
from uo.solution.solution import Solution

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.algorithm.metaheuristic.single_solution_metaheuristic import SingleSolutionMetaheuristic

@dataclass
class MonteCarloOptimizerConstructionParameters:
        """
        Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search_constructor_parameters.
        MonteCarloOptimizerConstructionParameters` represents constructor parameters for Monte Carlo algorithm.
        """
        finish_control: Optional[FinishControl] = None
        problem: Problem = None
        solution_template: Optional[Solution] = None
        output_control: Optional[OutputControl] = None
        random_seed: Optional[int] = None
        additional_statistics_control: Optional[AdditionalStatisticsControl] = None

class MonteCarloOptimizer(SingleSolutionMetaheuristic):
    """
    Instance of the class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.MonteCarloOptimizer` encapsulate 
    :ref:`Algorithm_Variable_Neighborhood_Search` optimization algorithm.
    """
    
    def __init__(self, 
            finish_control:FinishControl, 
            problem:Problem, 
            solution_template:Optional[Solution],
            output_control:Optional[OutputControl]=None, 
            random_seed:Optional[int]=None, 
            additional_statistics_control:Optional[AdditionalStatisticsControl]=None
        )->None:
        """
        Create new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.MonteCarloOptimizer`. 
        That instance implements :ref:`MonteCarlo<Algorithm_Variable_Neighborhood_Search>` algorithm. 

        :param `FinishControl` finish_control: structure that control finish criteria for metaheuristic execution
        :param int random_seed: random seed for metaheuristic execution
        :param `AdditionalStatisticsControl` additional_statistics_control: structure that controls additional 
        statistics obtained during population-based metaheuristic execution        
        :param `OutputControl` output_control: structure that controls output
        :param `Problem` problem: problem to be solved
        :param `Solution` solution_template: initial solution of the problem 
        """
        super().__init__( name='MonteCarlo', 
                finish_control=finish_control, 
                random_seed=random_seed, 
                additional_statistics_control=additional_statistics_control, 
                output_control=output_control, 
                problem=problem,
                solution_template=solution_template)
        self.current_solution = None
        if self.solution_template is not None:
            self.current_solution = self.solution_template.copy()

    def copy(self):
        """
        Internal copy of the current instance 
        
        :return: new instance with the same properties
        """
        fc:Optional[FinishControl] = None
        if self.finish_control is not None:
            fc = self.finish_control.copy()
        pr:Optional[Problem] = None
        if self.problem is not None:
            pr = self.problem.copy()
        st:Optional[Solution] = None
        if self.solution_template is not None:
            st = self.solution_template.copy()
        oc:Optional[OutputControl] = None
        if self.output_control is not None:
            oc = self.output_control.copy()
        asc:Optional[AdditionalStatisticsControl] = None
        if self.additional_statistics_control is not None:
            asc = self.additional_statistics_control.copy()
        ga_opt:'MonteCarloOptimizer' = MonteCarloOptimizer(fc,
                                                pr,
                                                st,
                                                oc,
                                                self.random_seed,
                                                asc)
        return ga_opt    

    @classmethod
    def from_construction_tuple(cls, construction_tuple:MonteCarloOptimizerConstructionParameters):
        """
        Additional constructor, that creates new instance of class :class:`~uo.algorithm.metaheuristic.variable_neighborhood_search.MonteCarloOptimizer`. 

        :param `MonteCarloOptimizerConstructionParameters` construction_tuple: tuple with all constructor parameters
        """
        return cls( 
            construction_tuple.finish_control,
            construction_tuple.problem, 
            construction_tuple.solution_template,
            construction_tuple.output_control, 
            construction_tuple.random_seed, 
            construction_tuple.additional_statistics_control
        )

    def init(self)->None:
        """
        Initialization of the MonteCarlo algorithm
        """
        super().init()
        self.current_solution.init_random(self.problem)
        self.evaluation = 1
        self.current_solution.evaluate(self.problem)
        self.best_solution = self.current_solution
    
    def main_loop_iteration(self)->None:
        """
        One iteration within main loop of the MonteCarlo algorithm
        """
        self.iteration += 1
        self.current_solution.init_random(self.problem)
        improvement:bool = self.current_solution.is_better(self.best_solution, self.problem)
        if improvement:
            # update auxiliary structure that keeps all solution codes
            self.update_additional_statistics_if_required(self.current_solution)
            self.best_solution = self.current_solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='',group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the `MonteCarloOptimizer` instance

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
        :return: string representation of instance that controls output
        :rtype: str
        """             
        s = delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_start
        s = super().string_rep(delimiter, indentation, indentation_symbol, '', '')
        s += delimiter
        if self.current_solution is not None:
            s += 'current_solution=' + self.current_solution.string_rep(delimiter, indentation + 1, 
                    indentation_symbol, group_start, group_end) + delimiter
        else:
            s += 'current_solution=None' + delimiter
        for _ in range(0, indentation):
            s += indentation_symbol  
        for _ in range(0, indentation):
            s += indentation_symbol  
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the `MonteCarloOptimizer` instance

        :return: string representation of the `MonteCarloOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('|')
        return s;

    def __repr__(self)->str:
        """
        String representation of the `MonteCarloOptimizer` instance

        :return: string representation of the `MonteCarloOptimizer` instance
        :rtype: str
        """
        s = self.string_rep('\n')
        return s

    def __format__(self, spec:str)->str:
        """
        Formatted the MonteCarloOptimizer instance

        :param spec: str -- format specification 
        :return: formatted `MonteCarloOptimizer` instance
        :rtype: str
        """
        return self.string_rep('\n',0,'   ','{', '}')
