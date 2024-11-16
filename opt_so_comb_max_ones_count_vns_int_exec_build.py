from random import randint
from random import choice
from typing import Optional

from uo.problem.problem import Problem
from uo.solution.quality_of_solution import QualityOfSolution
from uo.solution.solution import Solution

from uo.algorithm.metaheuristic.metaheuristic import Metaheuristic
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support import VnsShakingSupport
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support import VnsLocalSearchSupport

class MaxOnesCountProblem2(Problem):

    def __init__(self, dim:int=10)->None:
        if not isinstance(dim, int):
            raise TypeError('Parameter \'dim\' have not valid type.')
        if dim <= 0:
            raise ValueError("Problem dimension should be positive!")
        if dim > 31:
            raise ValueError("Problem dimension should be less than 32")
        self.__dimension = dim
        super().__init__("MaxOnesCountProblem2", is_minimization=False, is_multi_objective=False)   

    def copy(self):
        pr = MaxOnesCountProblem2(self.dimension)
        return pr

    @property
    def dimension(self)->int:
        return self.__dimension

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return ''

    def __str__(self)->str:
        return ''
    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''

class MaxOnesCountProblemIntSolution(Solution[int,str]):
    
    def __init__(self, random_seed:Optional[int]=None)->None:
        if not isinstance(random_seed, int) and random_seed is not None:
            raise TypeError('Parameter \'random_seed\' must be \'int\' or \'None\'.')
        super().__init__(random_seed, 
                fitness_value=None, fitness_values=None, objective_value=None, objective_values=None, is_feasible=False, 
                evaluation_cache_is_used=False, evaluation_cache_max_size=0, 
                distance_calculation_cache_is_used=False, distance_calculation_cache_max_size=0)

    def copy(self):
        sol = MaxOnesCountProblemIntSolution(self.random_seed)
        return sol
        
    def init_random(self, problem:Problem)->None:
        if problem.dimension is None:
            raise ValueError("Problem dimension should not be None!")
        if problem.dimension <= 0:
            raise ValueError("Problem dimension should be positive!")
        if problem.dimension >= 32:
            raise ValueError("Problem dimension should be less than 32!")
        self.representation = randint(0, 2^problem.dimension-1)
        self.representation = self.obtain_feasible_representation(problem)

    def init_from(self, representation:int, problem:Problem)->None:
        if not isinstance(representation, int):
            raise TypeError('Parameter \'representation\' must have type \'int\'.')
        self.representation = representation

    def argument(self)->str:
        return bin(self.representation)

    def calculate_quality_directly(self, representation:int, 
            problem:Problem)->QualityOfSolution:
        ones_count = representation.bit_count()
        return QualityOfSolution(ones_count, None, ones_count, None, True)

    def native_representation(self, representation_str:str)->int:
        ret:int = int(representation_str, 2)
        return ret

    def representation_distance_directly(self, solution_code_1:str, solution_code_2:str)->float:
        rep_1:int = self.native_representation(solution_code_1)
        rep_2:int = self.native_representation(solution_code_2)
        result = (rep_1 ^ rep_2).bit_count()
        return result 

    def argument(self, problem:Problem)->str:
        return bin(self.representation)

    def string_rep(self, delimiter:str='\n', indentation:int=0, indentation_symbol:str='   ', 
            group_start:str='{', group_end:str='}',)->str:
        return ''

    def __str__(self)->str:
        return ''

    def __repr__(self)->str:
        return ''

    def __format__(self, spec:str)->str:
        return ''

class MaxOnesCountProblemIntSolutionVnsShakingSupport(VnsShakingSupport[int,str]):
    
    def __init__(self)->None:
        return

    def copy(self):
        sup = MaxOnesCountProblemIntSolutionVnsShakingSupport()
        return sup
        
    def shaking(self, k:int, problem:MaxOnesCountProblem2, solution:MaxOnesCountProblemIntSolution, 
            optimizer:Metaheuristic )->bool:
        if optimizer.should_finish():
            return False
        tries:int = 0
        limit:int = 10000
        while tries < limit:
            positions:list[int] = []
            for _ in range(0,k):
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
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            return True
        else:
            return False 
        
    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'MaxOnesCountProblemIntSolutionVnsShakingSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')


class MaxOnesCountProblemIntSolutionVnsLocalSearchSupport(VnsLocalSearchSupport[int,str]):
    
    def __init__(self)->None:
        return

    def copy(self):
        sup = MaxOnesCountProblemIntSolutionVnsLocalSearchSupport()
        return sup

    def local_search(self, k:int, problem:MaxOnesCountProblem2, solution:MaxOnesCountProblemIntSolution, 
            optimizer: Metaheuristic)->bool:
        if optimizer.should_finish():
            return False
        if k < 1:
            return False
        # ls_bi for k==1
        start_sol:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution()
        start_sol.copy_from(solution)
        best_sol:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution()
        best_sol.copy_from(solution)
        better_sol_found:bool = False
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            solution.representation ^= mask 
            optimizer.evaluation +=1 
            solution.evaluate(problem)
            if solution.is_better(best_sol, problem):
                better_sol_found = True
                best_sol.copy_from(solution)
            solution.representation ^= mask 
        if better_sol_found:
            solution.copy_from(best_sol)
            return True
        solution.copy_from(start_sol)
        return False

    def local_search_first_improvement(self, k:int, problem:MaxOnesCountProblem2, solution:MaxOnesCountProblemIntSolution, 
            optimizer: Metaheuristic)->bool:
        if optimizer.should_finish():
            return False
        if k < 1:
            return False
        # ls_fi for k==1
        start_sol:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution()
        start_sol.copy_from(solution)
        for i in range(0, problem.dimension):
            mask:int = 1 << i
            solution.representation ^= mask 
            optimizer.write_output_values_if_needed("before_evaluation", "b_e")
            optimizer.evaluation += 1
            solution.evaluate(problem)
            optimizer.write_output_values_if_needed("after_evaluation", "a_e")
            if solution.is_better(start_sol, problem):
                return True
            solution.representation ^= mask
        solution.copy_from(start_sol)
        return False

    def string_rep(self, delimiter:str, indentation:int=0, indentation_symbol:str='', group_start:str ='{', 
        group_end:str ='}')->str:
        return 'MaxOnesCountProblemIntSolutionVnsLocalSearchSupport'

    def __str__(self)->str:
        return self.string_rep('|')

    def __repr__(self)->str:
        return self.string_rep('\n')


    def __format__(self, spec:str)->str:
        return self.string_rep('|')

def main():
    problem_to_solve:MaxOnesCountProblem2 = MaxOnesCountProblem2(dim=24)
    solution:MaxOnesCountProblemIntSolution = MaxOnesCountProblemIntSolution()
    finish:FinishControl = FinishControl( criteria='evaluations & seconds', 
            evaluations_max=500, seconds_max=10)
    vns_shaking_support:MaxOnesCountProblemIntSolutionVnsShakingSupport = \
        MaxOnesCountProblemIntSolutionVnsShakingSupport()
    vns_ls_support:MaxOnesCountProblemIntSolutionVnsLocalSearchSupport = \
        MaxOnesCountProblemIntSolutionVnsLocalSearchSupport()
    vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
    vns_construction_params.problem = problem_to_solve
    vns_construction_params.solution_template = solution
    vns_construction_params.vns_shaking_support = vns_shaking_support
    vns_construction_params.vns_ls_support = vns_ls_support
    vns_construction_params.finish_control = finish
    vns_construction_params.random_seed = 43434343
    vns_construction_params.k_min = 1
    vns_construction_params.k_max = 3
    optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
    bs = optimizer.optimize()
    print('Best solution representation: {}'.format(bs.representation))            
    print('Best solution code: {}'.format(bs.string_representation()))            
    print('Best solution objective:  {}'.format(bs.objective_value))
    print('Best solution fitness: {}'.format(bs.fitness_value))
    print('Number of iterations: {}'.format(optimizer.iteration))            
    print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()
