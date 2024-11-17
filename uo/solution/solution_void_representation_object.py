""" 
The :mod:`~uo.solution.solution_void_object_str` module describes the class :class:`~uo.solution.SolutionVoidObject`.
"""

from pathlib import Path
import sys
directory = Path(__file__).resolve()
sys.path.append(directory.parent)

from typing import Optional

from uo.utils.logger import logger

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.solution.quality_of_solution import QualityOfSolution


from uo.algorithm.optimizer import Optimizer
from uo.algorithm.output_control import OutputControl

class SolutionVoidObject(Solution[object, str]):
    def __init__(self, random_seed=None, 
                fitness_value=0, 
                fitness_values=None, 
                objective_value=0, 
                objective_values= None,  
                is_feasible=True,
                evaluation_cache_is_used=False, 
                evaluation_cache_max_size=0, 
                distance_calculation_cache_is_used=False, 
                distance_calculation_cache_max_size=0)->None:
        super().__init__(random_seed, 
        fitness_value, fitness_values, objective_value, objective_values, is_feasible,
        evaluation_cache_is_used, evaluation_cache_max_size, 
        distance_calculation_cache_is_used, distance_calculation_cache_max_size)

    def copy(self)->'SolutionVoidObject':
        fvs:Optional[list] = None
        if self.fitness_values is not None:
            fvs = self.fitness_values.copy()
        ovs:Optional[list] = None
        if self.objective_values is not None:
            ovs = self.objective_values.copy()
        obj:SolutionVoidObject = SolutionVoidObject(self.random_seed,
                                        self.fitness_value,
                                        fvs,
                                        self.objective_value,
                                        ovs,
                                        self.is_feasible)
        obj.__evaluation_cache_cs = None
        if self.evaluation_cache_cs is not None:
            obj.__evaluation_cache_cs = self.evaluation_cache_cs
        obj.__representation_distance_cache_cs = None
        if self.representation_distance_cache_cs is not None:
            obj.__representation_distance_cache_cs = self.representation_distance_cache_cs
        return obj

    def borrow_from(self, original: Solution) -> None:
        super().borrow_from(original)
    
    def argument(self, representation:object)->str:
        return str(representation)

    def init_random(self, problem:Problem)->None:
        self.representation = None

    def init_from(self, representation:object, problem:Problem)->None:
        if not isinstance(problem, Problem):
            raise TypeError('Parameter \'problem\' must be of type \'Problem\'.')
        self.representation = representation

    def native_representation(self, representation_str:str)->object:
        return representation_str

    def calculate_quality_directly(self, representation:object, 
            problem:Problem)->QualityOfSolution:
        return QualityOfSolution(0, None, 0, None, True)

    def representation_distance_directly(self, solution_code_1:str, solution_code_2:str)->float:
        return 0

    def string_representation(self):
        return str(self.representation)    

    def __str__(self)->str:
        return self.string_rep("|")

    def __repr__(self)->str:
        return self.string_rep("|")

    def __format__(self, spec:str)->str:
        return self.string_rep(spec)  
