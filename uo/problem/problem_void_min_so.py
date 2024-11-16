""" 
The :mod:`~uo.problem.problem` module describes the class :class:`~uo.problem.Problem`.
"""

from abc import ABCMeta
from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)

from uo.problem.problem import Problem 

class ProblemVoidMinSO(Problem):
    
    def __init__(self, name:str="problem_void_minimization_single_optimization", 
                is_minimization:bool = True, 
                is_multi_objective:bool=False)->None:
        if not isinstance(is_minimization, bool):
                raise TypeError('Parameter \'is_minimization\' must be \'bool\'.')        
        if not isinstance(is_multi_objective, bool):
                raise TypeError('Parameter \'is_multi_objective\' must be \'bool\' .')        
        super().__init__(name, is_minimization, is_multi_objective)

    def copy(self):
        """
        Copy the `ProblemVoidMinSO`
        
        :return: new `ProblemVoidMinSO` instance with the same properties
        :rtype: `ProblemVoidMinSO`
        """        
        obj:ProblemVoidMinSO = ProblemVoidMinSO("problem void min so", 
                                    True,
                                    False)
        return obj
    
    @classmethod
    def __load_from_file__(cls, data_representation: str)->None:
        return

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''
    
