from random import randint
from random import choice
from random import randint
import networkx as nx

from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl

from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_shaking_support_standard_bit_array import \
        VnsShakingSupportStandardBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_ls_support_standard_bi_bit_array import \
        VnsLocalSearchSupportStandardBestImprovementBitArray
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizerConstructionParameters
from uo.algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem import MinMultiCutProblem
from opt.single_objective.comb.min_multi_cut_problem.min_multi_cut_problem_bit_array_solution import \
                MinMultiCutProblemBitArraySolution

def main():
        nodes = 10
        prob = 0.5
        graph: nx.Graph = nx.fast_gnp_random_graph(nodes, prob, seed=11)
        for edge in graph.edges():
                graph.edges[edge]['weight'] = randint(1,10)
        nodes = list(graph.nodes())
        num_pairs = randint(1, max(2,len(nodes)//3))
        source_terminal_pairs = []
        for _ in range(num_pairs):
                source = choice(nodes)
                terminal_candidates = [node for node in nodes if node != source]
                terminal = choice(terminal_candidates)
                source_terminal_pairs.append((source, terminal))

        problem_to_solve:MinMultiCutProblem = MinMultiCutProblem(graph, source_terminal_pairs)
        solution:MinMultiCutProblemBitArraySolution = MinMultiCutProblemBitArraySolution()
        finish:FinishControl = FinishControl(criteria='evaluations', evaluations_max=500)
        num_edges:int = len(problem_to_solve.graph.edges())
        vns_shaking_support:VnsShakingSupportStandardBitArray = \
                VnsShakingSupportStandardBitArray(dimension=num_edges)
        vns_ls_support:VnsLocalSearchSupportStandardBestImprovementBitArray = \
                VnsLocalSearchSupportStandardBestImprovementBitArray(dimension=num_edges)
        vns_construction_params:VnsOptimizerConstructionParameters = VnsOptimizerConstructionParameters()
        vns_construction_params.problem = problem_to_solve
        vns_construction_params.solution_template = solution
        vns_construction_params.finish_control = finish
        vns_construction_params.random_seed = 43434343
        vns_construction_params.vns_shaking_support = vns_shaking_support
        vns_construction_params.vns_ls_support = vns_ls_support
        vns_construction_params.k_min = 1
        vns_construction_params.k_max = 3
        optimizer:VnsOptimizer = VnsOptimizer.from_construction_tuple(vns_construction_params)
        optimizer.optimize()
        print('Best solution representation: {}'.format(optimizer.best_solution.representation.bin))            
        print('Best solution code: {}'.format(optimizer.best_solution.string_representation()))            
        print('Best solution objective: {}'.format(optimizer.best_solution.objective_value))
        print('Best solution fitness: {}'.format(optimizer.best_solution.fitness_value))
        print('Number of iterations: {}'.format(optimizer.iteration))            
        print('Number of evaluations: {}'.format(optimizer.evaluation))            

if __name__ == '__main__':
        main()