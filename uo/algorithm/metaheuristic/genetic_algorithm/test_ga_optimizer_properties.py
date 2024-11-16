import unittest   
import unittest.mock as mocker

from uo.problem.problem import Problem


from uo.algorithm.output_control import OutputControl
from uo.algorithm.metaheuristic.finish_control import FinishControl
from uo.algorithm.metaheuristic.genetic_algorithm.ga_optimizer_gen import GaOptimizerGenerational
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection import GaSelection
from uo.algorithm.metaheuristic.genetic_algorithm.ga_selection_roulette import GaSelectionRoulette
from uo.algorithm.metaheuristic.genetic_algorithm.ga_crossover_support import GaCrossoverSupport
from uo.algorithm.metaheuristic.genetic_algorithm.ga_mutation_support import GaMutationSupport
from uo.solution.solution_void_representation_int import SolutionVoidInt

class TestGaOptimizerGenerationalProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestGaOptimizerGenerationalProperties\n")

    def setUp(self):
        self.output_control_stub = mocker.MagicMock(spec=OutputControl)

        self.problem_mock = mocker.MagicMock(spec=Problem)
        type(self.problem_mock).name = mocker.PropertyMock(return_value='some_problem')
        type(self.problem_mock).is_minimization = mocker.PropertyMock(return_value=True)
        type(self.problem_mock).file_path = mocker.PropertyMock(return_value='some file path')
        type(self.problem_mock).dimension = mocker.PropertyMock(return_value=42)
        self.problem_mock.copy = mocker.Mock(return_value=self.problem_mock)

        self.selection_roulette_mock =  mocker.MagicMock(spec=GaSelectionRoulette)
        
        self.ga_support_crossover_stub = mocker.MagicMock(spec=GaCrossoverSupport)
        type(self.ga_support_crossover_stub).copy = mocker.CallableMixin(spec="return self")        
        self.ga_support_mutation_stub = mocker.MagicMock(spec=GaMutationSupport)
        type(self.ga_support_mutation_stub).copy = mocker.CallableMixin(spec="return self")        
        
        self.evaluations_max = 42
        self.iterations_max = 42
        self.seconds_max = 42
        self.finish_control_mock = mocker.MagicMock(spec=FinishControl)
        type(self.finish_control_mock).evaluations_max= mocker.PropertyMock(return_value=self.evaluations_max)
        type(self.finish_control_mock).iterations_max= mocker.PropertyMock(return_value=self.iterations_max)
        type(self.finish_control_mock).seconds_max= mocker.PropertyMock(return_value=self.seconds_max)
        self.finish_control_mock.copy = mocker.Mock(return_value=self.finish_control_mock)
        
        self.random_seed = 42
        self.mutation_probability = 0.1
        self.selection_type = 'selectionRoulette'
        self.tournament_size = 10
        self.population_size = 100
        self.elitism_size = 10

        self.ga_optimizer:GaOptimizerGenerational = GaOptimizerGenerational(
                output_control=self.output_control_stub,
                problem=self.problem_mock, 
                solution_template=SolutionVoidInt( 43, 0, 0, False),
                ga_selection=self.selection_roulette_mock,
                ga_crossover_support=self.ga_support_crossover_stub,
                ga_mutation_support=self.ga_support_mutation_stub,
                finish_control=self.finish_control_mock,
                random_seed=self.random_seed,
                population_size=self.population_size,
                elite_count=self.elitism_size
        )

    def test_name_should_be_ga(self):
        self.assertEqual(self.ga_optimizer.name, 'ga')

    def test_evaluations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.finish_control.evaluations_max, self.finish_control_mock.evaluations_max)

    def test_iterations_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.finish_control.iterations_max, self.finish_control_mock.iterations_max)

    def test_random_seed_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.random_seed, self.random_seed)

    def test_seconds_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.finish_control.seconds_max, self.finish_control_mock.seconds_max)

    def test_elite_count_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.elite_count, self.elitism_size)

    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.problem.name, self.problem_mock.name)

    def test_problem_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.problem.is_minimization, self.problem_mock.is_minimization)

    def test_problem_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.problem.file_path, self.problem_mock.file_path)

    def test_problem_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.ga_optimizer.problem.dimension, self.problem_mock.dimension)

    def test_create_with_invalid_selection_type_should_raise_value_exception_with_proper_message(self):
        with self.assertRaises(TypeError) as context:
            selection_stub = mocker.MagicMock(spec=GaSelectionRoulette)
            type(selection_stub).selection_roulette = mocker.CallableMixin(spec=lambda x: x)
            type(selection_stub).copy = mocker.CallableMixin(spec="return self")
            self.ga_optimizer:GaOptimizerGenerational = GaOptimizerGenerational(
                output_control=self.output_control_stub,
                problem=self.problem_mock, 
                solution_template=SolutionVoidInt( 43, 0, 0, False),
                ga_selection="not appropriate type",
                ga_crossover_support=self.ga_support_crossover_stub,
                ga_mutation_support=self.ga_support_mutation_stub,
                finish_control=self.finish_control_mock,
                random_seed=self.random_seed,
                population_size=self.population_size,
                elite_count=self.elitism_size
            )
        self.assertEqual('Parameter \'ga_selection\' must be \'GaSelection\'.', context.exception.args[0])

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestGaOptimizerGenerationalProperties")
    
if __name__ == '__main__':
    unittest.main()