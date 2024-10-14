
import unittest
import unittest.mock as mocker
from unittest.mock import patch
from unittest.mock import mock_open

from bitstring import BitArray

from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem import MaxOnesCountProblem
from opt.single_objective.comb.max_ones_count_problem.max_ones_count_problem_int_solution import MaxOnesCountProblemIntSolution
from uo.problem.problem import Problem
from uo.problem.problem_void_min_so import ProblemVoidMinSO
from uo.solution.solution import Solution


# Generated by CodiumAI

import unittest

class TestMaxOnesCountProblemIntSolution(unittest.TestCase):

    # Create new instance of MaxOnesCountProblemIntSolution with default parameters
    def test_create_new_instance_with_default_parameters(self):
        # Arrange
        # Act
        solution = MaxOnesCountProblemIntSolution()
        # Assert
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)
        self.assertIsNone(solution.evaluation_cache_cs)
        self.assertIsNone(solution.representation_distance_cache_cs)

    # Create new instance of MaxOnesCountProblemIntSolution with custom parameters
    def test_create_new_instance_with_custom_parameters(self):
        # Arrange
        # Act
        solution = MaxOnesCountProblemIntSolution(random_seed=123, evaluation_cache_is_used=True, 
                            evaluation_cache_max_size=100, distance_calculation_cache_is_used=True, 
                            distance_calculation_cache_max_size=200)
        # Assert
        self.assertIsNone(solution.fitness_value)
        self.assertIsNone(solution.fitness_values)
        self.assertIsNone(solution.objective_value)
        self.assertIsNone(solution.objective_values)
        self.assertFalse(solution.is_feasible)

    # Initialize solution randomly
    def test_initialize_solution_randomly(self):
        # Arrange
        problem_mock = mocker.MagicMock(spec=MaxOnesCountProblem)
        type(problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_mock).dimension = mocker.PropertyMock(return_value=12)
        # Act
        solution = MaxOnesCountProblemIntSolution()
        solution.init_random(problem_mock)
        # Assert
        self.assertIsNotNone(solution.representation)
        self.assertGreaterEqual(solution.representation, 0)
        self.assertLessEqual(solution.representation, 2**problem_mock.dimension - 1)

    # Initialize solution from representation
    def test_initialize_solution_from_representation(self):
        # Arrange
        problem_stub = mocker.MagicMock()
        type(problem_stub).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_stub).dimension = mocker.PropertyMock(return_value=12)
        representation = 12345
        # Act
        solution = MaxOnesCountProblemIntSolution()
        solution.init_from(representation, problem_stub)
        # Assert
        self.assertEqual(solution.representation, representation)

    # Calculate quality directly
    def test_calculate_quality_directly(self):
        # Arrange
        problem_stub = mocker.MagicMock()
        type(problem_stub).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_stub).dimension = mocker.PropertyMock(return_value=12)
        representation = 12345
        # Act
        solution = MaxOnesCountProblemIntSolution()
        quality = solution.calculate_quality_directly(representation, problem_stub)
        # Assert
        self.assertEqual(quality.fitness_value, representation.bit_count())
        self.assertIsNone(quality.fitness_values)
        self.assertEqual(quality.objective_value, representation.bit_count())
        self.assertIsNone(quality.objective_values)
        self.assertTrue(quality.is_feasible)

    # Obtain native representation from string representation
    def test_obtain_native_representation_from_string_representation(self):
        # Arrange
        representation_str = "101010"
        # Act
        solution = MaxOnesCountProblemIntSolution()
        representation = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(representation, int(representation_str, 2))

    # Create new instance of MaxOnesCountProblemIntSolution with negative random seed
    def test_create_new_instance_with_negative_random_seed(self):
        # Arrange
        # Act
        solution = MaxOnesCountProblemIntSolution(random_seed=-123)
        # Assert
        self.assertEqual(solution.random_seed, -123)

    # Create new instance of MaxOnesCountProblemIntSolution with zero dimension
    def test_create_new_instance_with_zero_dimension(self):
        # Arrange
        problem_stub = mocker.MagicMock()
        type(problem_stub).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_stub).dimension = mocker.PropertyMock(return_value=0)
        # Act
        solution = MaxOnesCountProblemIntSolution()
        # Assert
        with self.assertRaises(ValueError):
            solution.init_random(problem_stub)

    # Create new instance of MaxOnesCountProblemIntSolution with dimension greater than or equal to 32
    def test_create_new_instance_with_large_dimension(self):
        # Arrange
        problem_stub = mocker.MagicMock()
        type(problem_stub).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_stub).dimension = mocker.PropertyMock(return_value=32)
        # Act
        solution = MaxOnesCountProblemIntSolution()
        # Assert
        with self.assertRaises(ValueError):
            solution.init_random(problem_stub)

    # Initialize solution randomly with problem dimension set to None
    def test_initialize_solution_randomly_with_none_dimension(self):
        # Arrange
        problem_stub = mocker.MagicMock()
        type(problem_stub).name = mocker.PropertyMock(return_value='some_problem')
        type(problem_stub).dimension = mocker.PropertyMock(return_value=None)
        # Act
        solution = MaxOnesCountProblemIntSolution()
        # Assert
        with self.assertRaises(ValueError):
            solution.init_random(problem_stub)



class TestNativeRepresentation(unittest.TestCase):

    # Obtain int representation from binary string representation
    def test_obtain_int_representation(self):
        # Arrange
        representation_str = "101010"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(result, 42)

    # String representation contains only binary digits
    def test_string_representation_contains_binary_digits(self):
        # Arrange
        representation_str = "101010"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertIsInstance(result, int)

    # String representation is not empty
    def test_string_representation_not_empty(self):
        # Arrange
        representation_str = "101010"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertIsNotNone(result)

    # String representation is '0'
    def test_string_representation_is_zero(self):
        # Arrange
        representation_str = "0"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(result, 0)

    # String representation is '1'
    def test_string_representation_is_one(self):
        # Arrange
        representation_str = "1"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(result, 1)

    # String representation is '00'
    def test_string_representation_is_double_zero(self):
        # Arrange
        representation_str = "00"
        solution = MaxOnesCountProblemIntSolution()
        # Act
        result = solution.native_representation(representation_str)
        # Assert
        self.assertEqual(result, 0)


class TestRepresentationDistanceDirectly(unittest.TestCase):

    # Calculate distance between two solutions with different representation codes.
    def test_different_representation_codes(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution.native_representation = mocker.Mock(side_effect=[10, 15])    
        # Act
        distance = solution.representation_distance_directly("101010", "111000")
        # Assert
        self.assertEqual(distance, 2)

    # Calculate distance between two solutions with same representation codes.
    def test_same_representation_codes(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution.native_representation = mocker.Mock(return_value=10)
        # Act
        distance = solution.representation_distance_directly("101010", "101010")
        # Assert
        self.assertEqual(distance, 0)

    # Calculate distance between two solutions with different lengths of representation codes.
    def test_different_lengths_of_representation_codes(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution.native_representation = mocker.Mock(side_effect=[10, 15])
        # Act
        distance = solution.representation_distance_directly("101010", "111")
        # Assert
        self.assertEqual(distance, 2)

    # Calculate distance between two solutions with non-string representation codes.
    def test_non_string_representation_codes(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        # Act & Assert
        with self.assertRaises(TypeError):
            solution.representation_distance_directly(101010, 111000)

class TestRepresentationDistanceDirectly(unittest.TestCase):

    # Calculate distance between two identical solutions
    def test_identical_solutions(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution_code_1 = "101010"
        solution_code_2 = "101010"
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
        # Assert
        self.assertEqual(distance, 0)

    # Calculate distance between two different solutions
    def test_different_solutions(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution_code_1 = "101010"
        solution_code_2 = "111000"
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
        # Assert
        self.assertEqual(distance, 2)

    # Calculate distance between two solutions with one bit difference
    def test_one_bit_difference(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution_code_1 = "101010"
        solution_code_2 = "101011"
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
        # Assert
        self.assertEqual(distance, 1)

    # Calculate distance between two solutions with different lengths
    def test_different_lengths(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution_code_1 = "101010"
        solution_code_2 = "10101010"
        # Act
        distance = solution.representation_distance_directly(solution_code_1, solution_code_2)
        # Assert
        self.assertEqual(distance, 1)

    # Calculate distance between two solutions with non-binary characters
    def test_non_binary_characters(self):
        # Arrange
        solution = MaxOnesCountProblemIntSolution()
        solution_code_1 = "101010"
        solution_code_2 = "1010A0"
        # Act & Assert
        with self.assertRaises(ValueError):
            solution.representation_distance_directly(solution_code_1, solution_code_2)


# Generated by CodiumAI

import unittest

class TestStringRep(unittest.TestCase):

    # Includes the string representation of the superclass
    def test_includes_superclass_representation(self):
        # Arrange
        sol = MaxOnesCountProblemIntSolution()
        sol.representation = 123
        # Act
        result = sol.string_rep()
        # Assert
        self.assertIsInstance(result, str)

    # Includes the string representation of the solution's native representation
    def test_includes_native_representation(self):
        # Arrange
        sol = MaxOnesCountProblemIntSolution()
        sol.representation = 123    
        # Act
        result = sol.string_rep()
        # Assert
        self.assertIn("string_representation()=", result)

