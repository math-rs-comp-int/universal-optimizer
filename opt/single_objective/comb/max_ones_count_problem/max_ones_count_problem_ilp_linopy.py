import sys
from pathlib import Path
directory = Path(__file__).resolve()
sys.path.append(directory)
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)

from dataclasses import dataclass
from copy import deepcopy
from datetime import datetime

import xarray as xr
from linopy import Model

from uo.utils.logger import logger

from typing import Optional

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.solution.solution_void_representation_object import SolutionVoidIntObject
from uo.solution.quality_of_solution import QualityOfSolution


from uo.algorithm.optimizer import Optimizer
from uo.algorithm.output_control import OutputControl

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem

class MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters:
    """
    Instance of the class :class:`MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters` represents constructor parameters for max ones problem ILP solver.
    """
    def __init__(self, problem: Problem = None, output_control: Optional[OutputControl] = None)->None:
        if not isinstance(output_control, OutputControl) and output_control is not None:
            raise TypeError('Parameter \'output_control\' must have type \'OutputControl\' or be None.')
        if not isinstance(problem, Problem):
            raise TypeError('Parameter \'problem\' must have type \'Problem\'.')
        self.__problem = problem
        self.__output_control = output_control

    @property
    def output_control(self)->OutputControl:
        """
        Property getter for the output control
        
        :return: output control 
        :rtype: `OutputControl`
        """
        return self.__output_control    

    @property
    def problem(self)->Problem:
        """
        Property getter for the output control
        
        :return: problem that is solved
        :rtype: `Problem`
        """
        return self.__problem    


class MaxOnesCountProblemIntegerLinearProgrammingSolution(SolutionVoidIntObject):
    def __init__(self, sol:'MaxOnesCountProblemIntegerLinearProgrammingSolver')->None:
        super().__init__()
        self.__sol = sol

    def string_representation(self):
        return str(self.__sol)    

class MaxOnesCountProblemIntegerLinearProgrammingSolver(Optimizer):

    def __init__(self, output_control:OutputControl=None,  problem:MaxOnesCountProblem=None)->None:
        """
        Create new `MaxOnesCountProblemIntegerLinearProgrammingSolver` instance

        :param `OutputControls` output_control: object that control output
        :param `MaxOnesCountProblem` problem: problem to be solved
        """
        if not isinstance(output_control, OutputControl) and output_control is not None:
            raise TypeError('Parameter \'output_control\' must have type \'OutputControl\' or be None.')
        if not isinstance(problem, MaxOnesCountProblem):
            raise TypeError('Parameter \'problem\' must have type \'MaxOnesCountProblem\'.')
        super().__init__(name="MaxOnesCountProblemIntegerLinearProgrammingSolver",
                problem=problem,  output_control=output_control )
        self.__model = Model()

    @classmethod
    def from_construction_tuple(cls, 
            construction_params:MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters=None):
        """
        Additional constructor. Create new `MaxOnesCountProblemIntegerLinearProgrammingSolver` instance from construction parameters

        :param `MaxOnesCountProblemIntegerLinearProgrammingSolverConstructionParameters` construction_params: parameters for construction 
        """
        return cls(
            construction_params.output_control, 
            construction_params.problem)

    def __copy__(self):
        """
        Internal copy of the current algorithm

        :return:  new `MaxOnesCountProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:`MaxOnesCountProblemIntegerLinearProgrammingSolver`
        """
        alg = deepcopy(self)
        return alg

    def copy(self):
        """
        Copy the current algorithm

        :return:  new `MaxOnesCountProblemIntegerLinearProgrammingSolver` instance with the same properties
        :rtype: :class:``MaxOnesCountProblemIntegerLinearProgrammingSolver``
        """
        return self.__copy__()

    @property
    def model(self)->Model:
        """
        Property getter for the ILP model
        
        :return: model of the problem 
        :rtype: `Model`
        """
        return self.__model    

    def optimize(self)->MaxOnesCountProblemIntegerLinearProgrammingSolution:
        """
        Uses ILP model in order to solve MaxOnesCountProblem
        """
        self.iteration = -1
        self.evaluation = -1
        self.execution_started = datetime.now() 
        l = []
        for _ in range(self.problem.dimension):
            l.append(0)
        coords = xr.DataArray(l)
        x = self.model.add_variables(binary=True, coords=[coords], name='x')
        #logger.debug(self.model.variables)
        if self.problem.is_minimization:
            self.model.add_objective((x).sum(), sense="min")
        else:
            self.model.add_objective((x).sum(),sense="max")
        self.model.solve()
        self.execution_ended = datetime.now()
        self.write_output_values_if_needed("after_algorithm", "a_a")
        self.best_solution = MaxOnesCountProblemIntegerLinearProgrammingSolution( self.model.solution.x )
        #logger.debug(self.model.solution.x)
        return self.best_solution

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        """
        String representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        
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
        s += group_end 
        return s

    def __str__(self)->str:
        """
        String representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')

    def __repr__(self)->str:
        """
        Representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :return: string representation of the 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('\n')

    def __format__(self, spec:str)->str:
        """
        Formatted 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        
        :param str spec: format specification
        :return: formatted 'MaxOnesCountProblemIntegerLinearProgrammingSolver' instance
        :rtype: str
        """
        return self.string_rep('|')