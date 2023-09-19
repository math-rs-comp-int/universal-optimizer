from pathlib import Path
directory = Path(__file__).resolve()
import sys
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)
sys.path.append(directory.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent)
sys.path.append(directory.parent.parent.parent.parent.parent.parent.parent.parent)

import unittest   
import unittest.mock as mock

from uo.target_problem.target_problem import TargetProblem 

class TestTargetProblem(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass TestTargetProblem\n")

    def setUp(self):
        self.problem_name = 'some problem'
        self.to_minimize = True
        self.dimension = 42
        self.file_path = 'some file path'

        self.problem = TargetProblem(
                name=self.problem_name,
                is_minimization = self.to_minimize,
                dimension=self.dimension,
                file_path=self.file_path  
        )
        return
    
    def test_problem_name_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.name, self.problem_name)

    def test_is_minimization_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.is_minimization, self.to_minimize)

    def test_dimension_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.dimension, self.dimension)

    def test_file_path_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.problem.file_path, self.file_path)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass TestTargetProblem")
    
if __name__ == '__main__':
    unittest.main()