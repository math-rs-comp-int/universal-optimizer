from datetime import datetime
import unittest   
import unittest.mock as mock
from uo.algorithm.metaheuristic.additional_statistics_control import AdditionalStatisticsControl

from uo.problem.problem import Problem
from uo.solution.solution import Solution
from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.monte_carlo.monte_carlo_optimizer import MonteCarloOptimizerConstructionParameters
from uo.algorithm.metaheuristic.monte_carlo.monte_carlo_optimizer import MonteCarloOptimizer
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution_void_representation_int import SolutionVoidInt


class TestMonteCarloOptimizer(unittest.TestCase):

    # Initializes MonteCarloOptimizer with valid parameters and runs without errors
    def test_initialization_with_valid_parameters(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
        solution_template = mock.Mock(spec=Solution)
    
        # Act
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
    
        # Assert
        self.assertIsInstance(optimizer, MonteCarloOptimizer)

    # Successfully creates a MonteCarloOptimizer instance using from_construction_tuple method
    def test_from_construction_tuple(self):
        # Arrange
        construction_params = MonteCarloOptimizerConstructionParameters(
            finish_control=mock.Mock(spec=FinishControl),
            problem=mock.Mock(spec=Problem),
            solution_template=mock.Mock(spec=Solution)
        )
    
        # Act
        optimizer = MonteCarloOptimizer.from_construction_tuple(construction_params)
    
        # Assert
        self.assertIsInstance(optimizer, MonteCarloOptimizer)

    # Properly initializes the current and best solutions during the init method
    def test_init_method_initializes_solutions(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
        solution_template = SolutionVoidInt()
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
    
        # Act
        optimizer.init()
    
        # Assert
        self.assertIsNotNone(optimizer.current_solution)
        self.assertIsNotNone(optimizer.best_solution)

    # Executes main_loop_iteration and updates best_solution when improvement is found
    def test_main_loop_iteration_updates_best_solution(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
        solution_template = SolutionVoidInt()
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
        optimizer.init()
    
        optimizer.current_solution.is_better = mock.Mock(return_value=True)
    
        # Act
        optimizer.main_loop_iteration()
    
        # Assert
        self.assertEqual(optimizer.best_solution.representation, optimizer.current_solution.representation)

    # Generates correct string representation of MonteCarloOptimizer instance
    def test_string_representation(self):
        # Arrange
        finish_control = FinishControl()
        problem = ProblemVoidMinSO()
        solution_template = SolutionVoidInt()        
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
    
        # Act
        string_rep = str(optimizer)
    
        # Assert
        self.assertIn('MonteCarlo', string_rep)

    # Handles None values for optional parameters without raising exceptions
    def test_handles_none_optional_parameters(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
    
        # Act & Assert
        try:
            MonteCarloOptimizer(finish_control, problem, None, None, None, None)
            success = True
        except Exception:
            success = False
    
        self.assertTrue(success)

    # Correctly handles cases where no improvement is found in main_loop_iteration
    def test_main_loop_iteration_no_improvement(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
        solution_template = SolutionVoidInt()
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
        optimizer.init()
    
        initial_best_solution = optimizer.best_solution
    
        optimizer.current_solution.is_better = mock.Mock(return_value=False)
    
        # Act
        optimizer.main_loop_iteration()
    
        # Assert
        self.assertEqual(optimizer.best_solution, initial_best_solution)

    # Manages invalid types for parameters in the constructor gracefully
    def test_invalid_parameter_types_in_constructor(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            MonteCarloOptimizer("invalid", "invalid", "invalid")

    # Handles scenarios where the problem is not properly defined
    def test_problem_not_properly_defined(self):
        # Arrange & Act & Assert
        with self.assertRaises(TypeError):
            MonteCarloOptimizer(mock.Mock(spec=FinishControl), None, mock.Mock(spec=Solution))

    # Ensures deep copy functionality works correctly for MonteCarloOptimizer instances
    def test_deep_copy_functionality(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
        solution_template = mock.Mock(spec=Solution)
    
        optimizer = MonteCarloOptimizer(finish_control, problem, solution_template)
    
        # Act
        copied_optimizer = optimizer.copy()
    
        # Assert
        self.assertNotEqual(id(optimizer), id(copied_optimizer))

    # Validates that random_seed affects the randomness of the solution initialization
    def test_random_seed_affects_randomness(self):
        # Arrange
        finish_control = mock.Mock(spec=FinishControl)
        problem = mock.Mock(spec=Problem)
    
        solution_template1 = SolutionVoidInt()
        solution_template2 = SolutionVoidInt()

        optimizer1 = MonteCarloOptimizer(finish_control, problem, solution_template1, random_seed=42)
        optimizer2 = MonteCarloOptimizer(finish_control, problem, solution_template2, random_seed=42)

        # Act
        optimizer1.init()
        optimizer2.init()

        # Assert (assuming init_random affects some state that can be compared)
        self.assertEqual(optimizer1.current_solution.representation, optimizer2.current_solution.representation)  